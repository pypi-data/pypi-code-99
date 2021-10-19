# coding: utf-8

"""
    Pulp 3 API

    Fetch, Upload, Organize, and Distribute Software Packages  # noqa: E501

    The version of the OpenAPI document: v3
    Contact: pulp-list@redhat.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import pulpcore.client.pulp_ansible
from pulpcore.client.pulp_ansible.models.ansible_ansible_repository import AnsibleAnsibleRepository  # noqa: E501
from pulpcore.client.pulp_ansible.rest import ApiException

class TestAnsibleAnsibleRepository(unittest.TestCase):
    """AnsibleAnsibleRepository unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AnsibleAnsibleRepository
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pulpcore.client.pulp_ansible.models.ansible_ansible_repository.AnsibleAnsibleRepository()  # noqa: E501
        if include_optional :
            return AnsibleAnsibleRepository(
                pulp_labels = None, 
                name = '0', 
                description = '0', 
                retain_repo_versions = 1, 
                remote = '0', 
                last_synced_metadata_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else :
            return AnsibleAnsibleRepository(
                name = '0',
        )

    def testAnsibleAnsibleRepository(self):
        """Test AnsibleAnsibleRepository"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
