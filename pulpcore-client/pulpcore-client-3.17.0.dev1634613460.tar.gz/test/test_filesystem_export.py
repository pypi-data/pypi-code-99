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

import pulpcore.client.pulpcore
from pulpcore.client.pulpcore.models.filesystem_export import FilesystemExport  # noqa: E501
from pulpcore.client.pulpcore.rest import ApiException

class TestFilesystemExport(unittest.TestCase):
    """FilesystemExport unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test FilesystemExport
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pulpcore.client.pulpcore.models.filesystem_export.FilesystemExport()  # noqa: E501
        if include_optional :
            return FilesystemExport(
                task = '0', 
                publication = '0', 
                repository_version = '0'
            )
        else :
            return FilesystemExport(
        )

    def testFilesystemExport(self):
        """Test FilesystemExport"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
