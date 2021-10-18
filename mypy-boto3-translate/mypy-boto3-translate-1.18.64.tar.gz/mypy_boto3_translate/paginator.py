"""
Type annotations for translate service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_translate/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_translate import TranslateClient
    from mypy_boto3_translate.paginator import (
        ListTerminologiesPaginator,
    )

    client: TranslateClient = boto3.client("translate")

    list_terminologies_paginator: ListTerminologiesPaginator = client.get_paginator("list_terminologies")
    ```
"""
from typing import Generic, Iterator, TypeVar

from botocore.paginate import PageIterator
from botocore.paginate import Paginator as Boto3Paginator

from .type_defs import ListTerminologiesResponseTypeDef, PaginatorConfigTypeDef

__all__ = ("ListTerminologiesPaginator",)


_ItemTypeDef = TypeVar("_ItemTypeDef")


class _PageIterator(Generic[_ItemTypeDef], PageIterator):
    def __iter__(self) -> Iterator[_ItemTypeDef]:
        """
        Proxy method to specify iterator item type.
        """


class ListTerminologiesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.64/reference/services/translate.html#Translate.Paginator.ListTerminologies)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_translate/paginators.html#listterminologiespaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> _PageIterator[ListTerminologiesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.64/reference/services/translate.html#Translate.Paginator.ListTerminologies.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_translate/paginators.html#listterminologiespaginator)
        """
