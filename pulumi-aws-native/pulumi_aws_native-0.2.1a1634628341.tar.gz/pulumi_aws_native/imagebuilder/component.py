# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from ._enums import *

__all__ = ['ComponentArgs', 'Component']

@pulumi.input_type
class ComponentArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str],
                 platform: pulumi.Input['ComponentPlatform'],
                 version: pulumi.Input[str],
                 change_description: Optional[pulumi.Input[str]] = None,
                 data: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 kms_key_id: Optional[pulumi.Input[str]] = None,
                 supported_os_versions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[Any] = None,
                 uri: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Component resource.
        :param pulumi.Input[str] name: The name of the component.
        :param pulumi.Input['ComponentPlatform'] platform: The platform of the component.
        :param pulumi.Input[str] version: The version of the component.
        :param pulumi.Input[str] change_description: The change description of the component.
        :param pulumi.Input[str] data: The data of the component.
        :param pulumi.Input[str] description: The description of the component.
        :param pulumi.Input[str] kms_key_id: The KMS key identifier used to encrypt the component.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] supported_os_versions: The operating system (OS) version supported by the component.
        :param Any tags: The tags associated with the component.
        :param pulumi.Input[str] uri: The uri of the component.
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "platform", platform)
        pulumi.set(__self__, "version", version)
        if change_description is not None:
            pulumi.set(__self__, "change_description", change_description)
        if data is not None:
            pulumi.set(__self__, "data", data)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if kms_key_id is not None:
            pulumi.set(__self__, "kms_key_id", kms_key_id)
        if supported_os_versions is not None:
            pulumi.set(__self__, "supported_os_versions", supported_os_versions)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if uri is not None:
            pulumi.set(__self__, "uri", uri)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        The name of the component.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def platform(self) -> pulumi.Input['ComponentPlatform']:
        """
        The platform of the component.
        """
        return pulumi.get(self, "platform")

    @platform.setter
    def platform(self, value: pulumi.Input['ComponentPlatform']):
        pulumi.set(self, "platform", value)

    @property
    @pulumi.getter
    def version(self) -> pulumi.Input[str]:
        """
        The version of the component.
        """
        return pulumi.get(self, "version")

    @version.setter
    def version(self, value: pulumi.Input[str]):
        pulumi.set(self, "version", value)

    @property
    @pulumi.getter(name="changeDescription")
    def change_description(self) -> Optional[pulumi.Input[str]]:
        """
        The change description of the component.
        """
        return pulumi.get(self, "change_description")

    @change_description.setter
    def change_description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "change_description", value)

    @property
    @pulumi.getter
    def data(self) -> Optional[pulumi.Input[str]]:
        """
        The data of the component.
        """
        return pulumi.get(self, "data")

    @data.setter
    def data(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "data", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the component.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[str]]:
        """
        The KMS key identifier used to encrypt the component.
        """
        return pulumi.get(self, "kms_key_id")

    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kms_key_id", value)

    @property
    @pulumi.getter(name="supportedOsVersions")
    def supported_os_versions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The operating system (OS) version supported by the component.
        """
        return pulumi.get(self, "supported_os_versions")

    @supported_os_versions.setter
    def supported_os_versions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "supported_os_versions", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[Any]:
        """
        The tags associated with the component.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[Any]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter
    def uri(self) -> Optional[pulumi.Input[str]]:
        """
        The uri of the component.
        """
        return pulumi.get(self, "uri")

    @uri.setter
    def uri(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "uri", value)


class Component(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 change_description: Optional[pulumi.Input[str]] = None,
                 data: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 kms_key_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 platform: Optional[pulumi.Input['ComponentPlatform']] = None,
                 supported_os_versions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[Any] = None,
                 uri: Optional[pulumi.Input[str]] = None,
                 version: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Resource schema for AWS::ImageBuilder::Component

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] change_description: The change description of the component.
        :param pulumi.Input[str] data: The data of the component.
        :param pulumi.Input[str] description: The description of the component.
        :param pulumi.Input[str] kms_key_id: The KMS key identifier used to encrypt the component.
        :param pulumi.Input[str] name: The name of the component.
        :param pulumi.Input['ComponentPlatform'] platform: The platform of the component.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] supported_os_versions: The operating system (OS) version supported by the component.
        :param Any tags: The tags associated with the component.
        :param pulumi.Input[str] uri: The uri of the component.
        :param pulumi.Input[str] version: The version of the component.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ComponentArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource schema for AWS::ImageBuilder::Component

        :param str resource_name: The name of the resource.
        :param ComponentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ComponentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 change_description: Optional[pulumi.Input[str]] = None,
                 data: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 kms_key_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 platform: Optional[pulumi.Input['ComponentPlatform']] = None,
                 supported_os_versions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[Any] = None,
                 uri: Optional[pulumi.Input[str]] = None,
                 version: Optional[pulumi.Input[str]] = None,
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
            __props__ = ComponentArgs.__new__(ComponentArgs)

            __props__.__dict__["change_description"] = change_description
            __props__.__dict__["data"] = data
            __props__.__dict__["description"] = description
            __props__.__dict__["kms_key_id"] = kms_key_id
            if name is None and not opts.urn:
                raise TypeError("Missing required property 'name'")
            __props__.__dict__["name"] = name
            if platform is None and not opts.urn:
                raise TypeError("Missing required property 'platform'")
            __props__.__dict__["platform"] = platform
            __props__.__dict__["supported_os_versions"] = supported_os_versions
            __props__.__dict__["tags"] = tags
            __props__.__dict__["uri"] = uri
            if version is None and not opts.urn:
                raise TypeError("Missing required property 'version'")
            __props__.__dict__["version"] = version
            __props__.__dict__["arn"] = None
            __props__.__dict__["encrypted"] = None
            __props__.__dict__["type"] = None
        super(Component, __self__).__init__(
            'aws-native:imagebuilder:Component',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Component':
        """
        Get an existing Component resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ComponentArgs.__new__(ComponentArgs)

        __props__.__dict__["arn"] = None
        __props__.__dict__["change_description"] = None
        __props__.__dict__["data"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["encrypted"] = None
        __props__.__dict__["kms_key_id"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["platform"] = None
        __props__.__dict__["supported_os_versions"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["uri"] = None
        __props__.__dict__["version"] = None
        return Component(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        The Amazon Resource Name (ARN) of the component.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="changeDescription")
    def change_description(self) -> pulumi.Output[Optional[str]]:
        """
        The change description of the component.
        """
        return pulumi.get(self, "change_description")

    @property
    @pulumi.getter
    def data(self) -> pulumi.Output[Optional[str]]:
        """
        The data of the component.
        """
        return pulumi.get(self, "data")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of the component.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def encrypted(self) -> pulumi.Output[bool]:
        """
        The encryption status of the component.
        """
        return pulumi.get(self, "encrypted")

    @property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> pulumi.Output[Optional[str]]:
        """
        The KMS key identifier used to encrypt the component.
        """
        return pulumi.get(self, "kms_key_id")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the component.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def platform(self) -> pulumi.Output['ComponentPlatform']:
        """
        The platform of the component.
        """
        return pulumi.get(self, "platform")

    @property
    @pulumi.getter(name="supportedOsVersions")
    def supported_os_versions(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        The operating system (OS) version supported by the component.
        """
        return pulumi.get(self, "supported_os_versions")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Any]]:
        """
        The tags associated with the component.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output['ComponentType']:
        """
        The type of the component denotes whether the component is used to build the image or only to test it. 
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def uri(self) -> pulumi.Output[Optional[str]]:
        """
        The uri of the component.
        """
        return pulumi.get(self, "uri")

    @property
    @pulumi.getter
    def version(self) -> pulumi.Output[str]:
        """
        The version of the component.
        """
        return pulumi.get(self, "version")

