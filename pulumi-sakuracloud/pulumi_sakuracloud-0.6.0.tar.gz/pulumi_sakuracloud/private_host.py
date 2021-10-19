# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['PrivateHostArgs', 'PrivateHost']

@pulumi.input_type
class PrivateHostArgs:
    def __init__(__self__, *,
                 class_: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 icon_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 zone: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a PrivateHost resource.
        :param pulumi.Input[str] class_: The class of the PrivateHost. This will be one of [`dynamic`/`ms_windows`]. Default:`dynamic`.
        :param pulumi.Input[str] description: The description of the PrivateHost. The length of this value must be in the range [`1`-`512`].
        :param pulumi.Input[str] icon_id: The icon id to attach to the PrivateHost.
        :param pulumi.Input[str] name: The name of the PrivateHost. The length of this value must be in the range [`1`-`64`].
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: Any tags to assign to the PrivateHost.
        :param pulumi.Input[str] zone: The name of zone that the PrivateHost will be created. (e.g. `is1a`, `tk1a`). Changing this forces a new resource to be created.
        """
        if class_ is not None:
            pulumi.set(__self__, "class_", class_)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if icon_id is not None:
            pulumi.set(__self__, "icon_id", icon_id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if zone is not None:
            pulumi.set(__self__, "zone", zone)

    @property
    @pulumi.getter(name="class")
    def class_(self) -> Optional[pulumi.Input[str]]:
        """
        The class of the PrivateHost. This will be one of [`dynamic`/`ms_windows`]. Default:`dynamic`.
        """
        return pulumi.get(self, "class_")

    @class_.setter
    def class_(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "class_", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the PrivateHost. The length of this value must be in the range [`1`-`512`].
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="iconId")
    def icon_id(self) -> Optional[pulumi.Input[str]]:
        """
        The icon id to attach to the PrivateHost.
        """
        return pulumi.get(self, "icon_id")

    @icon_id.setter
    def icon_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "icon_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the PrivateHost. The length of this value must be in the range [`1`-`64`].
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Any tags to assign to the PrivateHost.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter
    def zone(self) -> Optional[pulumi.Input[str]]:
        """
        The name of zone that the PrivateHost will be created. (e.g. `is1a`, `tk1a`). Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "zone")

    @zone.setter
    def zone(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "zone", value)


@pulumi.input_type
class _PrivateHostState:
    def __init__(__self__, *,
                 assigned_core: Optional[pulumi.Input[int]] = None,
                 assigned_memory: Optional[pulumi.Input[int]] = None,
                 class_: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 hostname: Optional[pulumi.Input[str]] = None,
                 icon_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 zone: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering PrivateHost resources.
        :param pulumi.Input[int] assigned_core: The total number of CPUs assigned to servers on the private host.
        :param pulumi.Input[int] assigned_memory: The total size of memory assigned to servers on the private host.
        :param pulumi.Input[str] class_: The class of the PrivateHost. This will be one of [`dynamic`/`ms_windows`]. Default:`dynamic`.
        :param pulumi.Input[str] description: The description of the PrivateHost. The length of this value must be in the range [`1`-`512`].
        :param pulumi.Input[str] hostname: The hostname of the private host.
        :param pulumi.Input[str] icon_id: The icon id to attach to the PrivateHost.
        :param pulumi.Input[str] name: The name of the PrivateHost. The length of this value must be in the range [`1`-`64`].
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: Any tags to assign to the PrivateHost.
        :param pulumi.Input[str] zone: The name of zone that the PrivateHost will be created. (e.g. `is1a`, `tk1a`). Changing this forces a new resource to be created.
        """
        if assigned_core is not None:
            pulumi.set(__self__, "assigned_core", assigned_core)
        if assigned_memory is not None:
            pulumi.set(__self__, "assigned_memory", assigned_memory)
        if class_ is not None:
            pulumi.set(__self__, "class_", class_)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if hostname is not None:
            pulumi.set(__self__, "hostname", hostname)
        if icon_id is not None:
            pulumi.set(__self__, "icon_id", icon_id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if zone is not None:
            pulumi.set(__self__, "zone", zone)

    @property
    @pulumi.getter(name="assignedCore")
    def assigned_core(self) -> Optional[pulumi.Input[int]]:
        """
        The total number of CPUs assigned to servers on the private host.
        """
        return pulumi.get(self, "assigned_core")

    @assigned_core.setter
    def assigned_core(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "assigned_core", value)

    @property
    @pulumi.getter(name="assignedMemory")
    def assigned_memory(self) -> Optional[pulumi.Input[int]]:
        """
        The total size of memory assigned to servers on the private host.
        """
        return pulumi.get(self, "assigned_memory")

    @assigned_memory.setter
    def assigned_memory(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "assigned_memory", value)

    @property
    @pulumi.getter(name="class")
    def class_(self) -> Optional[pulumi.Input[str]]:
        """
        The class of the PrivateHost. This will be one of [`dynamic`/`ms_windows`]. Default:`dynamic`.
        """
        return pulumi.get(self, "class_")

    @class_.setter
    def class_(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "class_", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the PrivateHost. The length of this value must be in the range [`1`-`512`].
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def hostname(self) -> Optional[pulumi.Input[str]]:
        """
        The hostname of the private host.
        """
        return pulumi.get(self, "hostname")

    @hostname.setter
    def hostname(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "hostname", value)

    @property
    @pulumi.getter(name="iconId")
    def icon_id(self) -> Optional[pulumi.Input[str]]:
        """
        The icon id to attach to the PrivateHost.
        """
        return pulumi.get(self, "icon_id")

    @icon_id.setter
    def icon_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "icon_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the PrivateHost. The length of this value must be in the range [`1`-`64`].
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Any tags to assign to the PrivateHost.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter
    def zone(self) -> Optional[pulumi.Input[str]]:
        """
        The name of zone that the PrivateHost will be created. (e.g. `is1a`, `tk1a`). Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "zone")

    @zone.setter
    def zone(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "zone", value)


class PrivateHost(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 class_: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 icon_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 zone: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages a SakuraCloud Private Host.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_sakuracloud as sakuracloud

        foobar = sakuracloud.PrivateHost("foobar",
            description="description",
            tags=[
                "tag1",
                "tag2",
            ])
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] class_: The class of the PrivateHost. This will be one of [`dynamic`/`ms_windows`]. Default:`dynamic`.
        :param pulumi.Input[str] description: The description of the PrivateHost. The length of this value must be in the range [`1`-`512`].
        :param pulumi.Input[str] icon_id: The icon id to attach to the PrivateHost.
        :param pulumi.Input[str] name: The name of the PrivateHost. The length of this value must be in the range [`1`-`64`].
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: Any tags to assign to the PrivateHost.
        :param pulumi.Input[str] zone: The name of zone that the PrivateHost will be created. (e.g. `is1a`, `tk1a`). Changing this forces a new resource to be created.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[PrivateHostArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a SakuraCloud Private Host.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_sakuracloud as sakuracloud

        foobar = sakuracloud.PrivateHost("foobar",
            description="description",
            tags=[
                "tag1",
                "tag2",
            ])
        ```

        :param str resource_name: The name of the resource.
        :param PrivateHostArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PrivateHostArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 class_: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 icon_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 zone: Optional[pulumi.Input[str]] = None,
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
            __props__ = PrivateHostArgs.__new__(PrivateHostArgs)

            __props__.__dict__["class_"] = class_
            __props__.__dict__["description"] = description
            __props__.__dict__["icon_id"] = icon_id
            __props__.__dict__["name"] = name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["zone"] = zone
            __props__.__dict__["assigned_core"] = None
            __props__.__dict__["assigned_memory"] = None
            __props__.__dict__["hostname"] = None
        super(PrivateHost, __self__).__init__(
            'sakuracloud:index/privateHost:PrivateHost',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            assigned_core: Optional[pulumi.Input[int]] = None,
            assigned_memory: Optional[pulumi.Input[int]] = None,
            class_: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            hostname: Optional[pulumi.Input[str]] = None,
            icon_id: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            zone: Optional[pulumi.Input[str]] = None) -> 'PrivateHost':
        """
        Get an existing PrivateHost resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] assigned_core: The total number of CPUs assigned to servers on the private host.
        :param pulumi.Input[int] assigned_memory: The total size of memory assigned to servers on the private host.
        :param pulumi.Input[str] class_: The class of the PrivateHost. This will be one of [`dynamic`/`ms_windows`]. Default:`dynamic`.
        :param pulumi.Input[str] description: The description of the PrivateHost. The length of this value must be in the range [`1`-`512`].
        :param pulumi.Input[str] hostname: The hostname of the private host.
        :param pulumi.Input[str] icon_id: The icon id to attach to the PrivateHost.
        :param pulumi.Input[str] name: The name of the PrivateHost. The length of this value must be in the range [`1`-`64`].
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: Any tags to assign to the PrivateHost.
        :param pulumi.Input[str] zone: The name of zone that the PrivateHost will be created. (e.g. `is1a`, `tk1a`). Changing this forces a new resource to be created.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _PrivateHostState.__new__(_PrivateHostState)

        __props__.__dict__["assigned_core"] = assigned_core
        __props__.__dict__["assigned_memory"] = assigned_memory
        __props__.__dict__["class_"] = class_
        __props__.__dict__["description"] = description
        __props__.__dict__["hostname"] = hostname
        __props__.__dict__["icon_id"] = icon_id
        __props__.__dict__["name"] = name
        __props__.__dict__["tags"] = tags
        __props__.__dict__["zone"] = zone
        return PrivateHost(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="assignedCore")
    def assigned_core(self) -> pulumi.Output[int]:
        """
        The total number of CPUs assigned to servers on the private host.
        """
        return pulumi.get(self, "assigned_core")

    @property
    @pulumi.getter(name="assignedMemory")
    def assigned_memory(self) -> pulumi.Output[int]:
        """
        The total size of memory assigned to servers on the private host.
        """
        return pulumi.get(self, "assigned_memory")

    @property
    @pulumi.getter(name="class")
    def class_(self) -> pulumi.Output[Optional[str]]:
        """
        The class of the PrivateHost. This will be one of [`dynamic`/`ms_windows`]. Default:`dynamic`.
        """
        return pulumi.get(self, "class_")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of the PrivateHost. The length of this value must be in the range [`1`-`512`].
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def hostname(self) -> pulumi.Output[str]:
        """
        The hostname of the private host.
        """
        return pulumi.get(self, "hostname")

    @property
    @pulumi.getter(name="iconId")
    def icon_id(self) -> pulumi.Output[Optional[str]]:
        """
        The icon id to attach to the PrivateHost.
        """
        return pulumi.get(self, "icon_id")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the PrivateHost. The length of this value must be in the range [`1`-`64`].
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        Any tags to assign to the PrivateHost.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def zone(self) -> pulumi.Output[str]:
        """
        The name of zone that the PrivateHost will be created. (e.g. `is1a`, `tk1a`). Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "zone")

