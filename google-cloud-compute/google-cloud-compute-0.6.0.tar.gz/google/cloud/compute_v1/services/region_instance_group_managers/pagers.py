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
from typing import (
    Any,
    AsyncIterable,
    Awaitable,
    Callable,
    Iterable,
    Sequence,
    Tuple,
    Optional,
)

from google.cloud.compute_v1.types import compute


class ListPager:
    """A pager for iterating through ``list`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.compute_v1.types.RegionInstanceGroupManagerList` object, and
    provides an ``__iter__`` method to iterate through its
    ``items`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``List`` requests and continue to iterate
    through the ``items`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.compute_v1.types.RegionInstanceGroupManagerList`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., compute.RegionInstanceGroupManagerList],
        request: compute.ListRegionInstanceGroupManagersRequest,
        response: compute.RegionInstanceGroupManagerList,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.compute_v1.types.ListRegionInstanceGroupManagersRequest):
                The initial request object.
            response (google.cloud.compute_v1.types.RegionInstanceGroupManagerList):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = compute.ListRegionInstanceGroupManagersRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterable[compute.RegionInstanceGroupManagerList]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterable[compute.InstanceGroupManager]:
        for page in self.pages:
            yield from page.items

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListErrorsPager:
    """A pager for iterating through ``list_errors`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.compute_v1.types.RegionInstanceGroupManagersListErrorsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``items`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListErrors`` requests and continue to iterate
    through the ``items`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.compute_v1.types.RegionInstanceGroupManagersListErrorsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., compute.RegionInstanceGroupManagersListErrorsResponse],
        request: compute.ListErrorsRegionInstanceGroupManagersRequest,
        response: compute.RegionInstanceGroupManagersListErrorsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.compute_v1.types.ListErrorsRegionInstanceGroupManagersRequest):
                The initial request object.
            response (google.cloud.compute_v1.types.RegionInstanceGroupManagersListErrorsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = compute.ListErrorsRegionInstanceGroupManagersRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterable[compute.RegionInstanceGroupManagersListErrorsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterable[compute.InstanceManagedByIgmError]:
        for page in self.pages:
            yield from page.items

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListManagedInstancesPager:
    """A pager for iterating through ``list_managed_instances`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.compute_v1.types.RegionInstanceGroupManagersListInstancesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``managed_instances`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListManagedInstances`` requests and continue to iterate
    through the ``managed_instances`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.compute_v1.types.RegionInstanceGroupManagersListInstancesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., compute.RegionInstanceGroupManagersListInstancesResponse],
        request: compute.ListManagedInstancesRegionInstanceGroupManagersRequest,
        response: compute.RegionInstanceGroupManagersListInstancesResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.compute_v1.types.ListManagedInstancesRegionInstanceGroupManagersRequest):
                The initial request object.
            response (google.cloud.compute_v1.types.RegionInstanceGroupManagersListInstancesResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = compute.ListManagedInstancesRegionInstanceGroupManagersRequest(
            request
        )
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(
        self,
    ) -> Iterable[compute.RegionInstanceGroupManagersListInstancesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterable[compute.ManagedInstance]:
        for page in self.pages:
            yield from page.managed_instances

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListPerInstanceConfigsPager:
    """A pager for iterating through ``list_per_instance_configs`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.compute_v1.types.RegionInstanceGroupManagersListInstanceConfigsResp` object, and
    provides an ``__iter__`` method to iterate through its
    ``items`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListPerInstanceConfigs`` requests and continue to iterate
    through the ``items`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.compute_v1.types.RegionInstanceGroupManagersListInstanceConfigsResp`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., compute.RegionInstanceGroupManagersListInstanceConfigsResp
        ],
        request: compute.ListPerInstanceConfigsRegionInstanceGroupManagersRequest,
        response: compute.RegionInstanceGroupManagersListInstanceConfigsResp,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.compute_v1.types.ListPerInstanceConfigsRegionInstanceGroupManagersRequest):
                The initial request object.
            response (google.cloud.compute_v1.types.RegionInstanceGroupManagersListInstanceConfigsResp):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = compute.ListPerInstanceConfigsRegionInstanceGroupManagersRequest(
            request
        )
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(
        self,
    ) -> Iterable[compute.RegionInstanceGroupManagersListInstanceConfigsResp]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterable[compute.PerInstanceConfig]:
        for page in self.pages:
            yield from page.items

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)
