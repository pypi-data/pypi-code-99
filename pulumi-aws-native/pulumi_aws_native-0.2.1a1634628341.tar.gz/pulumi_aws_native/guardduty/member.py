# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['MemberArgs', 'Member']

@pulumi.input_type
class MemberArgs:
    def __init__(__self__, *,
                 detector_id: pulumi.Input[str],
                 email: pulumi.Input[str],
                 disable_email_notification: Optional[pulumi.Input[bool]] = None,
                 message: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Member resource.
        """
        pulumi.set(__self__, "detector_id", detector_id)
        pulumi.set(__self__, "email", email)
        if disable_email_notification is not None:
            pulumi.set(__self__, "disable_email_notification", disable_email_notification)
        if message is not None:
            pulumi.set(__self__, "message", message)
        if status is not None:
            pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter(name="detectorId")
    def detector_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "detector_id")

    @detector_id.setter
    def detector_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "detector_id", value)

    @property
    @pulumi.getter
    def email(self) -> pulumi.Input[str]:
        return pulumi.get(self, "email")

    @email.setter
    def email(self, value: pulumi.Input[str]):
        pulumi.set(self, "email", value)

    @property
    @pulumi.getter(name="disableEmailNotification")
    def disable_email_notification(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "disable_email_notification")

    @disable_email_notification.setter
    def disable_email_notification(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "disable_email_notification", value)

    @property
    @pulumi.getter
    def message(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "message")

    @message.setter
    def message(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "message", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status", value)


warnings.warn("""Member is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class Member(pulumi.CustomResource):
    warnings.warn("""Member is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 detector_id: Optional[pulumi.Input[str]] = None,
                 disable_email_notification: Optional[pulumi.Input[bool]] = None,
                 email: Optional[pulumi.Input[str]] = None,
                 message: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::GuardDuty::Member

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: MemberArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::GuardDuty::Member

        :param str resource_name: The name of the resource.
        :param MemberArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(MemberArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 detector_id: Optional[pulumi.Input[str]] = None,
                 disable_email_notification: Optional[pulumi.Input[bool]] = None,
                 email: Optional[pulumi.Input[str]] = None,
                 message: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        pulumi.log.warn("""Member is deprecated: Member is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = MemberArgs.__new__(MemberArgs)

            if detector_id is None and not opts.urn:
                raise TypeError("Missing required property 'detector_id'")
            __props__.__dict__["detector_id"] = detector_id
            __props__.__dict__["disable_email_notification"] = disable_email_notification
            if email is None and not opts.urn:
                raise TypeError("Missing required property 'email'")
            __props__.__dict__["email"] = email
            __props__.__dict__["message"] = message
            __props__.__dict__["status"] = status
            __props__.__dict__["member_id"] = None
        super(Member, __self__).__init__(
            'aws-native:guardduty:Member',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Member':
        """
        Get an existing Member resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = MemberArgs.__new__(MemberArgs)

        __props__.__dict__["detector_id"] = None
        __props__.__dict__["disable_email_notification"] = None
        __props__.__dict__["email"] = None
        __props__.__dict__["member_id"] = None
        __props__.__dict__["message"] = None
        __props__.__dict__["status"] = None
        return Member(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="detectorId")
    def detector_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "detector_id")

    @property
    @pulumi.getter(name="disableEmailNotification")
    def disable_email_notification(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "disable_email_notification")

    @property
    @pulumi.getter
    def email(self) -> pulumi.Output[str]:
        return pulumi.get(self, "email")

    @property
    @pulumi.getter(name="memberId")
    def member_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "member_id")

    @property
    @pulumi.getter
    def message(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "message")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "status")

