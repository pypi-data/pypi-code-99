#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Licensed to the Apache Software Foundation (ASF) under one
    or more contributor license agreements.  See the NOTICE file
    distributed with this work for additional information
    regarding copyright ownership.  The ASF licenses this file
    to you under the Apache License, Version 2.0 (the
    "License"); you may not use this file except in compliance
    with the License.  You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing,
    software distributed under the License is distributed on an
    "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
    KIND, either express or implied.  See the License for the
    specific language governing permissions and limitations
    under the License.
"""

from pkgutil import extend_path

from .converters import qlm_to_qiskit, qiskit_to_qlm, U, U2, U3, \
        RXX, RZZ, R, MS
from .providers import QLMJob, QPUToBackend, BackendToQPU, \
        QiskitJob, AsyncBackendToQPU, QiskitConnector

# Try to find other QAT packages in other folders
__path__ = extend_path(__path__, __name__)
