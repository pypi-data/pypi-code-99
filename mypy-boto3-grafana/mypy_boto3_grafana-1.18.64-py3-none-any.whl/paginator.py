"""
Type annotations for grafana service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_grafana/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_grafana import ManagedGrafanaClient
    from mypy_boto3_grafana.paginator import (
        ListPermissionsPaginator,
        ListWorkspacesPaginator,
    )

    client: ManagedGrafanaClient = boto3.client("grafana")

    list_permissions_paginator: ListPermissionsPaginator = client.get_paginator("list_permissions")
    list_workspaces_paginator: ListWorkspacesPaginator = client.get_paginator("list_workspaces")
    ```
"""
from typing import Generic, Iterator, TypeVar

from botocore.paginate import PageIterator
from botocore.paginate import Paginator as Boto3Paginator

from .literals import UserTypeType
from .type_defs import (
    ListPermissionsResponseTypeDef,
    ListWorkspacesResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = ("ListPermissionsPaginator", "ListWorkspacesPaginator")


_ItemTypeDef = TypeVar("_ItemTypeDef")


class _PageIterator(Generic[_ItemTypeDef], PageIterator):
    def __iter__(self) -> Iterator[_ItemTypeDef]:
        """
        Proxy method to specify iterator item type.
        """


class ListPermissionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.64/reference/services/grafana.html#ManagedGrafana.Paginator.ListPermissions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_grafana/paginators.html#listpermissionspaginator)
    """

    def paginate(
        self,
        *,
        workspaceId: str,
        groupId: str = ...,
        userId: str = ...,
        userType: UserTypeType = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> _PageIterator[ListPermissionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.64/reference/services/grafana.html#ManagedGrafana.Paginator.ListPermissions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_grafana/paginators.html#listpermissionspaginator)
        """


class ListWorkspacesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.64/reference/services/grafana.html#ManagedGrafana.Paginator.ListWorkspaces)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_grafana/paginators.html#listworkspacespaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> _PageIterator[ListWorkspacesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.64/reference/services/grafana.html#ManagedGrafana.Paginator.ListWorkspaces.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_grafana/paginators.html#listworkspacespaginator)
        """
