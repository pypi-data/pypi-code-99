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

__all__ = ['CampaignArgs', 'Campaign']

@pulumi.input_type
class CampaignArgs:
    def __init__(__self__, *,
                 application_id: pulumi.Input[str],
                 message_configuration: pulumi.Input['CampaignMessageConfigurationArgs'],
                 name: pulumi.Input[str],
                 schedule: pulumi.Input['CampaignScheduleArgs'],
                 segment_id: pulumi.Input[str],
                 additional_treatments: Optional[pulumi.Input[Sequence[pulumi.Input['CampaignWriteTreatmentResourceArgs']]]] = None,
                 campaign_hook: Optional[pulumi.Input['CampaignHookArgs']] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 holdout_percent: Optional[pulumi.Input[int]] = None,
                 is_paused: Optional[pulumi.Input[bool]] = None,
                 limits: Optional[pulumi.Input['CampaignLimitsArgs']] = None,
                 segment_version: Optional[pulumi.Input[int]] = None,
                 tags: Optional[Any] = None,
                 treatment_description: Optional[pulumi.Input[str]] = None,
                 treatment_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Campaign resource.
        """
        pulumi.set(__self__, "application_id", application_id)
        pulumi.set(__self__, "message_configuration", message_configuration)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "schedule", schedule)
        pulumi.set(__self__, "segment_id", segment_id)
        if additional_treatments is not None:
            pulumi.set(__self__, "additional_treatments", additional_treatments)
        if campaign_hook is not None:
            pulumi.set(__self__, "campaign_hook", campaign_hook)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if holdout_percent is not None:
            pulumi.set(__self__, "holdout_percent", holdout_percent)
        if is_paused is not None:
            pulumi.set(__self__, "is_paused", is_paused)
        if limits is not None:
            pulumi.set(__self__, "limits", limits)
        if segment_version is not None:
            pulumi.set(__self__, "segment_version", segment_version)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if treatment_description is not None:
            pulumi.set(__self__, "treatment_description", treatment_description)
        if treatment_name is not None:
            pulumi.set(__self__, "treatment_name", treatment_name)

    @property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "application_id")

    @application_id.setter
    def application_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "application_id", value)

    @property
    @pulumi.getter(name="messageConfiguration")
    def message_configuration(self) -> pulumi.Input['CampaignMessageConfigurationArgs']:
        return pulumi.get(self, "message_configuration")

    @message_configuration.setter
    def message_configuration(self, value: pulumi.Input['CampaignMessageConfigurationArgs']):
        pulumi.set(self, "message_configuration", value)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def schedule(self) -> pulumi.Input['CampaignScheduleArgs']:
        return pulumi.get(self, "schedule")

    @schedule.setter
    def schedule(self, value: pulumi.Input['CampaignScheduleArgs']):
        pulumi.set(self, "schedule", value)

    @property
    @pulumi.getter(name="segmentId")
    def segment_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "segment_id")

    @segment_id.setter
    def segment_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "segment_id", value)

    @property
    @pulumi.getter(name="additionalTreatments")
    def additional_treatments(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['CampaignWriteTreatmentResourceArgs']]]]:
        return pulumi.get(self, "additional_treatments")

    @additional_treatments.setter
    def additional_treatments(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['CampaignWriteTreatmentResourceArgs']]]]):
        pulumi.set(self, "additional_treatments", value)

    @property
    @pulumi.getter(name="campaignHook")
    def campaign_hook(self) -> Optional[pulumi.Input['CampaignHookArgs']]:
        return pulumi.get(self, "campaign_hook")

    @campaign_hook.setter
    def campaign_hook(self, value: Optional[pulumi.Input['CampaignHookArgs']]):
        pulumi.set(self, "campaign_hook", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="holdoutPercent")
    def holdout_percent(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "holdout_percent")

    @holdout_percent.setter
    def holdout_percent(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "holdout_percent", value)

    @property
    @pulumi.getter(name="isPaused")
    def is_paused(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "is_paused")

    @is_paused.setter
    def is_paused(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_paused", value)

    @property
    @pulumi.getter
    def limits(self) -> Optional[pulumi.Input['CampaignLimitsArgs']]:
        return pulumi.get(self, "limits")

    @limits.setter
    def limits(self, value: Optional[pulumi.Input['CampaignLimitsArgs']]):
        pulumi.set(self, "limits", value)

    @property
    @pulumi.getter(name="segmentVersion")
    def segment_version(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "segment_version")

    @segment_version.setter
    def segment_version(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "segment_version", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[Any]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[Any]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="treatmentDescription")
    def treatment_description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "treatment_description")

    @treatment_description.setter
    def treatment_description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "treatment_description", value)

    @property
    @pulumi.getter(name="treatmentName")
    def treatment_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "treatment_name")

    @treatment_name.setter
    def treatment_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "treatment_name", value)


warnings.warn("""Campaign is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class Campaign(pulumi.CustomResource):
    warnings.warn("""Campaign is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 additional_treatments: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CampaignWriteTreatmentResourceArgs']]]]] = None,
                 application_id: Optional[pulumi.Input[str]] = None,
                 campaign_hook: Optional[pulumi.Input[pulumi.InputType['CampaignHookArgs']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 holdout_percent: Optional[pulumi.Input[int]] = None,
                 is_paused: Optional[pulumi.Input[bool]] = None,
                 limits: Optional[pulumi.Input[pulumi.InputType['CampaignLimitsArgs']]] = None,
                 message_configuration: Optional[pulumi.Input[pulumi.InputType['CampaignMessageConfigurationArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 schedule: Optional[pulumi.Input[pulumi.InputType['CampaignScheduleArgs']]] = None,
                 segment_id: Optional[pulumi.Input[str]] = None,
                 segment_version: Optional[pulumi.Input[int]] = None,
                 tags: Optional[Any] = None,
                 treatment_description: Optional[pulumi.Input[str]] = None,
                 treatment_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::Pinpoint::Campaign

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CampaignArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::Pinpoint::Campaign

        :param str resource_name: The name of the resource.
        :param CampaignArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CampaignArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 additional_treatments: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CampaignWriteTreatmentResourceArgs']]]]] = None,
                 application_id: Optional[pulumi.Input[str]] = None,
                 campaign_hook: Optional[pulumi.Input[pulumi.InputType['CampaignHookArgs']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 holdout_percent: Optional[pulumi.Input[int]] = None,
                 is_paused: Optional[pulumi.Input[bool]] = None,
                 limits: Optional[pulumi.Input[pulumi.InputType['CampaignLimitsArgs']]] = None,
                 message_configuration: Optional[pulumi.Input[pulumi.InputType['CampaignMessageConfigurationArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 schedule: Optional[pulumi.Input[pulumi.InputType['CampaignScheduleArgs']]] = None,
                 segment_id: Optional[pulumi.Input[str]] = None,
                 segment_version: Optional[pulumi.Input[int]] = None,
                 tags: Optional[Any] = None,
                 treatment_description: Optional[pulumi.Input[str]] = None,
                 treatment_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        pulumi.log.warn("""Campaign is deprecated: Campaign is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = CampaignArgs.__new__(CampaignArgs)

            __props__.__dict__["additional_treatments"] = additional_treatments
            if application_id is None and not opts.urn:
                raise TypeError("Missing required property 'application_id'")
            __props__.__dict__["application_id"] = application_id
            __props__.__dict__["campaign_hook"] = campaign_hook
            __props__.__dict__["description"] = description
            __props__.__dict__["holdout_percent"] = holdout_percent
            __props__.__dict__["is_paused"] = is_paused
            __props__.__dict__["limits"] = limits
            if message_configuration is None and not opts.urn:
                raise TypeError("Missing required property 'message_configuration'")
            __props__.__dict__["message_configuration"] = message_configuration
            if name is None and not opts.urn:
                raise TypeError("Missing required property 'name'")
            __props__.__dict__["name"] = name
            if schedule is None and not opts.urn:
                raise TypeError("Missing required property 'schedule'")
            __props__.__dict__["schedule"] = schedule
            if segment_id is None and not opts.urn:
                raise TypeError("Missing required property 'segment_id'")
            __props__.__dict__["segment_id"] = segment_id
            __props__.__dict__["segment_version"] = segment_version
            __props__.__dict__["tags"] = tags
            __props__.__dict__["treatment_description"] = treatment_description
            __props__.__dict__["treatment_name"] = treatment_name
            __props__.__dict__["arn"] = None
            __props__.__dict__["campaign_id"] = None
        super(Campaign, __self__).__init__(
            'aws-native:pinpoint:Campaign',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Campaign':
        """
        Get an existing Campaign resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = CampaignArgs.__new__(CampaignArgs)

        __props__.__dict__["additional_treatments"] = None
        __props__.__dict__["application_id"] = None
        __props__.__dict__["arn"] = None
        __props__.__dict__["campaign_hook"] = None
        __props__.__dict__["campaign_id"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["holdout_percent"] = None
        __props__.__dict__["is_paused"] = None
        __props__.__dict__["limits"] = None
        __props__.__dict__["message_configuration"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["schedule"] = None
        __props__.__dict__["segment_id"] = None
        __props__.__dict__["segment_version"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["treatment_description"] = None
        __props__.__dict__["treatment_name"] = None
        return Campaign(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="additionalTreatments")
    def additional_treatments(self) -> pulumi.Output[Optional[Sequence['outputs.CampaignWriteTreatmentResource']]]:
        return pulumi.get(self, "additional_treatments")

    @property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "application_id")

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="campaignHook")
    def campaign_hook(self) -> pulumi.Output[Optional['outputs.CampaignHook']]:
        return pulumi.get(self, "campaign_hook")

    @property
    @pulumi.getter(name="campaignId")
    def campaign_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "campaign_id")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="holdoutPercent")
    def holdout_percent(self) -> pulumi.Output[Optional[int]]:
        return pulumi.get(self, "holdout_percent")

    @property
    @pulumi.getter(name="isPaused")
    def is_paused(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "is_paused")

    @property
    @pulumi.getter
    def limits(self) -> pulumi.Output[Optional['outputs.CampaignLimits']]:
        return pulumi.get(self, "limits")

    @property
    @pulumi.getter(name="messageConfiguration")
    def message_configuration(self) -> pulumi.Output['outputs.CampaignMessageConfiguration']:
        return pulumi.get(self, "message_configuration")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def schedule(self) -> pulumi.Output['outputs.CampaignSchedule']:
        return pulumi.get(self, "schedule")

    @property
    @pulumi.getter(name="segmentId")
    def segment_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "segment_id")

    @property
    @pulumi.getter(name="segmentVersion")
    def segment_version(self) -> pulumi.Output[Optional[int]]:
        return pulumi.get(self, "segment_version")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Any]]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="treatmentDescription")
    def treatment_description(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "treatment_description")

    @property
    @pulumi.getter(name="treatmentName")
    def treatment_name(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "treatment_name")

