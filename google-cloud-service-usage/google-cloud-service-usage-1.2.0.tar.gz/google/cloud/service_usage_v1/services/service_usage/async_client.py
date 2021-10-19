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
from collections import OrderedDict
import functools
import re
from typing import Dict, Sequence, Tuple, Type, Union
import pkg_resources

import google.api_core.client_options as ClientOptions  # type: ignore
from google.api_core import exceptions as core_exceptions  # type: ignore
from google.api_core import gapic_v1  # type: ignore
from google.api_core import retry as retries  # type: ignore
from google.auth import credentials as ga_credentials  # type: ignore
from google.oauth2 import service_account  # type: ignore

from google.api_core import operation  # type: ignore
from google.api_core import operation_async  # type: ignore
from google.cloud.service_usage_v1.services.service_usage import pagers
from google.cloud.service_usage_v1.types import resources
from google.cloud.service_usage_v1.types import serviceusage
from .transports.base import ServiceUsageTransport, DEFAULT_CLIENT_INFO
from .transports.grpc_asyncio import ServiceUsageGrpcAsyncIOTransport
from .client import ServiceUsageClient


class ServiceUsageAsyncClient:
    """Enables services that service consumers want to use on Google Cloud
    Platform, lists the available or enabled services, or disables
    services that service consumers no longer use.

    See `Service Usage
    API <https://cloud.google.com/service-usage/docs/overview>`__
    """

    _client: ServiceUsageClient

    DEFAULT_ENDPOINT = ServiceUsageClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = ServiceUsageClient.DEFAULT_MTLS_ENDPOINT

    common_billing_account_path = staticmethod(
        ServiceUsageClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        ServiceUsageClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(ServiceUsageClient.common_folder_path)
    parse_common_folder_path = staticmethod(ServiceUsageClient.parse_common_folder_path)
    common_organization_path = staticmethod(ServiceUsageClient.common_organization_path)
    parse_common_organization_path = staticmethod(
        ServiceUsageClient.parse_common_organization_path
    )
    common_project_path = staticmethod(ServiceUsageClient.common_project_path)
    parse_common_project_path = staticmethod(
        ServiceUsageClient.parse_common_project_path
    )
    common_location_path = staticmethod(ServiceUsageClient.common_location_path)
    parse_common_location_path = staticmethod(
        ServiceUsageClient.parse_common_location_path
    )

    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            info.

        Args:
            info (dict): The service account private key info.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            ServiceUsageAsyncClient: The constructed client.
        """
        return ServiceUsageClient.from_service_account_info.__func__(ServiceUsageAsyncClient, info, *args, **kwargs)  # type: ignore

    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            file.

        Args:
            filename (str): The path to the service account private key json
                file.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            ServiceUsageAsyncClient: The constructed client.
        """
        return ServiceUsageClient.from_service_account_file.__func__(ServiceUsageAsyncClient, filename, *args, **kwargs)  # type: ignore

    from_service_account_json = from_service_account_file

    @property
    def transport(self) -> ServiceUsageTransport:
        """Returns the transport used by the client instance.

        Returns:
            ServiceUsageTransport: The transport used by the client instance.
        """
        return self._client.transport

    get_transport_class = functools.partial(
        type(ServiceUsageClient).get_transport_class, type(ServiceUsageClient)
    )

    def __init__(
        self,
        *,
        credentials: ga_credentials.Credentials = None,
        transport: Union[str, ServiceUsageTransport] = "grpc_asyncio",
        client_options: ClientOptions = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the service usage client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Union[str, ~.ServiceUsageTransport]): The
                transport to use. If set to None, a transport is chosen
                automatically.
            client_options (ClientOptions): Custom options for the client. It
                won't take effect if a ``transport`` instance is provided.
                (1) The ``api_endpoint`` property can be used to override the
                default endpoint provided by the client. GOOGLE_API_USE_MTLS_ENDPOINT
                environment variable can also be used to override the endpoint:
                "always" (always use the default mTLS endpoint), "never" (always
                use the default regular endpoint) and "auto" (auto switch to the
                default mTLS endpoint if client certificate is present, this is
                the default value). However, the ``api_endpoint`` property takes
                precedence if provided.
                (2) If GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable
                is "true", then the ``client_cert_source`` property can be used
                to provide client certificate for mutual TLS transport. If
                not provided, the default SSL client certificate will be used if
                present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not
                set, no client certificate will be used.

        Raises:
            google.auth.exceptions.MutualTlsChannelError: If mutual TLS transport
                creation failed for any reason.
        """
        self._client = ServiceUsageClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

    async def enable_service(
        self,
        request: serviceusage.EnableServiceRequest = None,
        *,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Enable a service so that it can be used with a
        project.

        Args:
            request (:class:`google.cloud.service_usage_v1.types.EnableServiceRequest`):
                The request object. Request message for the
                `EnableService` method.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.cloud.service_usage_v1.types.EnableServiceResponse` Response message for the EnableService method.
                   This response message is assigned to the response
                   field of the returned Operation when that operation
                   is done.

        """
        # Create or coerce a protobuf request object.
        request = serviceusage.EnableServiceRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.enable_service,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            serviceusage.EnableServiceResponse,
            metadata_type=resources.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def disable_service(
        self,
        request: serviceusage.DisableServiceRequest = None,
        *,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Disable a service so that it can no longer be used with a
        project. This prevents unintended usage that may cause
        unexpected billing charges or security leaks.

        It is not valid to call the disable method on a service that is
        not currently enabled. Callers will receive a
        ``FAILED_PRECONDITION`` status if the target service is not
        currently enabled.

        Args:
            request (:class:`google.cloud.service_usage_v1.types.DisableServiceRequest`):
                The request object. Request message for the
                `DisableService` method.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.cloud.service_usage_v1.types.DisableServiceResponse` Response message for the DisableService method.
                   This response message is assigned to the response
                   field of the returned Operation when that operation
                   is done.

        """
        # Create or coerce a protobuf request object.
        request = serviceusage.DisableServiceRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.disable_service,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            serviceusage.DisableServiceResponse,
            metadata_type=resources.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def get_service(
        self,
        request: serviceusage.GetServiceRequest = None,
        *,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> resources.Service:
        r"""Returns the service configuration and enabled state
        for a given service.

        Args:
            request (:class:`google.cloud.service_usage_v1.types.GetServiceRequest`):
                The request object. Request message for the `GetService`
                method.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.service_usage_v1.types.Service:
                A service that is available for use
                by the consumer.

        """
        # Create or coerce a protobuf request object.
        request = serviceusage.GetServiceRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_service,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def list_services(
        self,
        request: serviceusage.ListServicesRequest = None,
        *,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListServicesAsyncPager:
        r"""List all services available to the specified project, and the
        current state of those services with respect to the project. The
        list includes all public services, all services for which the
        calling user has the ``servicemanagement.services.bind``
        permission, and all services that have already been enabled on
        the project. The list can be filtered to only include services
        in a specific state, for example to only include services
        enabled on the project.

        WARNING: If you need to query enabled services frequently or
        across an organization, you should use `Cloud Asset Inventory
        API <https://cloud.google.com/asset-inventory/docs/apis>`__,
        which provides higher throughput and richer filtering
        capability.

        Args:
            request (:class:`google.cloud.service_usage_v1.types.ListServicesRequest`):
                The request object. Request message for the
                `ListServices` method.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.service_usage_v1.services.service_usage.pagers.ListServicesAsyncPager:
                Response message for the ListServices method.

                Iterating over this object will yield results and
                resolve additional pages automatically.

        """
        # Create or coerce a protobuf request object.
        request = serviceusage.ListServicesRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_services,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListServicesAsyncPager(
            method=rpc, request=request, response=response, metadata=metadata,
        )

        # Done; return the response.
        return response

    async def batch_enable_services(
        self,
        request: serviceusage.BatchEnableServicesRequest = None,
        *,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Enable multiple services on a project. The operation is atomic:
        if enabling any service fails, then the entire batch fails, and
        no state changes occur. To enable a single service, use the
        ``EnableService`` method instead.

        Args:
            request (:class:`google.cloud.service_usage_v1.types.BatchEnableServicesRequest`):
                The request object. Request message for the
                `BatchEnableServices` method.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.cloud.service_usage_v1.types.BatchEnableServicesResponse` Response message for the BatchEnableServices method.
                   This response message is assigned to the response
                   field of the returned Operation when that operation
                   is done.

        """
        # Create or coerce a protobuf request object.
        request = serviceusage.BatchEnableServicesRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.batch_enable_services,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            serviceusage.BatchEnableServicesResponse,
            metadata_type=resources.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def batch_get_services(
        self,
        request: serviceusage.BatchGetServicesRequest = None,
        *,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> serviceusage.BatchGetServicesResponse:
        r"""Returns the service configurations and enabled states
        for a given list of services.

        Args:
            request (:class:`google.cloud.service_usage_v1.types.BatchGetServicesRequest`):
                The request object. Request message for the
                `BatchGetServices` method.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.service_usage_v1.types.BatchGetServicesResponse:
                Response message for the BatchGetServices method.
        """
        # Create or coerce a protobuf request object.
        request = serviceusage.BatchGetServicesRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.batch_get_services,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()


try:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
        gapic_version=pkg_resources.get_distribution(
            "google-cloud-service-usage",
        ).version,
    )
except pkg_resources.DistributionNotFound:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo()


__all__ = ("ServiceUsageAsyncClient",)
