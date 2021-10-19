# -*- coding: utf-8 -*-
# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""DFDewey Config Template."""

# Postgres Config
PG_HOST = '127.0.0.1'
PG_PORT = 5432
PG_DB_NAME = 'dfdewey'

# Elasticsearch Config
ES_HOST = '127.0.0.1'
ES_PORT = 9200
# ES_URL can be used to specify a RFC-1738 formatted URL
#ES_URL = 'https://user:secret@127.0.0.1:9200/'
