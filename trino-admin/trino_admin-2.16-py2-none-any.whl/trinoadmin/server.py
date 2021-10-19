# -*- coding: utf-8 -*-
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Module for installing, monitoring, and controlling presto server
using presto-admin
"""
import cgi
import logging
import re
import socket
import sys
import urllib2
import urlparse
from contextlib import closing

from fabric.api import task, sudo, env
from fabric.context_managers import settings, hide
from fabric.decorators import runs_once, with_settings
from fabric.operations import run, os
from fabric.tasks import execute
from fabric.utils import warn, error, abort
from retrying import retry, RetryError

import util.filesystem
from trinoadmin import catalog
from trinoadmin import configure_cmds
from trinoadmin import package
from trinoadmin.standalone.config import StandaloneConfig
from trinoadmin.trinoclient import TrinoClient
from trinoadmin.util import constants
from trinoadmin.util.base_config import requires_config
from trinoadmin.util.exception import ConfigFileNotFoundError, ConfigurationError
from trinoadmin.util.fabricapi import get_host_list, get_coordinator_role
from trinoadmin.util.local_config_util import get_catalog_directory
from trinoadmin.util.remote_config_util import lookup_port, \
    lookup_server_log_file, lookup_launcher_log_file, lookup_string_config

__all__ = ['install', 'uninstall', 'upgrade', 'start', 'stop', 'restart',
           'status']

if constants.BRAND == 'trino':
    INIT_SCRIPTS = '/etc/init.d/trino'
else:
    INIT_SCRIPTS = '/etc/init.d/presto'

RETRY_TIMEOUT = 120
SYSTEM_RUNTIME_NODES = 'select * from system.runtime.nodes'


def old_sysnode_processor(node_info_rows):
    def old_transform(node_is_active):
        return 'active' if node_is_active else 'inactive'

    return get_sysnode_info_from(node_info_rows, old_transform)


def new_sysnode_processor(node_info_rows):
    return get_sysnode_info_from(node_info_rows, lambda x: x)


# NODE_INFO_PER_URI_SQL = VersionRangeList(
#     VersionRange((0, 0), (0, 128),
#                  ('select http_uri, node_version, active from '
#                   'system.runtime.nodes where '
#                   'url_extract_host(http_uri) = \'%s\'',
#                   old_sysnode_processor)),
#     VersionRange((0, 128), (sys.maxsize,),
#                  ('select http_uri, node_version, state from '
#                   'system.runtime.nodes where '
#                   'url_extract_host(http_uri) = \'%s\'',
#                   new_sysnode_processor))
# )
NODE_INFO_PER_URI_SQL = 'select http_uri, node_version, state from ' + \
                        'system.runtime.nodes where ' + \
                        'url_extract_host(http_uri) = \'%s\''

EXTERNAL_IP_SQL = 'select url_extract_host(http_uri) from ' \
                  'system.runtime.nodes WHERE node_id = \'%s\''
CATALOG_INFO_SQL = 'select catalog_name from system.metadata.catalogs'
_LOGGER = logging.getLogger(__name__)

DOWNLOAD_DIRECTORY = '/tmp'
DEFAULT_RPM_NAME = constants.BRAND + '-server-rpm.rpm'
if constants.BRAND == 'trino':
    LATEST_RPM_URL = 'https://repository.sonatype.org/service/local/artifact/maven' \
                     '/content?r=central-proxy&g=io.trinodb' \
                     '&a=trino-server-rpm&e=rpm&v=RELEASE'
else:
    LATEST_RPM_URL = 'https://repository.sonatype.org/service/local/artifact/maven' \
                     '/content?r=central-proxy&g=com.facebook.presto' \
                     '&a=presto-server-rpm&e=rpm&v=RELEASE'


class LocalPrestoRpmFinder:
    def __init__(self, local_path):
        self.local_path = local_path

    @staticmethod
    def _check_rpm_uncorrupted(rpm_path):
        # package.check_if_valid_rpm() outputs information that is not applicable
        # to this function
        # stderr is redirected to not be displayed and should be restored at the
        # end of the function to behave as expected later
        old_stderr = sys.stderr
        sys.stderr = open(os.devnull, 'w')
        try:
            package.check_if_valid_rpm(rpm_path)
        except SystemExit:
            try:
                os.remove(rpm_path)
                warn('Removed corrupted rpm at: %s' % rpm_path)
            except OSError:
                pass
            return False
        finally:
            sys.stderr = old_stderr

        return True

    def _check_if_absolute_path(self):
        if os.path.isfile(self.local_path) and self._check_rpm_uncorrupted(self.local_path):
            print('Found existing rpm at: %s' % self.local_path)
            return self.local_path
        else:
            return None

    def _check_if_relative_path(self, directory_path):
        path_relative_to_download_dir = os.path.join(directory_path, self.local_path)
        if os.path.isfile(path_relative_to_download_dir) and self._check_rpm_uncorrupted(path_relative_to_download_dir):
            print('Found existing rpm at: %s' % path_relative_to_download_dir)
            return path_relative_to_download_dir
        else:
            return None

    def find_local_presto_rpm(self):
        rpm_at_absolute_path = self._check_if_absolute_path()
        if rpm_at_absolute_path:
            return rpm_at_absolute_path

        rpm_at_relative_path = self._check_if_relative_path(DOWNLOAD_DIRECTORY)
        if rpm_at_relative_path:
            return rpm_at_relative_path

        return None


class UrlHandler:
    def __init__(self, url):
        self.url = url
        self.url_response = None
        try:
            self.url_response = urllib2.urlopen(self.url)
        except urllib2.HTTPError as e:
            _LOGGER.error('Url %s responded with code %s' % (url, e.code))
            raise

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close_url()

    def get_url(self):
        return self.url_response.geturl()

    def get_content_length(self):
        try:
            headers = self.url_response.info()
            return int(headers['Content-Length'])
        except (KeyError, ValueError):
            # Handle the case when the server does not include
            # the 'Content-Length' header
            return None

    def get_download_file_name(self, version=None):
        try:
            headers = self.url_response.info()
            content_disposition = headers['Content-Disposition']
            values, params = cgi.parse_header(content_disposition)
            return params['filename']
        except KeyError:
            # Handle the case when the server does not include
            # the 'Content-Disposition' header
            if not version:
                return DEFAULT_RPM_NAME
            else:
                return DEFAULT_RPM_NAME.rsplit('.', 1)[0] + version + '.rpm'

    def read_block(self, block_size):
        return self.url_response.read(block_size)

    def close_url(self):
        if self.url_response:
            self.url_response.close()


class PrestoRpmDownloader:
    def __init__(self, url_handler):
        self.url_handler = url_handler

    def download_rpm(self, version=None):
        content_length = self.url_handler.get_content_length()
        download_file_path = self.get_download_file_path(version)

        with open(download_file_path, 'wb') as local_file:
            bytes_read = 0
            block_size = 16 * 1024 * 1024
            while True:
                download_buffer = self.url_handler.read_block(block_size)
                if not download_buffer:
                    break
                bytes_read += len(download_buffer)
                local_file.write(download_buffer)
                self.print_download_status(bytes_read, content_length)
            print("Downloaded %d bytes" % bytes_read)

        print('Rpm downloaded to: %s' % download_file_path)
        return download_file_path

    def get_download_file_path(self, version=None):
        return os.path.join(DOWNLOAD_DIRECTORY, self.url_handler.get_download_file_name(version))

    @staticmethod
    def print_download_status(bytes_read, content_length):
        if content_length:
            percent = float(bytes_read) / content_length
            percent = round(percent * 100, 2)
            print('Downloaded %d of %d bytes (%0.2f%%)' %
                  (bytes_read, content_length, percent))


class PrestoRpmFetcher:
    def __init__(self, rpm_specifier):
        self.rpm_specifier = rpm_specifier

    def check_valid_version(self):
        return re.match('^[0-9]+(\.[0-9]+){0,2}$', self.rpm_specifier)

    @staticmethod
    def _find_or_download_latest_presto_rpm():
        return PrestoRpmFetcher.find_or_download_rpm_by_url(LATEST_RPM_URL)

    def use_rpm_specifier_as_latest(self):
        print('Using rpm_specifier as "latest"\n'
              'Fetching the latest presto rpm')
        return self._find_or_download_latest_presto_rpm()

    def _find_or_download_rpm_by_version(self, rpm_version):
        # See here for more information: http://search.maven.org/#api
        if constants.BRAND == 'trino':
            download_url = 'http://search.maven.org/remotecontent?filepath=io/trinodb/' \
                           'trino-server-rpm/' + rpm_version + '/trino-server-rpm-' + \
                           rpm_version + '.rpm'
        else:
            download_url = 'http://search.maven.org/remotecontent?filepath=com/facebook/presto/' \
                           'presto-server-rpm/' + rpm_version + '/presto-server-rpm-' + \
                           rpm_version + '.rpm'

        return self.find_or_download_rpm_by_url(download_url, rpm_version)

    def use_rpm_specifier_as_version(self):
        print('Using rpm_specifier as a version\n'
              'Fetching presto rpm version %s' % self.rpm_specifier)
        return self._find_or_download_rpm_by_version(self.rpm_specifier)

    def use_rpm_specifier_as_url(self):
        print('Using rpm_specifier as a url\n'
              'Fetching presto rpm at url: %s' % self.rpm_specifier)
        return self.find_or_download_rpm_by_url(self.rpm_specifier)

    def use_rpm_specifier_as_local_path(self):
        print('Using rpm_specifier as a local path\n'
              'Fetching local presto rpm at path: %s' % self.rpm_specifier)
        local_finder = LocalPrestoRpmFinder(self.rpm_specifier)
        return local_finder.find_local_presto_rpm()

    @staticmethod
    def find_or_download_rpm_by_url(url, version=None):
        """
        Args:
            url:      The url of the presto rpm to be downloaded.
            version:  An optional version number.
                      If the server doesn't respond with the file name that is being
                      requested, this allows the downloaded file to have the correct
                      version attached to its name (presto-server-rpm-'version'.rpm)
                      rather than the default name

        If downloading the presto rpm at the given url would overwrite an existing rpm,
        this function returns the path to the existing rpm. However, if the rpm that
        would be downloaded takes the default rpm name, it will overwrite the existing
        rpm because there is no way to know if the default rpm name is of the same version
        as the requested rpm. If the rpm is corrupted, this function will remove the corrupted
        rpm and attempt to download it.

        Returns:
            The path to the downloaded or found presto rpm
        """
        with UrlHandler(url) as url_handler:
            downloader = PrestoRpmDownloader(url_handler)
            download_file_path = downloader.get_download_file_path(version)
            local_finder = LocalPrestoRpmFinder(download_file_path)
            local_rpm_path = local_finder.find_local_presto_rpm()
            if local_rpm_path and os.path.basename(local_rpm_path) != DEFAULT_RPM_NAME:
                print('Found and using local presto rpm at path: %s\n'
                      'Delete the existing rpm to force a new download' % local_rpm_path)
                return local_rpm_path
            elif local_rpm_path:
                print('Found local presto rpm at path: %s\n'
                      'The rpm has the default name, so it will not be used' % local_rpm_path)
            print('Downloading rpm from %s\n'
                  'to %s\n'
                  'This can take a few minutes' % (url_handler.get_url(), download_file_path))
            return downloader.download_rpm(version)

    def get_path_to_presto_rpm(self):
        """
        This function finds and downloads (if necessary) the requested presto rpm, which can be
        figured out from the rpm_specifier. The rpm_specifier can take many forms:
        'latest', url, version, and local path (from highest to lowest precedence). This function
        interprets the rpm_specifier only as the highest precedence form.
        """
        scheme, netloc, path, parameters, query, fragment = urlparse.urlparse(self.rpm_specifier)
        if self.rpm_specifier == "latest":
            rpm_path = self.use_rpm_specifier_as_latest()
        elif scheme != '' and scheme != 'file':
            rpm_path = self.use_rpm_specifier_as_url()
        elif self.check_valid_version():
            rpm_path = self.use_rpm_specifier_as_version()
        else:
            rpm_path = self.use_rpm_specifier_as_local_path()

        if not rpm_path:
            abort('Unable to find or download presto rpm with specifier %s' % self.rpm_specifier)
        else:
            return rpm_path


@task
@runs_once
@requires_config(StandaloneConfig)
def install(rpm_specifier):
    """
    Copy and install the presto-server rpm to all the nodes in the cluster and
    configure the nodes.

    The topology information will be read from the config.json file. If this
    file is missing, then the coordinator and workers will be obtained
    interactively. Install will fail for invalid json configuration.

    The catalog configurations will be read from the local catalog directory
    which defaults to ~/.prestoadmin/catalog. If this directory is missing or empty
    then no catalog configuration is deployed.

    Install will fail for incorrectly formatted configuration files. Expected
    format is key=value for .properties files and one option per line for
    jvm.config

    Parameters:
        rpm_specifier - String specifying location of presto rpm to copy and install
                        to nodes in the cluster. The string can specify a presto rpm
                        in the following ways:

                        1.  'latest' to download the latest release
                        2.  Url to download
                        3.  Version number to download
                        4.  Path to a local copy

                        If rpm_specifier matches multiple forms, it is interpreted as the form with
                        highest precedence. The forms are listed from highest to lowest precedence
                        (going top to bottom) For example, if the rpm_specifier matches the criteria
                        to be a url to download, it will be interpreted as such and will never be
                        interpreted as a version number or a local path.

                        Before downloading an rpm, install will attempt to find a local
                        copy with a matching version number to the requested rpm. If such
                        a match is found, it will use the local copy instead of downloading
                        the rpm again.

        --nodeps -      (optional) Flag to indicate if server install
                        should ignore checking Presto rpm package
                        dependencies. Equivalent to adding --nodeps
                        flag to rpm -i.

        --no-config-update - pass this in order to avoid server update after installation
    """
    rpm_fetcher = PrestoRpmFetcher(rpm_specifier)
    path_to_rpm = rpm_fetcher.get_path_to_presto_rpm()
    package.check_if_valid_rpm(path_to_rpm)
    return execute(deploy_install_configure, path_to_rpm, hosts=get_host_list())


def _do_config():
    return False if env.no_config_update else True


def deploy_install_configure(local_path):
    package.deploy_install(local_path)
    if _do_config():
        update_configs()
    wait_for_presto_user()


def add_tpch_catalog():
    tpch_catalog_config = os.path.join(get_catalog_directory(), 'tpch.properties')
    util.filesystem.write_to_file_if_not_exists('connector.name=tpch', tpch_catalog_config)


def update_configs():
    configure_cmds.deploy()

    add_tpch_catalog()
    try:
        catalog.add()
    except ConfigFileNotFoundError:
        _LOGGER.info('No catalog directory found, not adding catalogs.')


@retry(stop_max_delay=3000, wait_fixed=250)
def wait_for_presto_user():
    ret = sudo('getent passwd presto', quiet=True)
    if not ret.succeeded:
        raise Exception('Presto package was not installed successfully. '
                        'Presto user was not created.')


@task
@requires_config(StandaloneConfig)
def uninstall():
    """
    Uninstall Presto after stopping the services on all nodes

    Parameters:
        --nodeps -              (optional) Flag to indicate if server uninstall
                                should ignore checking Presto rpm package
                                dependencies. Equivalent to adding --nodeps
                                flag to rpm -e.
    """
    stop()

    if package.is_rpm_installed(constants.BRAND):
        package.rpm_uninstall(constants.BRAND)
    elif package.is_rpm_installed(constants.BRAND + '-server'):
        package.rpm_uninstall(constants.BRAND + '-server')
    elif package.is_rpm_installed(constants.BRAND + '-server-rpm'):
        package.rpm_uninstall(constants.BRAND + '-server-rpm')
    else:
        abort('Unable to uninstall package on: ' + env.host)


@task
@requires_config(StandaloneConfig)
def upgrade(new_rpm_path, local_config_dir=None, overwrite=False):
    """
    Copy and upgrade a new presto-server rpm to all of the nodes in the
    cluster. Retains existing node configuration.

    The existing topology information is read from the config.json file.
    Unlike install, there is no provision to supply topology information
    interactively.

    The existing cluster configuration is collected from the nodes on the
    cluster and stored on the host running presto-admin. After the
    presto-server packages have been upgraded, presto-admin pushes the
    collected configuration back out to the hosts on the cluster.

    Note that the configuration files in the presto-admin configuration
    directory are not updated during upgrade.

    :param new_rpm_path -       The path to the new Presto RPM to
                                install
    :param local_config_dir -   (optional) Directory to store the cluster
                                configuration in. If not specified, a temp
                                directory is used.
    :param overwrite -          (optional) if set to True then existing
                                configuration will be orerwriten.

    :param --nodeps -           (optional) Flag to indicate if server upgrade
                                should ignore checking Presto rpm package
                                dependencies. Equivalent to adding --nodeps
                                flag to rpm -U.
    """
    stop()

    temp_config_tar = configure_cmds.gather_config_directory()

    package.deploy_upgrade(new_rpm_path)

    configure_cmds.deploy_config_directory(temp_config_tar)


def service(control=None):
    if check_presto_version() != '':
        return False
    if control == 'start' and is_port_in_use(env.host):
        return False
    _LOGGER.info('Executing %s on presto server' % control)
    ret = sudo('set -m; ' + INIT_SCRIPTS + ' ' + control)
    return ret.succeeded


def check_status_for_control_commands():
    print('Waiting to make sure we can connect to the Presto server on %s, '
          'please wait. This check will time out after %d minutes if the '
          'server does not respond.'
          % (env.host, (RETRY_TIMEOUT / 60)))
    if check_server_status():
        print('Server started successfully on: ' + env.host)
    else:
        warn('Could not verify server status for: ' + env.host +
             '\nThis could mean that the server failed to start or that there was no coordinator or worker up. '
             'Please check ' + lookup_server_log_file(env.host) + ' and ' +
             lookup_launcher_log_file(env.host))


def is_port_in_use(host):
    _LOGGER.info("Checking if port used by Prestoserver is already in use..")
    try:
        portnum = lookup_port(host)
    except Exception:
        _LOGGER.info("Cannot find port from config.properties. "
                     "Skipping check for port already being used")
        return 0
    with settings(hide('warnings', 'stdout'), warn_only=True):
        output = run('netstat -lnt |grep -E "\<%s\>" |grep LISTEN' % str(portnum))
    if output:
        _LOGGER.info("Presto server port already in use. Skipping "
                     "server start...")
        error('Server failed to start on %s. Port %s already in use'
              % (env.host, str(portnum)))
    return output


@task
@requires_config(StandaloneConfig)
def start():
    """
    Start the Presto server on all nodes

    A status check is performed on the entire cluster and a list of
    servers that did not start, if any, are reported at the end.
    """
    if service('start'):
        check_status_for_control_commands()


@task
@requires_config(StandaloneConfig)
def stop():
    """
    Stop the Presto server on all nodes
    """
    service('stop')


def stop_and_start():
    if check_presto_version() != '':
        return False
    sudo('set -m; ' + INIT_SCRIPTS + ' stop')
    if is_port_in_use(env.host):
        return False
    _LOGGER.info('Executing start on presto server')
    ret = sudo('set -m; ' + INIT_SCRIPTS + ' start')
    return ret.succeeded


@task
@requires_config(StandaloneConfig)
def restart():
    """
    Restart the Presto server on all nodes.

    A status check is performed on the entire cluster and a list of
    servers that did not start, if any, are reported at the end.
    """
    if stop_and_start():
        check_status_for_control_commands()


def check_presto_version():
    """
    Checks that the Presto version is suitable.

    Returns:
        Error string if applicable
    """
    if not presto_installed():
        not_installed_str = constants.BRAND.capitalize() + ' is not installed.'
        warn(not_installed_str)
        return not_installed_str

    return ''


def presto_installed():
    with settings(hide('warnings', 'stdout'), warn_only=True):
        package_search = run('rpm -q ' + constants.BRAND + '-server-rpm')
        if not package_search.succeeded:
            package_search = run('rpm -q ' + constants.BRAND)
        if not package_search.succeeded:
            package_search = run('rpm -q starburst-presto-server-rpm')
        return package_search.succeeded


def get_presto_version():
    with settings(hide('warnings', 'stdout'), warn_only=True):
        version = run('rpm -q --qf \"%{VERSION}\\n\" ' + constants.BRAND + '-server-rpm')
        # currently we have two rpm names out so we need this retry
        if not version.succeeded:
            version = run('rpm -q --qf \"%{VERSION}\\n\" ' + constants.BRAND)
        version = version.strip()
        _LOGGER.debug('{} rpm version: {}'.format(constants.BRAND.capitalize(), version))

        return version


def check_server_status():
    """
    Checks if server is running for env.host. Retries connecting to server
    until server is up or till RETRY_TIMEOUT is reached

    Parameters:
        client - client that executes the query

    Returns:
        True or False
    """
    if len(get_coordinator_role()) < 1:
        warn('No coordinator defined.  Cannot verify server status.')
    with closing(TrinoClient(get_coordinator_role()[0], env.user)) as client:
        node_id = lookup_string_config('node.id', os.path.join(constants.REMOTE_CONF_DIR, 'node.properties'), env.host)
        try:
            return query_server_for_status(client, node_id)
        except RetryError:
            return False


@retry(stop_max_delay=RETRY_TIMEOUT * 1000, wait_fixed=5000, retry_on_result=lambda result: result is False)
def query_server_for_status(client, node_id):
    try:
        rows = client.run_sql(SYSTEM_RUNTIME_NODES)
        if rows is not None:
            return _is_in_rows(node_id, rows)
    except ConfigurationError as e:
        _LOGGER.warn(e)
    return False


def _is_in_rows(value, rows):
    for row in rows:
        if value in row:
            return True
    return False


def execute_catalog_info_sql(client):
    """
    Returns [[catalog_name], [catalog_2]..] from catalogs system table

    Parameters:
        client - client that executes the query
    """
    return client.run_sql(CATALOG_INFO_SQL)


def execute_external_ip_sql(client, uuid):
    """
    Returns external ip of the host with uuid after parsing the http_uri column
    from nodes system table

    Parameters:
        client - client that executes the query
        uuid - node_id of the node
    """
    return client.run_sql(EXTERNAL_IP_SQL % uuid)


def get_sysnode_info_from(node_info_row, state_transform):
    """
    Returns system node info dict from node info row for a node

    Parameters:
        node_info_row -

    Returns:
        Node info dict in format:
        {'http://node1/statement': [presto-main:0.97-SNAPSHOT, True]}
    """
    output = {}
    for row in node_info_row:
        if row:
            output[row[0]] = [row[1], state_transform(row[2])]

    _LOGGER.info('Node info: %s ', output)
    return output


def get_catalog_info_from(client):
    """
    Returns installed catalogs

    Parameters:
        client - client that executes the query

    Returns:
        comma delimited catalogs eg: tpch, hive, system
    """
    syscatalog = []
    catalog_info = execute_catalog_info_sql(client)
    for conn_info in catalog_info:
        if conn_info:
            syscatalog.append(conn_info[0])
    return ', '.join(syscatalog)


def get_roles_for(host):
    roles = []
    for role in ['coordinator', 'worker']:
        if host in env.roledefs[role]:
            roles.append(role)
    return roles


def print_node_info(node_status, catalog_status):
    """

    Args:
        node_status: list, [node_id, http_uri, node_version, coordinator, state]
        catalog_status: list of catalogies

    Returns:

    """

    print('\tNode URI(http): ' + node_status[1] +
          '\n\t' + constants.BRAND.capitalize() + ' Version: ' + node_status[2] +
          '\n\tNode status:    ' + node_status[4])
    if catalog_status:
        print('\tCatalogs:     ' + catalog_status)
    # for k in node_status:
    #     print('\tNode URI(http): ' + str(k) +
    #           '\n\t' + constants.BRAND.capitalize() + ' Version: ' + str(node_status[k][0]) +
    #           '\n\tNode status:    ' + str(node_status[k][1]))
    #     if catalog_status:
    #         print('\tCatalogs:     ' + catalog_status)


def print_status_header(external_ip, server_status, host):
    print('Server Status:')
    print('\t{}(IP: {}, Roles: {}): {}'.format(host, external_ip, ', '.join(get_roles_for(host)), server_status))


def get_status_from_coordinator():
    """
    get all nodes' status according to query "select * from system.runtime.nodes"

    Returns: list of node status, each element is a list, like
        1b6055c4-7e03-4c27-a809-a8284b3fd0e9,http://10.1.1.1:8080,356,true,active
        the first field is node_id, followed by http_uri, node_version, coordinator, state
    """
    _LOGGER.info("Begin to get status from coordinator")
    with closing(TrinoClient(get_coordinator_role()[0], env.user)) as client:
        try:
            coordinator_status = client.run_sql(SYSTEM_RUNTIME_NODES)
            catalog_status = get_catalog_info_from(client)
        except Exception as e:
            # Just log errors that come from a missing port or anything else; if
            # we can't connect to the coordinator, we just want to print out a
            # minimal status anyway.
            _LOGGER.warn("Failed to get coordinator status: " + e.message)
            coordinator_status = []
            catalog_status = []

        for host in get_host_list():
            try:
                external_ip = socket.gethostbyname(host)
                if get_node_status(coordinator_status, external_ip):
                    is_running = "Running"
                else:
                    is_running = "Not Running"
                error_message = ""
            except socket.gaierror as e:
                external_ip = 'Unknow'
                is_running = "Not Running"
                error_message = e.message

            print_status_header(external_ip, is_running, host)
            if error_message:
                print('\t' + error_message)
            elif not coordinator_status:
                print('\tNo information available: unable to query coordinator')
            elif not is_running:
                print('\tNo information available')
            else:
                node_status = get_node_status(coordinator_status, external_ip)
                if node_status:
                    print_node_info(node_status, catalog_status)
                else:
                    print('\tNo information available: the coordinator has not yet'
                          ' discovered this node')


def get_node_status(coordinator_status, ip):
    """

    Args:
        coordinator_status: list of node status
        ip: node ip

    Returns: node status

    """
    for row in coordinator_status:
        if ip in row[1]:
            return row
    return None


@task
@runs_once
@requires_config(StandaloneConfig)
@with_settings(hide('warnings'))
def status():
    """
    Print the status of presto in the cluster
    """
    get_status_from_coordinator()
