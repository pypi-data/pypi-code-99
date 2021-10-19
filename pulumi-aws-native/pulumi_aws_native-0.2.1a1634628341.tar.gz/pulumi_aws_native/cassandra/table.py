# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._enums import *
from ._inputs import *

__all__ = ['TableArgs', 'Table']

@pulumi.input_type
class TableArgs:
    def __init__(__self__, *,
                 keyspace_name: pulumi.Input[str],
                 partition_key_columns: pulumi.Input[Sequence[pulumi.Input['TableColumnArgs']]],
                 billing_mode: Optional[pulumi.Input['TableBillingModeArgs']] = None,
                 clustering_key_columns: Optional[pulumi.Input[Sequence[pulumi.Input['TableClusteringKeyColumnArgs']]]] = None,
                 encryption_specification: Optional[pulumi.Input['TableEncryptionSpecificationArgs']] = None,
                 point_in_time_recovery_enabled: Optional[pulumi.Input[bool]] = None,
                 regular_columns: Optional[pulumi.Input[Sequence[pulumi.Input['TableColumnArgs']]]] = None,
                 table_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['TableTagArgs']]]] = None):
        """
        The set of arguments for constructing a Table resource.
        :param pulumi.Input[str] keyspace_name: Name for Cassandra keyspace
        :param pulumi.Input[Sequence[pulumi.Input['TableColumnArgs']]] partition_key_columns: Partition key columns of the table
        :param pulumi.Input[Sequence[pulumi.Input['TableClusteringKeyColumnArgs']]] clustering_key_columns: Clustering key columns of the table
        :param pulumi.Input[bool] point_in_time_recovery_enabled: Indicates whether point in time recovery is enabled (true) or disabled (false) on the table
        :param pulumi.Input[Sequence[pulumi.Input['TableColumnArgs']]] regular_columns: Non-key columns of the table
        :param pulumi.Input[str] table_name: Name for Cassandra table
        :param pulumi.Input[Sequence[pulumi.Input['TableTagArgs']]] tags: An array of key-value pairs to apply to this resource
        """
        pulumi.set(__self__, "keyspace_name", keyspace_name)
        pulumi.set(__self__, "partition_key_columns", partition_key_columns)
        if billing_mode is not None:
            pulumi.set(__self__, "billing_mode", billing_mode)
        if clustering_key_columns is not None:
            pulumi.set(__self__, "clustering_key_columns", clustering_key_columns)
        if encryption_specification is not None:
            pulumi.set(__self__, "encryption_specification", encryption_specification)
        if point_in_time_recovery_enabled is not None:
            pulumi.set(__self__, "point_in_time_recovery_enabled", point_in_time_recovery_enabled)
        if regular_columns is not None:
            pulumi.set(__self__, "regular_columns", regular_columns)
        if table_name is not None:
            pulumi.set(__self__, "table_name", table_name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="keyspaceName")
    def keyspace_name(self) -> pulumi.Input[str]:
        """
        Name for Cassandra keyspace
        """
        return pulumi.get(self, "keyspace_name")

    @keyspace_name.setter
    def keyspace_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "keyspace_name", value)

    @property
    @pulumi.getter(name="partitionKeyColumns")
    def partition_key_columns(self) -> pulumi.Input[Sequence[pulumi.Input['TableColumnArgs']]]:
        """
        Partition key columns of the table
        """
        return pulumi.get(self, "partition_key_columns")

    @partition_key_columns.setter
    def partition_key_columns(self, value: pulumi.Input[Sequence[pulumi.Input['TableColumnArgs']]]):
        pulumi.set(self, "partition_key_columns", value)

    @property
    @pulumi.getter(name="billingMode")
    def billing_mode(self) -> Optional[pulumi.Input['TableBillingModeArgs']]:
        return pulumi.get(self, "billing_mode")

    @billing_mode.setter
    def billing_mode(self, value: Optional[pulumi.Input['TableBillingModeArgs']]):
        pulumi.set(self, "billing_mode", value)

    @property
    @pulumi.getter(name="clusteringKeyColumns")
    def clustering_key_columns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['TableClusteringKeyColumnArgs']]]]:
        """
        Clustering key columns of the table
        """
        return pulumi.get(self, "clustering_key_columns")

    @clustering_key_columns.setter
    def clustering_key_columns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['TableClusteringKeyColumnArgs']]]]):
        pulumi.set(self, "clustering_key_columns", value)

    @property
    @pulumi.getter(name="encryptionSpecification")
    def encryption_specification(self) -> Optional[pulumi.Input['TableEncryptionSpecificationArgs']]:
        return pulumi.get(self, "encryption_specification")

    @encryption_specification.setter
    def encryption_specification(self, value: Optional[pulumi.Input['TableEncryptionSpecificationArgs']]):
        pulumi.set(self, "encryption_specification", value)

    @property
    @pulumi.getter(name="pointInTimeRecoveryEnabled")
    def point_in_time_recovery_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates whether point in time recovery is enabled (true) or disabled (false) on the table
        """
        return pulumi.get(self, "point_in_time_recovery_enabled")

    @point_in_time_recovery_enabled.setter
    def point_in_time_recovery_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "point_in_time_recovery_enabled", value)

    @property
    @pulumi.getter(name="regularColumns")
    def regular_columns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['TableColumnArgs']]]]:
        """
        Non-key columns of the table
        """
        return pulumi.get(self, "regular_columns")

    @regular_columns.setter
    def regular_columns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['TableColumnArgs']]]]):
        pulumi.set(self, "regular_columns", value)

    @property
    @pulumi.getter(name="tableName")
    def table_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name for Cassandra table
        """
        return pulumi.get(self, "table_name")

    @table_name.setter
    def table_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "table_name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['TableTagArgs']]]]:
        """
        An array of key-value pairs to apply to this resource
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['TableTagArgs']]]]):
        pulumi.set(self, "tags", value)


class Table(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 billing_mode: Optional[pulumi.Input[pulumi.InputType['TableBillingModeArgs']]] = None,
                 clustering_key_columns: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TableClusteringKeyColumnArgs']]]]] = None,
                 encryption_specification: Optional[pulumi.Input[pulumi.InputType['TableEncryptionSpecificationArgs']]] = None,
                 keyspace_name: Optional[pulumi.Input[str]] = None,
                 partition_key_columns: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TableColumnArgs']]]]] = None,
                 point_in_time_recovery_enabled: Optional[pulumi.Input[bool]] = None,
                 regular_columns: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TableColumnArgs']]]]] = None,
                 table_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TableTagArgs']]]]] = None,
                 __props__=None):
        """
        Resource schema for AWS::Cassandra::Table

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TableClusteringKeyColumnArgs']]]] clustering_key_columns: Clustering key columns of the table
        :param pulumi.Input[str] keyspace_name: Name for Cassandra keyspace
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TableColumnArgs']]]] partition_key_columns: Partition key columns of the table
        :param pulumi.Input[bool] point_in_time_recovery_enabled: Indicates whether point in time recovery is enabled (true) or disabled (false) on the table
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TableColumnArgs']]]] regular_columns: Non-key columns of the table
        :param pulumi.Input[str] table_name: Name for Cassandra table
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TableTagArgs']]]] tags: An array of key-value pairs to apply to this resource
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: TableArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource schema for AWS::Cassandra::Table

        :param str resource_name: The name of the resource.
        :param TableArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(TableArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 billing_mode: Optional[pulumi.Input[pulumi.InputType['TableBillingModeArgs']]] = None,
                 clustering_key_columns: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TableClusteringKeyColumnArgs']]]]] = None,
                 encryption_specification: Optional[pulumi.Input[pulumi.InputType['TableEncryptionSpecificationArgs']]] = None,
                 keyspace_name: Optional[pulumi.Input[str]] = None,
                 partition_key_columns: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TableColumnArgs']]]]] = None,
                 point_in_time_recovery_enabled: Optional[pulumi.Input[bool]] = None,
                 regular_columns: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TableColumnArgs']]]]] = None,
                 table_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TableTagArgs']]]]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = TableArgs.__new__(TableArgs)

            __props__.__dict__["billing_mode"] = billing_mode
            __props__.__dict__["clustering_key_columns"] = clustering_key_columns
            __props__.__dict__["encryption_specification"] = encryption_specification
            if keyspace_name is None and not opts.urn:
                raise TypeError("Missing required property 'keyspace_name'")
            __props__.__dict__["keyspace_name"] = keyspace_name
            if partition_key_columns is None and not opts.urn:
                raise TypeError("Missing required property 'partition_key_columns'")
            __props__.__dict__["partition_key_columns"] = partition_key_columns
            __props__.__dict__["point_in_time_recovery_enabled"] = point_in_time_recovery_enabled
            __props__.__dict__["regular_columns"] = regular_columns
            __props__.__dict__["table_name"] = table_name
            __props__.__dict__["tags"] = tags
        super(Table, __self__).__init__(
            'aws-native:cassandra:Table',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Table':
        """
        Get an existing Table resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = TableArgs.__new__(TableArgs)

        __props__.__dict__["billing_mode"] = None
        __props__.__dict__["clustering_key_columns"] = None
        __props__.__dict__["encryption_specification"] = None
        __props__.__dict__["keyspace_name"] = None
        __props__.__dict__["partition_key_columns"] = None
        __props__.__dict__["point_in_time_recovery_enabled"] = None
        __props__.__dict__["regular_columns"] = None
        __props__.__dict__["table_name"] = None
        __props__.__dict__["tags"] = None
        return Table(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="billingMode")
    def billing_mode(self) -> pulumi.Output[Optional['outputs.TableBillingMode']]:
        return pulumi.get(self, "billing_mode")

    @property
    @pulumi.getter(name="clusteringKeyColumns")
    def clustering_key_columns(self) -> pulumi.Output[Optional[Sequence['outputs.TableClusteringKeyColumn']]]:
        """
        Clustering key columns of the table
        """
        return pulumi.get(self, "clustering_key_columns")

    @property
    @pulumi.getter(name="encryptionSpecification")
    def encryption_specification(self) -> pulumi.Output[Optional['outputs.TableEncryptionSpecification']]:
        return pulumi.get(self, "encryption_specification")

    @property
    @pulumi.getter(name="keyspaceName")
    def keyspace_name(self) -> pulumi.Output[str]:
        """
        Name for Cassandra keyspace
        """
        return pulumi.get(self, "keyspace_name")

    @property
    @pulumi.getter(name="partitionKeyColumns")
    def partition_key_columns(self) -> pulumi.Output[Sequence['outputs.TableColumn']]:
        """
        Partition key columns of the table
        """
        return pulumi.get(self, "partition_key_columns")

    @property
    @pulumi.getter(name="pointInTimeRecoveryEnabled")
    def point_in_time_recovery_enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        Indicates whether point in time recovery is enabled (true) or disabled (false) on the table
        """
        return pulumi.get(self, "point_in_time_recovery_enabled")

    @property
    @pulumi.getter(name="regularColumns")
    def regular_columns(self) -> pulumi.Output[Optional[Sequence['outputs.TableColumn']]]:
        """
        Non-key columns of the table
        """
        return pulumi.get(self, "regular_columns")

    @property
    @pulumi.getter(name="tableName")
    def table_name(self) -> pulumi.Output[Optional[str]]:
        """
        Name for Cassandra table
        """
        return pulumi.get(self, "table_name")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.TableTag']]]:
        """
        An array of key-value pairs to apply to this resource
        """
        return pulumi.get(self, "tags")

