# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="insert_or_update_paragraph_tab_stop_online_request.py">
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
import json

from six.moves.urllib.parse import quote
from asposewordscloud import *
from asposewordscloud.models.requests import *
from asposewordscloud.models.responses import *

class InsertOrUpdateParagraphTabStopOnlineRequest(BaseRequestObject):
    """
    Request model for insert_or_update_paragraph_tab_stop_online operation.
    Initializes a new instance.
    :param document The document.
    :param tab_stop_insert_dto TabStopInsert dto.
    :param index Object index.
    :param node_path The path to the node in the document tree.
    :param load_encoding Encoding that will be used to load an HTML (or TXT) document if the encoding is not specified in HTML.
    :param password Password for opening an encrypted document.
    :param dest_file_name Result path of the document after the operation. If this parameter is omitted then result of the operation will be saved as the source document.
    """

    def __init__(self, document, tab_stop_insert_dto, index, node_path=None, load_encoding=None, password=None, dest_file_name=None):
        self.document = document
        self.tab_stop_insert_dto = tab_stop_insert_dto
        self.index = index
        self.node_path = node_path
        self.load_encoding = load_encoding
        self.password = password
        self.dest_file_name = dest_file_name

    def create_http_request(self, api_client):
        # verify the required parameter 'document' is set
        if self.document is None:
            raise ValueError("Missing the required parameter `document` when calling `insert_or_update_paragraph_tab_stop_online`")  # noqa: E501
        # verify the required parameter 'tab_stop_insert_dto' is set
        if self.tab_stop_insert_dto is None:
            raise ValueError("Missing the required parameter `tab_stop_insert_dto` when calling `insert_or_update_paragraph_tab_stop_online`")  # noqa: E501
        # verify the required parameter 'index' is set
        if self.index is None:
            raise ValueError("Missing the required parameter `index` when calling `insert_or_update_paragraph_tab_stop_online`")  # noqa: E501

        path = '/v4.0/words/online/post/{nodePath}/paragraphs/{index}/tabstops'
        path_params = {}
        if self.index is not None:
            path_params['index'] = self.index  # noqa: E501
        else:
            path_params['index'] = ''  # noqa: E501
        if self.node_path is not None:
            path_params['nodePath'] = self.node_path  # noqa: E501
        else:
            path_params['nodePath'] = ''  # noqa: E501

        # path parameters
        collection_formats = {}
        if path_params:
            path_params = api_client.sanitize_for_serialization(path_params)
            path_params = api_client.parameters_to_tuples(path_params, collection_formats)
            for k, v in path_params:
                # specified safe chars, encode everything
                path = path.replace(
                    '{%s}' % k,
                    quote(str(v), safe=api_client.configuration.safe_chars_for_path_param)
                )

        # remove optional path parameters
        path = path.replace('//', '/')

        query_params = []
        if self.load_encoding is not None:
                query_params.append(('loadEncoding', self.load_encoding))  # noqa: E501
        if self.password is not None:
                query_params.append(('password', self.password))  # noqa: E501
        if self.dest_file_name is not None:
                query_params.append(('destFileName', self.dest_file_name))  # noqa: E501

        header_params = {}
        # HTTP header `Content-Type`
        header_params['Content-Type'] = api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        form_params = []
        if self.document is not None:
            form_params.append(['document', self.document, 'file'])  # noqa: E501
        if self.tab_stop_insert_dto is not None:
            form_params.append(['tabStopInsertDto', self.tab_stop_insert_dto.to_json(), 'string'])  # noqa: E501

        body_params = None
        return {
            "method": "PUT",
            "path": path,
            "query_params": query_params,
            "header_params": header_params,
            "form_params": form_params,
            "body": body_params,
            "collection_formats": collection_formats,
            "response_type": 'InsertOrUpdateParagraphTabStopOnlineResponse'  # noqa: E501
        }

    def get_response_type(self):
        return 'InsertOrUpdateParagraphTabStopOnlineResponse'  # noqa: E501

    def deserialize_response(self, api_client, response):
        multipart = self.getparts(response)
        return InsertOrUpdateParagraphTabStopOnlineResponse(
          self.deserialize(json.loads(multipart[0].text), TabStopsResponse, api_client),
          self.deserialize_file(multipart[1].content, multipart[1].headers, api_client))
