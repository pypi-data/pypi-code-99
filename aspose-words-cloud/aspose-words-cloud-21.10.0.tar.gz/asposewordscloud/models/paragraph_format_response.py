# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="paragraph_format_response.py">
#   Copyright (c) 2021 Aspose.Words for Cloud
# </copyright>
# <summary>
#   Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.
# </summary>
# -----------------------------------------------------------------------------------
import pprint
import re  # noqa: F401

import datetime
import six
import json


class ParagraphFormatResponse(object):
    """The REST response with the formatting properties of a paragraph.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'request_id': 'str',
        'paragraph_format': 'ParagraphFormat'
    }

    attribute_map = {
        'request_id': 'RequestId',
        'paragraph_format': 'ParagraphFormat'
    }

    def __init__(self, request_id=None, paragraph_format=None):  # noqa: E501
        """ParagraphFormatResponse - a model defined in Swagger"""  # noqa: E501

        self._request_id = None
        self._paragraph_format = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if paragraph_format is not None:
            self.paragraph_format = paragraph_format

    @property
    def request_id(self):
        """Gets the request_id of this ParagraphFormatResponse.  # noqa: E501

        Gets or sets the request Id.  # noqa: E501

        :return: The request_id of this ParagraphFormatResponse.  # noqa: E501
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this ParagraphFormatResponse.

        Gets or sets the request Id.  # noqa: E501

        :param request_id: The request_id of this ParagraphFormatResponse.  # noqa: E501
        :type: str
        """
        self._request_id = request_id

    @property
    def paragraph_format(self):
        """Gets the paragraph_format of this ParagraphFormatResponse.  # noqa: E501

        Gets or sets the formatting properties of a paragraph.  # noqa: E501

        :return: The paragraph_format of this ParagraphFormatResponse.  # noqa: E501
        :rtype: ParagraphFormat
        """
        return self._paragraph_format

    @paragraph_format.setter
    def paragraph_format(self, paragraph_format):
        """Sets the paragraph_format of this ParagraphFormatResponse.

        Gets or sets the formatting properties of a paragraph.  # noqa: E501

        :param paragraph_format: The paragraph_format of this ParagraphFormatResponse.  # noqa: E501
        :type: ParagraphFormat
        """
        self._paragraph_format = paragraph_format


    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if value is None:
                continue
            if isinstance(value, list):
                result[self.attribute_map[attr]] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[self.attribute_map[attr]] = value.to_dict()
            elif isinstance(value, dict):
                result[self.attribute_map[attr]] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            elif isinstance(value, (datetime.datetime, datetime.date)):
                result[self.attribute_map[attr]] = value.isoformat()
            else:
                result[self.attribute_map[attr]] = value

        return result

    def to_json(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[self.attribute_map[attr]] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[self.attribute_map[attr]] = value.to_dict()
            elif isinstance(value, dict):
                result[self.attribute_map[attr]] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            elif isinstance(value, (datetime.datetime, datetime.date)):
                result[self.attribute_map[attr]] = value.isoformat()
            else:
                result[self.attribute_map[attr]] = value

        return json.dumps(result)

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ParagraphFormatResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other