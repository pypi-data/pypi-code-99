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

from grafeas.grafeas_v1.types import common


__protobuf__ = proto.module(
    package="grafeas.v1", manifest={"AttestationNote", "AttestationOccurrence",},
)


class AttestationNote(proto.Message):
    r"""Note kind that represents a logical attestation "role" or
    "authority". For example, an organization might have one
    ``Authority`` for "QA" and one for "build". This note is intended to
    act strictly as a grouping mechanism for the attached occurrences
    (Attestations). This grouping mechanism also provides a security
    boundary, since IAM ACLs gate the ability for a principle to attach
    an occurrence to a given note. It also provides a single point of
    lookup to find all attached attestation occurrences, even if they
    don't all live in the same project.

    Attributes:
        hint (grafeas.grafeas_v1.types.AttestationNote.Hint):
            Hint hints at the purpose of the attestation
            authority.
    """

    class Hint(proto.Message):
        r"""This submessage provides human-readable hints about the
        purpose of the authority. Because the name of a note acts as its
        resource reference, it is important to disambiguate the
        canonical name of the Note (which might be a UUID for security
        purposes) from "readable" names more suitable for debug output.
        Note that these hints should not be used to look up authorities
        in security sensitive contexts, such as when looking up
        attestations to verify.

        Attributes:
            human_readable_name (str):
                Required. The human readable name of this
                attestation authority, for example "qa".
        """

        human_readable_name = proto.Field(proto.STRING, number=1,)

    hint = proto.Field(proto.MESSAGE, number=1, message=Hint,)


class AttestationOccurrence(proto.Message):
    r"""Occurrence that represents a single "attestation". The
    authenticity of an attestation can be verified using the
    attached signature. If the verifier trusts the public key of the
    signer, then verifying the signature is sufficient to establish
    trust. In this circumstance, the authority to which this
    attestation is attached is primarily useful for lookup (how to
    find this attestation if you already know the authority and
    artifact to be verified) and intent (for which authority this
    attestation was intended to sign.

    Attributes:
        serialized_payload (bytes):
            Required. The serialized payload that is verified by one or
            more ``signatures``.
        signatures (Sequence[grafeas.grafeas_v1.types.Signature]):
            One or more signatures over ``serialized_payload``. Verifier
            implementations should consider this attestation message
            verified if at least one ``signature`` verifies
            ``serialized_payload``. See ``Signature`` in common.proto
            for more details on signature structure and verification.
    """

    serialized_payload = proto.Field(proto.BYTES, number=1,)
    signatures = proto.RepeatedField(proto.MESSAGE, number=2, message=common.Signature,)


__all__ = tuple(sorted(__protobuf__.manifest))
