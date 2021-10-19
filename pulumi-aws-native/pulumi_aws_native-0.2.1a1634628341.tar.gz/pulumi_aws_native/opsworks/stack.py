# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

__all__ = ['StackArgs', 'Stack']

@pulumi.input_type
class StackArgs:
    def __init__(__self__, *,
                 default_instance_profile_arn: pulumi.Input[str],
                 name: pulumi.Input[str],
                 service_role_arn: pulumi.Input[str],
                 agent_version: Optional[pulumi.Input[str]] = None,
                 attributes: Optional[Any] = None,
                 chef_configuration: Optional[pulumi.Input['StackChefConfigurationArgs']] = None,
                 clone_app_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 clone_permissions: Optional[pulumi.Input[bool]] = None,
                 configuration_manager: Optional[pulumi.Input['StackConfigurationManagerArgs']] = None,
                 custom_cookbooks_source: Optional[pulumi.Input['StackSourceArgs']] = None,
                 custom_json: Optional[Any] = None,
                 default_availability_zone: Optional[pulumi.Input[str]] = None,
                 default_os: Optional[pulumi.Input[str]] = None,
                 default_root_device_type: Optional[pulumi.Input[str]] = None,
                 default_ssh_key_name: Optional[pulumi.Input[str]] = None,
                 default_subnet_id: Optional[pulumi.Input[str]] = None,
                 ecs_cluster_arn: Optional[pulumi.Input[str]] = None,
                 elastic_ips: Optional[pulumi.Input[Sequence[pulumi.Input['StackElasticIpArgs']]]] = None,
                 hostname_theme: Optional[pulumi.Input[str]] = None,
                 rds_db_instances: Optional[pulumi.Input[Sequence[pulumi.Input['StackRdsDbInstanceArgs']]]] = None,
                 source_stack_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['StackTagArgs']]]] = None,
                 use_custom_cookbooks: Optional[pulumi.Input[bool]] = None,
                 use_opsworks_security_groups: Optional[pulumi.Input[bool]] = None,
                 vpc_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Stack resource.
        """
        pulumi.set(__self__, "default_instance_profile_arn", default_instance_profile_arn)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "service_role_arn", service_role_arn)
        if agent_version is not None:
            pulumi.set(__self__, "agent_version", agent_version)
        if attributes is not None:
            pulumi.set(__self__, "attributes", attributes)
        if chef_configuration is not None:
            pulumi.set(__self__, "chef_configuration", chef_configuration)
        if clone_app_ids is not None:
            pulumi.set(__self__, "clone_app_ids", clone_app_ids)
        if clone_permissions is not None:
            pulumi.set(__self__, "clone_permissions", clone_permissions)
        if configuration_manager is not None:
            pulumi.set(__self__, "configuration_manager", configuration_manager)
        if custom_cookbooks_source is not None:
            pulumi.set(__self__, "custom_cookbooks_source", custom_cookbooks_source)
        if custom_json is not None:
            pulumi.set(__self__, "custom_json", custom_json)
        if default_availability_zone is not None:
            pulumi.set(__self__, "default_availability_zone", default_availability_zone)
        if default_os is not None:
            pulumi.set(__self__, "default_os", default_os)
        if default_root_device_type is not None:
            pulumi.set(__self__, "default_root_device_type", default_root_device_type)
        if default_ssh_key_name is not None:
            pulumi.set(__self__, "default_ssh_key_name", default_ssh_key_name)
        if default_subnet_id is not None:
            pulumi.set(__self__, "default_subnet_id", default_subnet_id)
        if ecs_cluster_arn is not None:
            pulumi.set(__self__, "ecs_cluster_arn", ecs_cluster_arn)
        if elastic_ips is not None:
            pulumi.set(__self__, "elastic_ips", elastic_ips)
        if hostname_theme is not None:
            pulumi.set(__self__, "hostname_theme", hostname_theme)
        if rds_db_instances is not None:
            pulumi.set(__self__, "rds_db_instances", rds_db_instances)
        if source_stack_id is not None:
            pulumi.set(__self__, "source_stack_id", source_stack_id)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if use_custom_cookbooks is not None:
            pulumi.set(__self__, "use_custom_cookbooks", use_custom_cookbooks)
        if use_opsworks_security_groups is not None:
            pulumi.set(__self__, "use_opsworks_security_groups", use_opsworks_security_groups)
        if vpc_id is not None:
            pulumi.set(__self__, "vpc_id", vpc_id)

    @property
    @pulumi.getter(name="defaultInstanceProfileArn")
    def default_instance_profile_arn(self) -> pulumi.Input[str]:
        return pulumi.get(self, "default_instance_profile_arn")

    @default_instance_profile_arn.setter
    def default_instance_profile_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "default_instance_profile_arn", value)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="serviceRoleArn")
    def service_role_arn(self) -> pulumi.Input[str]:
        return pulumi.get(self, "service_role_arn")

    @service_role_arn.setter
    def service_role_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "service_role_arn", value)

    @property
    @pulumi.getter(name="agentVersion")
    def agent_version(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "agent_version")

    @agent_version.setter
    def agent_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "agent_version", value)

    @property
    @pulumi.getter
    def attributes(self) -> Optional[Any]:
        return pulumi.get(self, "attributes")

    @attributes.setter
    def attributes(self, value: Optional[Any]):
        pulumi.set(self, "attributes", value)

    @property
    @pulumi.getter(name="chefConfiguration")
    def chef_configuration(self) -> Optional[pulumi.Input['StackChefConfigurationArgs']]:
        return pulumi.get(self, "chef_configuration")

    @chef_configuration.setter
    def chef_configuration(self, value: Optional[pulumi.Input['StackChefConfigurationArgs']]):
        pulumi.set(self, "chef_configuration", value)

    @property
    @pulumi.getter(name="cloneAppIds")
    def clone_app_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "clone_app_ids")

    @clone_app_ids.setter
    def clone_app_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "clone_app_ids", value)

    @property
    @pulumi.getter(name="clonePermissions")
    def clone_permissions(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "clone_permissions")

    @clone_permissions.setter
    def clone_permissions(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "clone_permissions", value)

    @property
    @pulumi.getter(name="configurationManager")
    def configuration_manager(self) -> Optional[pulumi.Input['StackConfigurationManagerArgs']]:
        return pulumi.get(self, "configuration_manager")

    @configuration_manager.setter
    def configuration_manager(self, value: Optional[pulumi.Input['StackConfigurationManagerArgs']]):
        pulumi.set(self, "configuration_manager", value)

    @property
    @pulumi.getter(name="customCookbooksSource")
    def custom_cookbooks_source(self) -> Optional[pulumi.Input['StackSourceArgs']]:
        return pulumi.get(self, "custom_cookbooks_source")

    @custom_cookbooks_source.setter
    def custom_cookbooks_source(self, value: Optional[pulumi.Input['StackSourceArgs']]):
        pulumi.set(self, "custom_cookbooks_source", value)

    @property
    @pulumi.getter(name="customJson")
    def custom_json(self) -> Optional[Any]:
        return pulumi.get(self, "custom_json")

    @custom_json.setter
    def custom_json(self, value: Optional[Any]):
        pulumi.set(self, "custom_json", value)

    @property
    @pulumi.getter(name="defaultAvailabilityZone")
    def default_availability_zone(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "default_availability_zone")

    @default_availability_zone.setter
    def default_availability_zone(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "default_availability_zone", value)

    @property
    @pulumi.getter(name="defaultOs")
    def default_os(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "default_os")

    @default_os.setter
    def default_os(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "default_os", value)

    @property
    @pulumi.getter(name="defaultRootDeviceType")
    def default_root_device_type(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "default_root_device_type")

    @default_root_device_type.setter
    def default_root_device_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "default_root_device_type", value)

    @property
    @pulumi.getter(name="defaultSshKeyName")
    def default_ssh_key_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "default_ssh_key_name")

    @default_ssh_key_name.setter
    def default_ssh_key_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "default_ssh_key_name", value)

    @property
    @pulumi.getter(name="defaultSubnetId")
    def default_subnet_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "default_subnet_id")

    @default_subnet_id.setter
    def default_subnet_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "default_subnet_id", value)

    @property
    @pulumi.getter(name="ecsClusterArn")
    def ecs_cluster_arn(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "ecs_cluster_arn")

    @ecs_cluster_arn.setter
    def ecs_cluster_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ecs_cluster_arn", value)

    @property
    @pulumi.getter(name="elasticIps")
    def elastic_ips(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['StackElasticIpArgs']]]]:
        return pulumi.get(self, "elastic_ips")

    @elastic_ips.setter
    def elastic_ips(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['StackElasticIpArgs']]]]):
        pulumi.set(self, "elastic_ips", value)

    @property
    @pulumi.getter(name="hostnameTheme")
    def hostname_theme(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "hostname_theme")

    @hostname_theme.setter
    def hostname_theme(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "hostname_theme", value)

    @property
    @pulumi.getter(name="rdsDbInstances")
    def rds_db_instances(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['StackRdsDbInstanceArgs']]]]:
        return pulumi.get(self, "rds_db_instances")

    @rds_db_instances.setter
    def rds_db_instances(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['StackRdsDbInstanceArgs']]]]):
        pulumi.set(self, "rds_db_instances", value)

    @property
    @pulumi.getter(name="sourceStackId")
    def source_stack_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "source_stack_id")

    @source_stack_id.setter
    def source_stack_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source_stack_id", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['StackTagArgs']]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['StackTagArgs']]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="useCustomCookbooks")
    def use_custom_cookbooks(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "use_custom_cookbooks")

    @use_custom_cookbooks.setter
    def use_custom_cookbooks(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "use_custom_cookbooks", value)

    @property
    @pulumi.getter(name="useOpsworksSecurityGroups")
    def use_opsworks_security_groups(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "use_opsworks_security_groups")

    @use_opsworks_security_groups.setter
    def use_opsworks_security_groups(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "use_opsworks_security_groups", value)

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "vpc_id")

    @vpc_id.setter
    def vpc_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vpc_id", value)


warnings.warn("""Stack is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class Stack(pulumi.CustomResource):
    warnings.warn("""Stack is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 agent_version: Optional[pulumi.Input[str]] = None,
                 attributes: Optional[Any] = None,
                 chef_configuration: Optional[pulumi.Input[pulumi.InputType['StackChefConfigurationArgs']]] = None,
                 clone_app_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 clone_permissions: Optional[pulumi.Input[bool]] = None,
                 configuration_manager: Optional[pulumi.Input[pulumi.InputType['StackConfigurationManagerArgs']]] = None,
                 custom_cookbooks_source: Optional[pulumi.Input[pulumi.InputType['StackSourceArgs']]] = None,
                 custom_json: Optional[Any] = None,
                 default_availability_zone: Optional[pulumi.Input[str]] = None,
                 default_instance_profile_arn: Optional[pulumi.Input[str]] = None,
                 default_os: Optional[pulumi.Input[str]] = None,
                 default_root_device_type: Optional[pulumi.Input[str]] = None,
                 default_ssh_key_name: Optional[pulumi.Input[str]] = None,
                 default_subnet_id: Optional[pulumi.Input[str]] = None,
                 ecs_cluster_arn: Optional[pulumi.Input[str]] = None,
                 elastic_ips: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['StackElasticIpArgs']]]]] = None,
                 hostname_theme: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 rds_db_instances: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['StackRdsDbInstanceArgs']]]]] = None,
                 service_role_arn: Optional[pulumi.Input[str]] = None,
                 source_stack_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['StackTagArgs']]]]] = None,
                 use_custom_cookbooks: Optional[pulumi.Input[bool]] = None,
                 use_opsworks_security_groups: Optional[pulumi.Input[bool]] = None,
                 vpc_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::OpsWorks::Stack

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: StackArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::OpsWorks::Stack

        :param str resource_name: The name of the resource.
        :param StackArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(StackArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 agent_version: Optional[pulumi.Input[str]] = None,
                 attributes: Optional[Any] = None,
                 chef_configuration: Optional[pulumi.Input[pulumi.InputType['StackChefConfigurationArgs']]] = None,
                 clone_app_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 clone_permissions: Optional[pulumi.Input[bool]] = None,
                 configuration_manager: Optional[pulumi.Input[pulumi.InputType['StackConfigurationManagerArgs']]] = None,
                 custom_cookbooks_source: Optional[pulumi.Input[pulumi.InputType['StackSourceArgs']]] = None,
                 custom_json: Optional[Any] = None,
                 default_availability_zone: Optional[pulumi.Input[str]] = None,
                 default_instance_profile_arn: Optional[pulumi.Input[str]] = None,
                 default_os: Optional[pulumi.Input[str]] = None,
                 default_root_device_type: Optional[pulumi.Input[str]] = None,
                 default_ssh_key_name: Optional[pulumi.Input[str]] = None,
                 default_subnet_id: Optional[pulumi.Input[str]] = None,
                 ecs_cluster_arn: Optional[pulumi.Input[str]] = None,
                 elastic_ips: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['StackElasticIpArgs']]]]] = None,
                 hostname_theme: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 rds_db_instances: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['StackRdsDbInstanceArgs']]]]] = None,
                 service_role_arn: Optional[pulumi.Input[str]] = None,
                 source_stack_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['StackTagArgs']]]]] = None,
                 use_custom_cookbooks: Optional[pulumi.Input[bool]] = None,
                 use_opsworks_security_groups: Optional[pulumi.Input[bool]] = None,
                 vpc_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        pulumi.log.warn("""Stack is deprecated: Stack is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = StackArgs.__new__(StackArgs)

            __props__.__dict__["agent_version"] = agent_version
            __props__.__dict__["attributes"] = attributes
            __props__.__dict__["chef_configuration"] = chef_configuration
            __props__.__dict__["clone_app_ids"] = clone_app_ids
            __props__.__dict__["clone_permissions"] = clone_permissions
            __props__.__dict__["configuration_manager"] = configuration_manager
            __props__.__dict__["custom_cookbooks_source"] = custom_cookbooks_source
            __props__.__dict__["custom_json"] = custom_json
            __props__.__dict__["default_availability_zone"] = default_availability_zone
            if default_instance_profile_arn is None and not opts.urn:
                raise TypeError("Missing required property 'default_instance_profile_arn'")
            __props__.__dict__["default_instance_profile_arn"] = default_instance_profile_arn
            __props__.__dict__["default_os"] = default_os
            __props__.__dict__["default_root_device_type"] = default_root_device_type
            __props__.__dict__["default_ssh_key_name"] = default_ssh_key_name
            __props__.__dict__["default_subnet_id"] = default_subnet_id
            __props__.__dict__["ecs_cluster_arn"] = ecs_cluster_arn
            __props__.__dict__["elastic_ips"] = elastic_ips
            __props__.__dict__["hostname_theme"] = hostname_theme
            if name is None and not opts.urn:
                raise TypeError("Missing required property 'name'")
            __props__.__dict__["name"] = name
            __props__.__dict__["rds_db_instances"] = rds_db_instances
            if service_role_arn is None and not opts.urn:
                raise TypeError("Missing required property 'service_role_arn'")
            __props__.__dict__["service_role_arn"] = service_role_arn
            __props__.__dict__["source_stack_id"] = source_stack_id
            __props__.__dict__["tags"] = tags
            __props__.__dict__["use_custom_cookbooks"] = use_custom_cookbooks
            __props__.__dict__["use_opsworks_security_groups"] = use_opsworks_security_groups
            __props__.__dict__["vpc_id"] = vpc_id
        super(Stack, __self__).__init__(
            'aws-native:opsworks:Stack',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Stack':
        """
        Get an existing Stack resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = StackArgs.__new__(StackArgs)

        __props__.__dict__["agent_version"] = None
        __props__.__dict__["attributes"] = None
        __props__.__dict__["chef_configuration"] = None
        __props__.__dict__["clone_app_ids"] = None
        __props__.__dict__["clone_permissions"] = None
        __props__.__dict__["configuration_manager"] = None
        __props__.__dict__["custom_cookbooks_source"] = None
        __props__.__dict__["custom_json"] = None
        __props__.__dict__["default_availability_zone"] = None
        __props__.__dict__["default_instance_profile_arn"] = None
        __props__.__dict__["default_os"] = None
        __props__.__dict__["default_root_device_type"] = None
        __props__.__dict__["default_ssh_key_name"] = None
        __props__.__dict__["default_subnet_id"] = None
        __props__.__dict__["ecs_cluster_arn"] = None
        __props__.__dict__["elastic_ips"] = None
        __props__.__dict__["hostname_theme"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["rds_db_instances"] = None
        __props__.__dict__["service_role_arn"] = None
        __props__.__dict__["source_stack_id"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["use_custom_cookbooks"] = None
        __props__.__dict__["use_opsworks_security_groups"] = None
        __props__.__dict__["vpc_id"] = None
        return Stack(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="agentVersion")
    def agent_version(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "agent_version")

    @property
    @pulumi.getter
    def attributes(self) -> pulumi.Output[Optional[Any]]:
        return pulumi.get(self, "attributes")

    @property
    @pulumi.getter(name="chefConfiguration")
    def chef_configuration(self) -> pulumi.Output[Optional['outputs.StackChefConfiguration']]:
        return pulumi.get(self, "chef_configuration")

    @property
    @pulumi.getter(name="cloneAppIds")
    def clone_app_ids(self) -> pulumi.Output[Optional[Sequence[str]]]:
        return pulumi.get(self, "clone_app_ids")

    @property
    @pulumi.getter(name="clonePermissions")
    def clone_permissions(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "clone_permissions")

    @property
    @pulumi.getter(name="configurationManager")
    def configuration_manager(self) -> pulumi.Output[Optional['outputs.StackConfigurationManager']]:
        return pulumi.get(self, "configuration_manager")

    @property
    @pulumi.getter(name="customCookbooksSource")
    def custom_cookbooks_source(self) -> pulumi.Output[Optional['outputs.StackSource']]:
        return pulumi.get(self, "custom_cookbooks_source")

    @property
    @pulumi.getter(name="customJson")
    def custom_json(self) -> pulumi.Output[Optional[Any]]:
        return pulumi.get(self, "custom_json")

    @property
    @pulumi.getter(name="defaultAvailabilityZone")
    def default_availability_zone(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "default_availability_zone")

    @property
    @pulumi.getter(name="defaultInstanceProfileArn")
    def default_instance_profile_arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "default_instance_profile_arn")

    @property
    @pulumi.getter(name="defaultOs")
    def default_os(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "default_os")

    @property
    @pulumi.getter(name="defaultRootDeviceType")
    def default_root_device_type(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "default_root_device_type")

    @property
    @pulumi.getter(name="defaultSshKeyName")
    def default_ssh_key_name(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "default_ssh_key_name")

    @property
    @pulumi.getter(name="defaultSubnetId")
    def default_subnet_id(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "default_subnet_id")

    @property
    @pulumi.getter(name="ecsClusterArn")
    def ecs_cluster_arn(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "ecs_cluster_arn")

    @property
    @pulumi.getter(name="elasticIps")
    def elastic_ips(self) -> pulumi.Output[Optional[Sequence['outputs.StackElasticIp']]]:
        return pulumi.get(self, "elastic_ips")

    @property
    @pulumi.getter(name="hostnameTheme")
    def hostname_theme(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "hostname_theme")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="rdsDbInstances")
    def rds_db_instances(self) -> pulumi.Output[Optional[Sequence['outputs.StackRdsDbInstance']]]:
        return pulumi.get(self, "rds_db_instances")

    @property
    @pulumi.getter(name="serviceRoleArn")
    def service_role_arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "service_role_arn")

    @property
    @pulumi.getter(name="sourceStackId")
    def source_stack_id(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "source_stack_id")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.StackTag']]]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="useCustomCookbooks")
    def use_custom_cookbooks(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "use_custom_cookbooks")

    @property
    @pulumi.getter(name="useOpsworksSecurityGroups")
    def use_opsworks_security_groups(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "use_opsworks_security_groups")

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "vpc_id")

