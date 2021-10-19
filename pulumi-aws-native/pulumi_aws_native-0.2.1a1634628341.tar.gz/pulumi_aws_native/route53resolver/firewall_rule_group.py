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

__all__ = ['FirewallRuleGroupArgs', 'FirewallRuleGroup']

@pulumi.input_type
class FirewallRuleGroupArgs:
    def __init__(__self__, *,
                 firewall_rules: Optional[pulumi.Input[Sequence[pulumi.Input['FirewallRuleGroupFirewallRuleArgs']]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['FirewallRuleGroupTagArgs']]]] = None):
        """
        The set of arguments for constructing a FirewallRuleGroup resource.
        :param pulumi.Input[Sequence[pulumi.Input['FirewallRuleGroupFirewallRuleArgs']]] firewall_rules: FirewallRules
        :param pulumi.Input[str] name: FirewallRuleGroupName
        :param pulumi.Input[Sequence[pulumi.Input['FirewallRuleGroupTagArgs']]] tags: Tags
        """
        if firewall_rules is not None:
            pulumi.set(__self__, "firewall_rules", firewall_rules)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="firewallRules")
    def firewall_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['FirewallRuleGroupFirewallRuleArgs']]]]:
        """
        FirewallRules
        """
        return pulumi.get(self, "firewall_rules")

    @firewall_rules.setter
    def firewall_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['FirewallRuleGroupFirewallRuleArgs']]]]):
        pulumi.set(self, "firewall_rules", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        FirewallRuleGroupName
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['FirewallRuleGroupTagArgs']]]]:
        """
        Tags
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['FirewallRuleGroupTagArgs']]]]):
        pulumi.set(self, "tags", value)


class FirewallRuleGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 firewall_rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FirewallRuleGroupFirewallRuleArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FirewallRuleGroupTagArgs']]]]] = None,
                 __props__=None):
        """
        Resource schema for AWS::Route53Resolver::FirewallRuleGroup.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FirewallRuleGroupFirewallRuleArgs']]]] firewall_rules: FirewallRules
        :param pulumi.Input[str] name: FirewallRuleGroupName
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FirewallRuleGroupTagArgs']]]] tags: Tags
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[FirewallRuleGroupArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource schema for AWS::Route53Resolver::FirewallRuleGroup.

        :param str resource_name: The name of the resource.
        :param FirewallRuleGroupArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(FirewallRuleGroupArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 firewall_rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FirewallRuleGroupFirewallRuleArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FirewallRuleGroupTagArgs']]]]] = None,
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
            __props__ = FirewallRuleGroupArgs.__new__(FirewallRuleGroupArgs)

            __props__.__dict__["firewall_rules"] = firewall_rules
            __props__.__dict__["name"] = name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["arn"] = None
            __props__.__dict__["creation_time"] = None
            __props__.__dict__["creator_request_id"] = None
            __props__.__dict__["modification_time"] = None
            __props__.__dict__["owner_id"] = None
            __props__.__dict__["rule_count"] = None
            __props__.__dict__["share_status"] = None
            __props__.__dict__["status"] = None
            __props__.__dict__["status_message"] = None
        super(FirewallRuleGroup, __self__).__init__(
            'aws-native:route53resolver:FirewallRuleGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'FirewallRuleGroup':
        """
        Get an existing FirewallRuleGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = FirewallRuleGroupArgs.__new__(FirewallRuleGroupArgs)

        __props__.__dict__["arn"] = None
        __props__.__dict__["creation_time"] = None
        __props__.__dict__["creator_request_id"] = None
        __props__.__dict__["firewall_rules"] = None
        __props__.__dict__["modification_time"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["owner_id"] = None
        __props__.__dict__["rule_count"] = None
        __props__.__dict__["share_status"] = None
        __props__.__dict__["status"] = None
        __props__.__dict__["status_message"] = None
        __props__.__dict__["tags"] = None
        return FirewallRuleGroup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        Arn
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> pulumi.Output[str]:
        """
        Rfc3339TimeString
        """
        return pulumi.get(self, "creation_time")

    @property
    @pulumi.getter(name="creatorRequestId")
    def creator_request_id(self) -> pulumi.Output[str]:
        """
        The id of the creator request.
        """
        return pulumi.get(self, "creator_request_id")

    @property
    @pulumi.getter(name="firewallRules")
    def firewall_rules(self) -> pulumi.Output[Optional[Sequence['outputs.FirewallRuleGroupFirewallRule']]]:
        """
        FirewallRules
        """
        return pulumi.get(self, "firewall_rules")

    @property
    @pulumi.getter(name="modificationTime")
    def modification_time(self) -> pulumi.Output[str]:
        """
        Rfc3339TimeString
        """
        return pulumi.get(self, "modification_time")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[str]]:
        """
        FirewallRuleGroupName
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="ownerId")
    def owner_id(self) -> pulumi.Output[str]:
        """
        AccountId
        """
        return pulumi.get(self, "owner_id")

    @property
    @pulumi.getter(name="ruleCount")
    def rule_count(self) -> pulumi.Output[int]:
        """
        Count
        """
        return pulumi.get(self, "rule_count")

    @property
    @pulumi.getter(name="shareStatus")
    def share_status(self) -> pulumi.Output['FirewallRuleGroupShareStatus']:
        """
        ShareStatus, possible values are NOT_SHARED, SHARED_WITH_ME, SHARED_BY_ME.
        """
        return pulumi.get(self, "share_status")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output['FirewallRuleGroupStatus']:
        """
        ResolverFirewallRuleGroupAssociation, possible values are COMPLETE, DELETING, UPDATING, and INACTIVE_OWNER_ACCOUNT_CLOSED.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="statusMessage")
    def status_message(self) -> pulumi.Output[str]:
        """
        FirewallRuleGroupStatus
        """
        return pulumi.get(self, "status_message")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.FirewallRuleGroupTag']]]:
        """
        Tags
        """
        return pulumi.get(self, "tags")

