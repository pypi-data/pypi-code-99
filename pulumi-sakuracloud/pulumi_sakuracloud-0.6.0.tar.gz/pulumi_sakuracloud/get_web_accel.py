# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'GetWebAccelResult',
    'AwaitableGetWebAccelResult',
    'get_web_accel',
    'get_web_accel_output',
]

@pulumi.output_type
class GetWebAccelResult:
    """
    A collection of values returned by getWebAccel.
    """
    def __init__(__self__, cname_record_value=None, domain=None, domain_type=None, has_certificate=None, host_header=None, id=None, name=None, origin=None, site_id=None, status=None, subdomain=None, txt_record_value=None):
        if cname_record_value and not isinstance(cname_record_value, str):
            raise TypeError("Expected argument 'cname_record_value' to be a str")
        pulumi.set(__self__, "cname_record_value", cname_record_value)
        if domain and not isinstance(domain, str):
            raise TypeError("Expected argument 'domain' to be a str")
        pulumi.set(__self__, "domain", domain)
        if domain_type and not isinstance(domain_type, str):
            raise TypeError("Expected argument 'domain_type' to be a str")
        pulumi.set(__self__, "domain_type", domain_type)
        if has_certificate and not isinstance(has_certificate, bool):
            raise TypeError("Expected argument 'has_certificate' to be a bool")
        pulumi.set(__self__, "has_certificate", has_certificate)
        if host_header and not isinstance(host_header, str):
            raise TypeError("Expected argument 'host_header' to be a str")
        pulumi.set(__self__, "host_header", host_header)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if origin and not isinstance(origin, str):
            raise TypeError("Expected argument 'origin' to be a str")
        pulumi.set(__self__, "origin", origin)
        if site_id and not isinstance(site_id, str):
            raise TypeError("Expected argument 'site_id' to be a str")
        pulumi.set(__self__, "site_id", site_id)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if subdomain and not isinstance(subdomain, str):
            raise TypeError("Expected argument 'subdomain' to be a str")
        pulumi.set(__self__, "subdomain", subdomain)
        if txt_record_value and not isinstance(txt_record_value, str):
            raise TypeError("Expected argument 'txt_record_value' to be a str")
        pulumi.set(__self__, "txt_record_value", txt_record_value)

    @property
    @pulumi.getter(name="cnameRecordValue")
    def cname_record_value(self) -> str:
        """
        .
        """
        return pulumi.get(self, "cname_record_value")

    @property
    @pulumi.getter
    def domain(self) -> str:
        return pulumi.get(self, "domain")

    @property
    @pulumi.getter(name="domainType")
    def domain_type(self) -> str:
        """
        .
        """
        return pulumi.get(self, "domain_type")

    @property
    @pulumi.getter(name="hasCertificate")
    def has_certificate(self) -> bool:
        """
        .
        """
        return pulumi.get(self, "has_certificate")

    @property
    @pulumi.getter(name="hostHeader")
    def host_header(self) -> str:
        """
        .
        """
        return pulumi.get(self, "host_header")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def origin(self) -> str:
        """
        .
        """
        return pulumi.get(self, "origin")

    @property
    @pulumi.getter(name="siteId")
    def site_id(self) -> str:
        """
        .
        """
        return pulumi.get(self, "site_id")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        .
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def subdomain(self) -> str:
        """
        .
        """
        return pulumi.get(self, "subdomain")

    @property
    @pulumi.getter(name="txtRecordValue")
    def txt_record_value(self) -> str:
        """
        .
        """
        return pulumi.get(self, "txt_record_value")


class AwaitableGetWebAccelResult(GetWebAccelResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetWebAccelResult(
            cname_record_value=self.cname_record_value,
            domain=self.domain,
            domain_type=self.domain_type,
            has_certificate=self.has_certificate,
            host_header=self.host_header,
            id=self.id,
            name=self.name,
            origin=self.origin,
            site_id=self.site_id,
            status=self.status,
            subdomain=self.subdomain,
            txt_record_value=self.txt_record_value)


def get_web_accel(domain: Optional[str] = None,
                  name: Optional[str] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetWebAccelResult:
    """
    Get information about an existing sakuracloud_webaccel.


    :param str domain: .
    :param str name: .
    """
    __args__ = dict()
    __args__['domain'] = domain
    __args__['name'] = name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('sakuracloud:index/getWebAccel:getWebAccel', __args__, opts=opts, typ=GetWebAccelResult).value

    return AwaitableGetWebAccelResult(
        cname_record_value=__ret__.cname_record_value,
        domain=__ret__.domain,
        domain_type=__ret__.domain_type,
        has_certificate=__ret__.has_certificate,
        host_header=__ret__.host_header,
        id=__ret__.id,
        name=__ret__.name,
        origin=__ret__.origin,
        site_id=__ret__.site_id,
        status=__ret__.status,
        subdomain=__ret__.subdomain,
        txt_record_value=__ret__.txt_record_value)


@_utilities.lift_output_func(get_web_accel)
def get_web_accel_output(domain: Optional[pulumi.Input[Optional[str]]] = None,
                         name: Optional[pulumi.Input[Optional[str]]] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetWebAccelResult]:
    """
    Get information about an existing sakuracloud_webaccel.


    :param str domain: .
    :param str name: .
    """
    ...
