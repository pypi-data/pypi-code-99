# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import proto  # type: ignore

from grafeas.grafeas_v1.types import provenance as g_provenance


__protobuf__ = proto.module(
    package="grafeas.v1", manifest={"BuildNote", "BuildOccurrence",},
)


class BuildNote(proto.Message):
    r"""Note holding the version of the provider's builder and the
    signature of the provenance message in the build details
    occurrence.

    Attributes:
        builder_version (str):
            Required. Immutable. Version of the builder
            which produced this build.
    """

    builder_version = proto.Field(proto.STRING, number=1,)


class BuildOccurrence(proto.Message):
    r"""Details of a build occurrence.

    Attributes:
        provenance (grafeas.grafeas_v1.types.BuildProvenance):
            Required. The actual provenance for the
            build.
        provenance_bytes (str):
            Serialized JSON representation of the provenance, used in
            generating the build signature in the corresponding build
            note. After verifying the signature, ``provenance_bytes``
            can be unmarshalled and compared to the provenance to
            confirm that it is unchanged. A base64-encoded string
            representation of the provenance bytes is used for the
            signature in order to interoperate with openssl which
            expects this format for signature verification.

            The serialized form is captured both to avoid ambiguity in
            how the provenance is marshalled to json as well to prevent
            incompatibilities with future changes.
    """

    provenance = proto.Field(
        proto.MESSAGE, number=1, message=g_provenance.BuildProvenance,
    )
    provenance_bytes = proto.Field(proto.STRING, number=2,)


__all__ = tuple(sorted(__protobuf__.manifest))
