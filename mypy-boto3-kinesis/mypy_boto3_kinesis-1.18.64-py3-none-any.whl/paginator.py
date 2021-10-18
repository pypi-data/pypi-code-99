"""
Type annotations for kinesis service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesis/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_kinesis import KinesisClient
    from mypy_boto3_kinesis.paginator import (
        DescribeStreamPaginator,
        ListShardsPaginator,
        ListStreamConsumersPaginator,
        ListStreamsPaginator,
    )

    client: KinesisClient = boto3.client("kinesis")

    describe_stream_paginator: DescribeStreamPaginator = client.get_paginator("describe_stream")
    list_shards_paginator: ListShardsPaginator = client.get_paginator("list_shards")
    list_stream_consumers_paginator: ListStreamConsumersPaginator = client.get_paginator("list_stream_consumers")
    list_streams_paginator: ListStreamsPaginator = client.get_paginator("list_streams")
    ```
"""
from datetime import datetime
from typing import Generic, Iterator, TypeVar, Union

from botocore.paginate import PageIterator
from botocore.paginate import Paginator as Boto3Paginator

from .type_defs import (
    DescribeStreamOutputTypeDef,
    ListShardsOutputTypeDef,
    ListStreamConsumersOutputTypeDef,
    ListStreamsOutputTypeDef,
    PaginatorConfigTypeDef,
    ShardFilterTypeDef,
)

__all__ = (
    "DescribeStreamPaginator",
    "ListShardsPaginator",
    "ListStreamConsumersPaginator",
    "ListStreamsPaginator",
)


_ItemTypeDef = TypeVar("_ItemTypeDef")


class _PageIterator(Generic[_ItemTypeDef], PageIterator):
    def __iter__(self) -> Iterator[_ItemTypeDef]:
        """
        Proxy method to specify iterator item type.
        """


class DescribeStreamPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.64/reference/services/kinesis.html#Kinesis.Paginator.DescribeStream)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesis/paginators.html#describestreampaginator)
    """

    def paginate(
        self, *, StreamName: str, PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> _PageIterator[DescribeStreamOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.64/reference/services/kinesis.html#Kinesis.Paginator.DescribeStream.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesis/paginators.html#describestreampaginator)
        """


class ListShardsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.64/reference/services/kinesis.html#Kinesis.Paginator.ListShards)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesis/paginators.html#listshardspaginator)
    """

    def paginate(
        self,
        *,
        StreamName: str = ...,
        ExclusiveStartShardId: str = ...,
        StreamCreationTimestamp: Union[datetime, str] = ...,
        ShardFilter: "ShardFilterTypeDef" = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> _PageIterator[ListShardsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.64/reference/services/kinesis.html#Kinesis.Paginator.ListShards.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesis/paginators.html#listshardspaginator)
        """


class ListStreamConsumersPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.64/reference/services/kinesis.html#Kinesis.Paginator.ListStreamConsumers)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesis/paginators.html#liststreamconsumerspaginator)
    """

    def paginate(
        self,
        *,
        StreamARN: str,
        StreamCreationTimestamp: Union[datetime, str] = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> _PageIterator[ListStreamConsumersOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.64/reference/services/kinesis.html#Kinesis.Paginator.ListStreamConsumers.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesis/paginators.html#liststreamconsumerspaginator)
        """


class ListStreamsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.64/reference/services/kinesis.html#Kinesis.Paginator.ListStreams)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesis/paginators.html#liststreamspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> _PageIterator[ListStreamsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.64/reference/services/kinesis.html#Kinesis.Paginator.ListStreams.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesis/paginators.html#liststreamspaginator)
        """
