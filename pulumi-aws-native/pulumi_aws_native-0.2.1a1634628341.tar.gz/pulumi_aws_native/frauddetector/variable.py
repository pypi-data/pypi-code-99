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

__all__ = ['VariableArgs', 'Variable']

@pulumi.input_type
class VariableArgs:
    def __init__(__self__, *,
                 data_source: pulumi.Input['VariableDataSource'],
                 data_type: pulumi.Input['VariableDataType'],
                 default_value: pulumi.Input[str],
                 name: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['VariableTagArgs']]]] = None,
                 variable_type: Optional[pulumi.Input['VariableType']] = None):
        """
        The set of arguments for constructing a Variable resource.
        :param pulumi.Input['VariableDataSource'] data_source: The source of the data.
        :param pulumi.Input['VariableDataType'] data_type: The data type.
        :param pulumi.Input[str] default_value: The default value for the variable when no value is received.
        :param pulumi.Input[str] name: The name of the variable.
        :param pulumi.Input[str] description: The description.
        :param pulumi.Input[Sequence[pulumi.Input['VariableTagArgs']]] tags: Tags associated with this variable.
        :param pulumi.Input['VariableType'] variable_type: The variable type. For more information see https://docs.aws.amazon.com/frauddetector/latest/ug/create-a-variable.html#variable-types
        """
        pulumi.set(__self__, "data_source", data_source)
        pulumi.set(__self__, "data_type", data_type)
        pulumi.set(__self__, "default_value", default_value)
        pulumi.set(__self__, "name", name)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if variable_type is not None:
            pulumi.set(__self__, "variable_type", variable_type)

    @property
    @pulumi.getter(name="dataSource")
    def data_source(self) -> pulumi.Input['VariableDataSource']:
        """
        The source of the data.
        """
        return pulumi.get(self, "data_source")

    @data_source.setter
    def data_source(self, value: pulumi.Input['VariableDataSource']):
        pulumi.set(self, "data_source", value)

    @property
    @pulumi.getter(name="dataType")
    def data_type(self) -> pulumi.Input['VariableDataType']:
        """
        The data type.
        """
        return pulumi.get(self, "data_type")

    @data_type.setter
    def data_type(self, value: pulumi.Input['VariableDataType']):
        pulumi.set(self, "data_type", value)

    @property
    @pulumi.getter(name="defaultValue")
    def default_value(self) -> pulumi.Input[str]:
        """
        The default value for the variable when no value is received.
        """
        return pulumi.get(self, "default_value")

    @default_value.setter
    def default_value(self, value: pulumi.Input[str]):
        pulumi.set(self, "default_value", value)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        The name of the variable.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['VariableTagArgs']]]]:
        """
        Tags associated with this variable.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['VariableTagArgs']]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="variableType")
    def variable_type(self) -> Optional[pulumi.Input['VariableType']]:
        """
        The variable type. For more information see https://docs.aws.amazon.com/frauddetector/latest/ug/create-a-variable.html#variable-types
        """
        return pulumi.get(self, "variable_type")

    @variable_type.setter
    def variable_type(self, value: Optional[pulumi.Input['VariableType']]):
        pulumi.set(self, "variable_type", value)


class Variable(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 data_source: Optional[pulumi.Input['VariableDataSource']] = None,
                 data_type: Optional[pulumi.Input['VariableDataType']] = None,
                 default_value: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['VariableTagArgs']]]]] = None,
                 variable_type: Optional[pulumi.Input['VariableType']] = None,
                 __props__=None):
        """
        A resource schema for a Variable in Amazon Fraud Detector.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input['VariableDataSource'] data_source: The source of the data.
        :param pulumi.Input['VariableDataType'] data_type: The data type.
        :param pulumi.Input[str] default_value: The default value for the variable when no value is received.
        :param pulumi.Input[str] description: The description.
        :param pulumi.Input[str] name: The name of the variable.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['VariableTagArgs']]]] tags: Tags associated with this variable.
        :param pulumi.Input['VariableType'] variable_type: The variable type. For more information see https://docs.aws.amazon.com/frauddetector/latest/ug/create-a-variable.html#variable-types
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: VariableArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A resource schema for a Variable in Amazon Fraud Detector.

        :param str resource_name: The name of the resource.
        :param VariableArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(VariableArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 data_source: Optional[pulumi.Input['VariableDataSource']] = None,
                 data_type: Optional[pulumi.Input['VariableDataType']] = None,
                 default_value: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['VariableTagArgs']]]]] = None,
                 variable_type: Optional[pulumi.Input['VariableType']] = None,
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
            __props__ = VariableArgs.__new__(VariableArgs)

            if data_source is None and not opts.urn:
                raise TypeError("Missing required property 'data_source'")
            __props__.__dict__["data_source"] = data_source
            if data_type is None and not opts.urn:
                raise TypeError("Missing required property 'data_type'")
            __props__.__dict__["data_type"] = data_type
            if default_value is None and not opts.urn:
                raise TypeError("Missing required property 'default_value'")
            __props__.__dict__["default_value"] = default_value
            __props__.__dict__["description"] = description
            if name is None and not opts.urn:
                raise TypeError("Missing required property 'name'")
            __props__.__dict__["name"] = name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["variable_type"] = variable_type
            __props__.__dict__["arn"] = None
            __props__.__dict__["created_time"] = None
            __props__.__dict__["last_updated_time"] = None
        super(Variable, __self__).__init__(
            'aws-native:frauddetector:Variable',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Variable':
        """
        Get an existing Variable resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = VariableArgs.__new__(VariableArgs)

        __props__.__dict__["arn"] = None
        __props__.__dict__["created_time"] = None
        __props__.__dict__["data_source"] = None
        __props__.__dict__["data_type"] = None
        __props__.__dict__["default_value"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["last_updated_time"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["variable_type"] = None
        return Variable(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        The ARN of the variable.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="createdTime")
    def created_time(self) -> pulumi.Output[str]:
        """
        The time when the variable was created.
        """
        return pulumi.get(self, "created_time")

    @property
    @pulumi.getter(name="dataSource")
    def data_source(self) -> pulumi.Output['VariableDataSource']:
        """
        The source of the data.
        """
        return pulumi.get(self, "data_source")

    @property
    @pulumi.getter(name="dataType")
    def data_type(self) -> pulumi.Output['VariableDataType']:
        """
        The data type.
        """
        return pulumi.get(self, "data_type")

    @property
    @pulumi.getter(name="defaultValue")
    def default_value(self) -> pulumi.Output[str]:
        """
        The default value for the variable when no value is received.
        """
        return pulumi.get(self, "default_value")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="lastUpdatedTime")
    def last_updated_time(self) -> pulumi.Output[str]:
        """
        The time when the variable was last updated.
        """
        return pulumi.get(self, "last_updated_time")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the variable.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.VariableTag']]]:
        """
        Tags associated with this variable.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="variableType")
    def variable_type(self) -> pulumi.Output[Optional['VariableType']]:
        """
        The variable type. For more information see https://docs.aws.amazon.com/frauddetector/latest/ug/create-a-variable.html#variable-types
        """
        return pulumi.get(self, "variable_type")

