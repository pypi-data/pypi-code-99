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
import abc
from typing import Awaitable, Callable, Dict, Optional, Sequence, Union
import packaging.version
import pkg_resources

import google.auth  # type: ignore
import google.api_core  # type: ignore
from google.api_core import exceptions as core_exceptions  # type: ignore
from google.api_core import gapic_v1  # type: ignore
from google.api_core import retry as retries  # type: ignore
from google.auth import credentials as ga_credentials  # type: ignore
from google.oauth2 import service_account  # type: ignore

from google.cloud.kms_v1.types import resources
from google.cloud.kms_v1.types import service
from google.iam.v1 import iam_policy_pb2  # type: ignore
from google.iam.v1 import policy_pb2  # type: ignore

try:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
        gapic_version=pkg_resources.get_distribution("google-cloud-kms",).version,
    )
except pkg_resources.DistributionNotFound:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo()

try:
    # google.auth.__version__ was added in 1.26.0
    _GOOGLE_AUTH_VERSION = google.auth.__version__
except AttributeError:
    try:  # try pkg_resources if it is available
        _GOOGLE_AUTH_VERSION = pkg_resources.get_distribution("google-auth").version
    except pkg_resources.DistributionNotFound:  # pragma: NO COVER
        _GOOGLE_AUTH_VERSION = None


class KeyManagementServiceTransport(abc.ABC):
    """Abstract transport class for KeyManagementService."""

    AUTH_SCOPES = (
        "https://www.googleapis.com/auth/cloud-platform",
        "https://www.googleapis.com/auth/cloudkms",
    )

    DEFAULT_HOST: str = "cloudkms.googleapis.com"

    def __init__(
        self,
        *,
        host: str = DEFAULT_HOST,
        credentials: ga_credentials.Credentials = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        **kwargs,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to.
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is mutually exclusive with credentials.
            scopes (Optional[Sequence[str]]): A list of scopes.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.
            always_use_jwt_access (Optional[bool]): Whether self signed JWT should
                be used for service account credentials.
        """
        # Save the hostname. Default to port 443 (HTTPS) if none is specified.
        if ":" not in host:
            host += ":443"
        self._host = host

        scopes_kwargs = self._get_scopes_kwargs(self._host, scopes)

        # Save the scopes.
        self._scopes = scopes

        # If no credentials are provided, then determine the appropriate
        # defaults.
        if credentials and credentials_file:
            raise core_exceptions.DuplicateCredentialArgs(
                "'credentials_file' and 'credentials' are mutually exclusive"
            )

        if credentials_file is not None:
            credentials, _ = google.auth.load_credentials_from_file(
                credentials_file, **scopes_kwargs, quota_project_id=quota_project_id
            )

        elif credentials is None:
            credentials, _ = google.auth.default(
                **scopes_kwargs, quota_project_id=quota_project_id
            )

        # If the credentials are service account credentials, then always try to use self signed JWT.
        if (
            always_use_jwt_access
            and isinstance(credentials, service_account.Credentials)
            and hasattr(service_account.Credentials, "with_always_use_jwt_access")
        ):
            credentials = credentials.with_always_use_jwt_access(True)

        # Save the credentials.
        self._credentials = credentials

    # TODO(busunkim): This method is in the base transport
    # to avoid duplicating code across the transport classes. These functions
    # should be deleted once the minimum required versions of google-auth is increased.

    # TODO: Remove this function once google-auth >= 1.25.0 is required
    @classmethod
    def _get_scopes_kwargs(
        cls, host: str, scopes: Optional[Sequence[str]]
    ) -> Dict[str, Optional[Sequence[str]]]:
        """Returns scopes kwargs to pass to google-auth methods depending on the google-auth version"""

        scopes_kwargs = {}

        if _GOOGLE_AUTH_VERSION and (
            packaging.version.parse(_GOOGLE_AUTH_VERSION)
            >= packaging.version.parse("1.25.0")
        ):
            scopes_kwargs = {"scopes": scopes, "default_scopes": cls.AUTH_SCOPES}
        else:
            scopes_kwargs = {"scopes": scopes or cls.AUTH_SCOPES}

        return scopes_kwargs

    def _prep_wrapped_messages(self, client_info):
        # Precompute the wrapped methods.
        self._wrapped_methods = {
            self.list_key_rings: gapic_v1.method.wrap_method(
                self.list_key_rings,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_crypto_keys: gapic_v1.method.wrap_method(
                self.list_crypto_keys,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_crypto_key_versions: gapic_v1.method.wrap_method(
                self.list_crypto_key_versions,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_import_jobs: gapic_v1.method.wrap_method(
                self.list_import_jobs,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_key_ring: gapic_v1.method.wrap_method(
                self.get_key_ring,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_crypto_key: gapic_v1.method.wrap_method(
                self.get_crypto_key,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_crypto_key_version: gapic_v1.method.wrap_method(
                self.get_crypto_key_version,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_public_key: gapic_v1.method.wrap_method(
                self.get_public_key,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_import_job: gapic_v1.method.wrap_method(
                self.get_import_job,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_key_ring: gapic_v1.method.wrap_method(
                self.create_key_ring,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_crypto_key: gapic_v1.method.wrap_method(
                self.create_crypto_key,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_crypto_key_version: gapic_v1.method.wrap_method(
                self.create_crypto_key_version,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.import_crypto_key_version: gapic_v1.method.wrap_method(
                self.import_crypto_key_version,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_import_job: gapic_v1.method.wrap_method(
                self.create_import_job,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_crypto_key: gapic_v1.method.wrap_method(
                self.update_crypto_key,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_crypto_key_version: gapic_v1.method.wrap_method(
                self.update_crypto_key_version,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_crypto_key_primary_version: gapic_v1.method.wrap_method(
                self.update_crypto_key_primary_version,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.destroy_crypto_key_version: gapic_v1.method.wrap_method(
                self.destroy_crypto_key_version,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.restore_crypto_key_version: gapic_v1.method.wrap_method(
                self.restore_crypto_key_version,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.encrypt: gapic_v1.method.wrap_method(
                self.encrypt,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.decrypt: gapic_v1.method.wrap_method(
                self.decrypt,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.asymmetric_sign: gapic_v1.method.wrap_method(
                self.asymmetric_sign,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.asymmetric_decrypt: gapic_v1.method.wrap_method(
                self.asymmetric_decrypt,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.mac_sign: gapic_v1.method.wrap_method(
                self.mac_sign,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.mac_verify: gapic_v1.method.wrap_method(
                self.mac_verify,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.generate_random_bytes: gapic_v1.method.wrap_method(
                self.generate_random_bytes,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
        }

    def close(self):
        """Closes resources associated with the transport.

       .. warning::
            Only call this method if the transport is NOT shared
            with other clients - this may cause errors in other clients!
        """
        raise NotImplementedError()

    @property
    def list_key_rings(
        self,
    ) -> Callable[
        [service.ListKeyRingsRequest],
        Union[service.ListKeyRingsResponse, Awaitable[service.ListKeyRingsResponse]],
    ]:
        raise NotImplementedError()

    @property
    def list_crypto_keys(
        self,
    ) -> Callable[
        [service.ListCryptoKeysRequest],
        Union[
            service.ListCryptoKeysResponse, Awaitable[service.ListCryptoKeysResponse]
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_crypto_key_versions(
        self,
    ) -> Callable[
        [service.ListCryptoKeyVersionsRequest],
        Union[
            service.ListCryptoKeyVersionsResponse,
            Awaitable[service.ListCryptoKeyVersionsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_import_jobs(
        self,
    ) -> Callable[
        [service.ListImportJobsRequest],
        Union[
            service.ListImportJobsResponse, Awaitable[service.ListImportJobsResponse]
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_key_ring(
        self,
    ) -> Callable[
        [service.GetKeyRingRequest],
        Union[resources.KeyRing, Awaitable[resources.KeyRing]],
    ]:
        raise NotImplementedError()

    @property
    def get_crypto_key(
        self,
    ) -> Callable[
        [service.GetCryptoKeyRequest],
        Union[resources.CryptoKey, Awaitable[resources.CryptoKey]],
    ]:
        raise NotImplementedError()

    @property
    def get_crypto_key_version(
        self,
    ) -> Callable[
        [service.GetCryptoKeyVersionRequest],
        Union[resources.CryptoKeyVersion, Awaitable[resources.CryptoKeyVersion]],
    ]:
        raise NotImplementedError()

    @property
    def get_public_key(
        self,
    ) -> Callable[
        [service.GetPublicKeyRequest],
        Union[resources.PublicKey, Awaitable[resources.PublicKey]],
    ]:
        raise NotImplementedError()

    @property
    def get_import_job(
        self,
    ) -> Callable[
        [service.GetImportJobRequest],
        Union[resources.ImportJob, Awaitable[resources.ImportJob]],
    ]:
        raise NotImplementedError()

    @property
    def create_key_ring(
        self,
    ) -> Callable[
        [service.CreateKeyRingRequest],
        Union[resources.KeyRing, Awaitable[resources.KeyRing]],
    ]:
        raise NotImplementedError()

    @property
    def create_crypto_key(
        self,
    ) -> Callable[
        [service.CreateCryptoKeyRequest],
        Union[resources.CryptoKey, Awaitable[resources.CryptoKey]],
    ]:
        raise NotImplementedError()

    @property
    def create_crypto_key_version(
        self,
    ) -> Callable[
        [service.CreateCryptoKeyVersionRequest],
        Union[resources.CryptoKeyVersion, Awaitable[resources.CryptoKeyVersion]],
    ]:
        raise NotImplementedError()

    @property
    def import_crypto_key_version(
        self,
    ) -> Callable[
        [service.ImportCryptoKeyVersionRequest],
        Union[resources.CryptoKeyVersion, Awaitable[resources.CryptoKeyVersion]],
    ]:
        raise NotImplementedError()

    @property
    def create_import_job(
        self,
    ) -> Callable[
        [service.CreateImportJobRequest],
        Union[resources.ImportJob, Awaitable[resources.ImportJob]],
    ]:
        raise NotImplementedError()

    @property
    def update_crypto_key(
        self,
    ) -> Callable[
        [service.UpdateCryptoKeyRequest],
        Union[resources.CryptoKey, Awaitable[resources.CryptoKey]],
    ]:
        raise NotImplementedError()

    @property
    def update_crypto_key_version(
        self,
    ) -> Callable[
        [service.UpdateCryptoKeyVersionRequest],
        Union[resources.CryptoKeyVersion, Awaitable[resources.CryptoKeyVersion]],
    ]:
        raise NotImplementedError()

    @property
    def update_crypto_key_primary_version(
        self,
    ) -> Callable[
        [service.UpdateCryptoKeyPrimaryVersionRequest],
        Union[resources.CryptoKey, Awaitable[resources.CryptoKey]],
    ]:
        raise NotImplementedError()

    @property
    def destroy_crypto_key_version(
        self,
    ) -> Callable[
        [service.DestroyCryptoKeyVersionRequest],
        Union[resources.CryptoKeyVersion, Awaitable[resources.CryptoKeyVersion]],
    ]:
        raise NotImplementedError()

    @property
    def restore_crypto_key_version(
        self,
    ) -> Callable[
        [service.RestoreCryptoKeyVersionRequest],
        Union[resources.CryptoKeyVersion, Awaitable[resources.CryptoKeyVersion]],
    ]:
        raise NotImplementedError()

    @property
    def encrypt(
        self,
    ) -> Callable[
        [service.EncryptRequest],
        Union[service.EncryptResponse, Awaitable[service.EncryptResponse]],
    ]:
        raise NotImplementedError()

    @property
    def decrypt(
        self,
    ) -> Callable[
        [service.DecryptRequest],
        Union[service.DecryptResponse, Awaitable[service.DecryptResponse]],
    ]:
        raise NotImplementedError()

    @property
    def asymmetric_sign(
        self,
    ) -> Callable[
        [service.AsymmetricSignRequest],
        Union[
            service.AsymmetricSignResponse, Awaitable[service.AsymmetricSignResponse]
        ],
    ]:
        raise NotImplementedError()

    @property
    def asymmetric_decrypt(
        self,
    ) -> Callable[
        [service.AsymmetricDecryptRequest],
        Union[
            service.AsymmetricDecryptResponse,
            Awaitable[service.AsymmetricDecryptResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def mac_sign(
        self,
    ) -> Callable[
        [service.MacSignRequest],
        Union[service.MacSignResponse, Awaitable[service.MacSignResponse]],
    ]:
        raise NotImplementedError()

    @property
    def mac_verify(
        self,
    ) -> Callable[
        [service.MacVerifyRequest],
        Union[service.MacVerifyResponse, Awaitable[service.MacVerifyResponse]],
    ]:
        raise NotImplementedError()

    @property
    def generate_random_bytes(
        self,
    ) -> Callable[
        [service.GenerateRandomBytesRequest],
        Union[
            service.GenerateRandomBytesResponse,
            Awaitable[service.GenerateRandomBytesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def set_iam_policy(
        self,
    ) -> Callable[
        [iam_policy_pb2.SetIamPolicyRequest],
        Union[policy_pb2.Policy, Awaitable[policy_pb2.Policy]],
    ]:
        raise NotImplementedError()

    @property
    def get_iam_policy(
        self,
    ) -> Callable[
        [iam_policy_pb2.GetIamPolicyRequest],
        Union[policy_pb2.Policy, Awaitable[policy_pb2.Policy]],
    ]:
        raise NotImplementedError()

    @property
    def test_iam_permissions(
        self,
    ) -> Callable[
        [iam_policy_pb2.TestIamPermissionsRequest],
        Union[
            iam_policy_pb2.TestIamPermissionsResponse,
            Awaitable[iam_policy_pb2.TestIamPermissionsResponse],
        ],
    ]:
        raise NotImplementedError()


__all__ = ("KeyManagementServiceTransport",)
