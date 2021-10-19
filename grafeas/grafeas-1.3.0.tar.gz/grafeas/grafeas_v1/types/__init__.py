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
from .attestation import (
    AttestationNote,
    AttestationOccurrence,
)
from .build import (
    BuildNote,
    BuildOccurrence,
)
from .common import (
    RelatedUrl,
    Signature,
    NoteKind,
)
from .cvss import CVSSv3
from .deployment import (
    DeploymentNote,
    DeploymentOccurrence,
)
from .discovery import (
    DiscoveryNote,
    DiscoveryOccurrence,
)
from .grafeas import (
    BatchCreateNotesRequest,
    BatchCreateNotesResponse,
    BatchCreateOccurrencesRequest,
    BatchCreateOccurrencesResponse,
    CreateNoteRequest,
    CreateOccurrenceRequest,
    DeleteNoteRequest,
    DeleteOccurrenceRequest,
    GetNoteRequest,
    GetOccurrenceNoteRequest,
    GetOccurrenceRequest,
    ListNoteOccurrencesRequest,
    ListNoteOccurrencesResponse,
    ListNotesRequest,
    ListNotesResponse,
    ListOccurrencesRequest,
    ListOccurrencesResponse,
    Note,
    Occurrence,
    UpdateNoteRequest,
    UpdateOccurrenceRequest,
)
from .image import (
    Fingerprint,
    ImageNote,
    ImageOccurrence,
    Layer,
)
from .package import (
    Distribution,
    Location,
    PackageNote,
    PackageOccurrence,
    Version,
    Architecture,
)
from .provenance import (
    AliasContext,
    Artifact,
    BuildProvenance,
    CloudRepoSourceContext,
    Command,
    FileHashes,
    GerritSourceContext,
    GitSourceContext,
    Hash,
    ProjectRepoId,
    RepoId,
    Source,
    SourceContext,
)
from .upgrade import (
    UpgradeDistribution,
    UpgradeNote,
    UpgradeOccurrence,
    WindowsUpdate,
)
from .vulnerability import (
    VulnerabilityNote,
    VulnerabilityOccurrence,
    Severity,
)

__all__ = (
    "AttestationNote",
    "AttestationOccurrence",
    "BuildNote",
    "BuildOccurrence",
    "RelatedUrl",
    "Signature",
    "NoteKind",
    "CVSSv3",
    "DeploymentNote",
    "DeploymentOccurrence",
    "DiscoveryNote",
    "DiscoveryOccurrence",
    "BatchCreateNotesRequest",
    "BatchCreateNotesResponse",
    "BatchCreateOccurrencesRequest",
    "BatchCreateOccurrencesResponse",
    "CreateNoteRequest",
    "CreateOccurrenceRequest",
    "DeleteNoteRequest",
    "DeleteOccurrenceRequest",
    "GetNoteRequest",
    "GetOccurrenceNoteRequest",
    "GetOccurrenceRequest",
    "ListNoteOccurrencesRequest",
    "ListNoteOccurrencesResponse",
    "ListNotesRequest",
    "ListNotesResponse",
    "ListOccurrencesRequest",
    "ListOccurrencesResponse",
    "Note",
    "Occurrence",
    "UpdateNoteRequest",
    "UpdateOccurrenceRequest",
    "Fingerprint",
    "ImageNote",
    "ImageOccurrence",
    "Layer",
    "Distribution",
    "Location",
    "PackageNote",
    "PackageOccurrence",
    "Version",
    "Architecture",
    "AliasContext",
    "Artifact",
    "BuildProvenance",
    "CloudRepoSourceContext",
    "Command",
    "FileHashes",
    "GerritSourceContext",
    "GitSourceContext",
    "Hash",
    "ProjectRepoId",
    "RepoId",
    "Source",
    "SourceContext",
    "UpgradeDistribution",
    "UpgradeNote",
    "UpgradeOccurrence",
    "WindowsUpdate",
    "VulnerabilityNote",
    "VulnerabilityOccurrence",
    "Severity",
)
