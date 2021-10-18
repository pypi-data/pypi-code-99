"""
Type annotations for network-firewall service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_network_firewall import NetworkFirewallClient

    client: NetworkFirewallClient = boto3.client("network-firewall")
    ```
"""
import sys
from typing import Any, Dict, Mapping, Sequence, Type, overload

from botocore.client import BaseClient, ClientMeta

from .literals import RuleGroupTypeType
from .paginator import (
    ListFirewallPoliciesPaginator,
    ListFirewallsPaginator,
    ListRuleGroupsPaginator,
    ListTagsForResourcePaginator,
)
from .type_defs import (
    AssociateFirewallPolicyResponseTypeDef,
    AssociateSubnetsResponseTypeDef,
    CreateFirewallPolicyResponseTypeDef,
    CreateFirewallResponseTypeDef,
    CreateRuleGroupResponseTypeDef,
    DeleteFirewallPolicyResponseTypeDef,
    DeleteFirewallResponseTypeDef,
    DeleteRuleGroupResponseTypeDef,
    DescribeFirewallPolicyResponseTypeDef,
    DescribeFirewallResponseTypeDef,
    DescribeLoggingConfigurationResponseTypeDef,
    DescribeResourcePolicyResponseTypeDef,
    DescribeRuleGroupResponseTypeDef,
    DisassociateSubnetsResponseTypeDef,
    FirewallPolicyTypeDef,
    ListFirewallPoliciesResponseTypeDef,
    ListFirewallsResponseTypeDef,
    ListRuleGroupsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    LoggingConfigurationTypeDef,
    RuleGroupTypeDef,
    SubnetMappingTypeDef,
    TagTypeDef,
    UpdateFirewallDeleteProtectionResponseTypeDef,
    UpdateFirewallDescriptionResponseTypeDef,
    UpdateFirewallPolicyChangeProtectionResponseTypeDef,
    UpdateFirewallPolicyResponseTypeDef,
    UpdateLoggingConfigurationResponseTypeDef,
    UpdateRuleGroupResponseTypeDef,
    UpdateSubnetChangeProtectionResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("NetworkFirewallClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    InsufficientCapacityException: Type[BotocoreClientError]
    InternalServerError: Type[BotocoreClientError]
    InvalidOperationException: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]
    InvalidResourcePolicyException: Type[BotocoreClientError]
    InvalidTokenException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    LogDestinationPermissionException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ResourceOwnerCheckException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    UnsupportedOperationException: Type[BotocoreClientError]


class NetworkFirewallClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.64/reference/services/network-firewall.html#NetworkFirewall.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        NetworkFirewallClient exceptions.
        """

    def associate_firewall_policy(
        self,
        *,
        FirewallPolicyArn: str,
        UpdateToken: str = ...,
        FirewallArn: str = ...,
        FirewallName: str = ...
    ) -> AssociateFirewallPolicyResponseTypeDef:
        """
        Associates a  FirewallPolicy to a  Firewall .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.64/reference/services/network-firewall.html#NetworkFirewall.Client.associate_firewall_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client.html#associate_firewall_policy)
        """

    def associate_subnets(
        self,
        *,
        SubnetMappings: Sequence["SubnetMappingTypeDef"],
        UpdateToken: str = ...,
        FirewallArn: str = ...,
        FirewallName: str = ...
    ) -> AssociateSubnetsResponseTypeDef:
        """
        Associates the specified subnets in the Amazon VPC to the firewall.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.64/reference/services/network-firewall.html#NetworkFirewall.Client.associate_subnets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client.html#associate_subnets)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.64/reference/services/network-firewall.html#NetworkFirewall.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client.html#can_paginate)
        """

    def create_firewall(
        self,
        *,
        FirewallName: str,
        FirewallPolicyArn: str,
        VpcId: str,
        SubnetMappings: Sequence["SubnetMappingTypeDef"],
        DeleteProtection: bool = ...,
        SubnetChangeProtection: bool = ...,
        FirewallPolicyChangeProtection: bool = ...,
        Description: str = ...,
        Tags: Sequence["TagTypeDef"] = ...
    ) -> CreateFirewallResponseTypeDef:
        """
        Creates an AWS Network Firewall  Firewall and accompanying  FirewallStatus for a
        VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.64/reference/services/network-firewall.html#NetworkFirewall.Client.create_firewall)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client.html#create_firewall)
        """

    def create_firewall_policy(
        self,
        *,
        FirewallPolicyName: str,
        FirewallPolicy: "FirewallPolicyTypeDef",
        Description: str = ...,
        Tags: Sequence["TagTypeDef"] = ...,
        DryRun: bool = ...
    ) -> CreateFirewallPolicyResponseTypeDef:
        """
        Creates the firewall policy for the firewall according to the specifications.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.64/reference/services/network-firewall.html#NetworkFirewall.Client.create_firewall_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client.html#create_firewall_policy)
        """

    def create_rule_group(
        self,
        *,
        RuleGroupName: str,
        Type: RuleGroupTypeType,
        Capacity: int,
        RuleGroup: "RuleGroupTypeDef" = ...,
        Rules: str = ...,
        Description: str = ...,
        Tags: Sequence["TagTypeDef"] = ...,
        DryRun: bool = ...
    ) -> CreateRuleGroupResponseTypeDef:
        """
        Creates the specified stateless or stateful rule group, which includes the rules
        for network traffic inspection, a capacity setting, and tags.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.64/reference/services/network-firewall.html#NetworkFirewall.Client.create_rule_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client.html#create_rule_group)
        """

    def delete_firewall(
        self, *, FirewallName: str = ..., FirewallArn: str = ...
    ) -> DeleteFirewallResponseTypeDef:
        """
        Deletes the specified  Firewall and its  FirewallStatus.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.64/reference/services/network-firewall.html#NetworkFirewall.Client.delete_firewall)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client.html#delete_firewall)
        """

    def delete_firewall_policy(
        self, *, FirewallPolicyName: str = ..., FirewallPolicyArn: str = ...
    ) -> DeleteFirewallPolicyResponseTypeDef:
        """
        Deletes the specified  FirewallPolicy .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.64/reference/services/network-firewall.html#NetworkFirewall.Client.delete_firewall_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client.html#delete_firewall_policy)
        """

    def delete_resource_policy(self, *, ResourceArn: str) -> Dict[str, Any]:
        """
        Deletes a resource policy that you created in a  PutResourcePolicy request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.64/reference/services/network-firewall.html#NetworkFirewall.Client.delete_resource_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client.html#delete_resource_policy)
        """

    def delete_rule_group(
        self, *, RuleGroupName: str = ..., RuleGroupArn: str = ..., Type: RuleGroupTypeType = ...
    ) -> DeleteRuleGroupResponseTypeDef:
        """
        Deletes the specified  RuleGroup .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.64/reference/services/network-firewall.html#NetworkFirewall.Client.delete_rule_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client.html#delete_rule_group)
        """

    def describe_firewall(
        self, *, FirewallName: str = ..., FirewallArn: str = ...
    ) -> DescribeFirewallResponseTypeDef:
        """
        Returns the data objects for the specified firewall.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.64/reference/services/network-firewall.html#NetworkFirewall.Client.describe_firewall)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client.html#describe_firewall)
        """

    def describe_firewall_policy(
        self, *, FirewallPolicyName: str = ..., FirewallPolicyArn: str = ...
    ) -> DescribeFirewallPolicyResponseTypeDef:
        """
        Returns the data objects for the specified firewall policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.64/reference/services/network-firewall.html#NetworkFirewall.Client.describe_firewall_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client.html#describe_firewall_policy)
        """

    def describe_logging_configuration(
        self, *, FirewallArn: str = ..., FirewallName: str = ...
    ) -> DescribeLoggingConfigurationResponseTypeDef:
        """
        Returns the logging configuration for the specified firewall.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.64/reference/services/network-firewall.html#NetworkFirewall.Client.describe_logging_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client.html#describe_logging_configuration)
        """

    def describe_resource_policy(
        self, *, ResourceArn: str
    ) -> DescribeResourcePolicyResponseTypeDef:
        """
        Retrieves a resource policy that you created in a  PutResourcePolicy request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.64/reference/services/network-firewall.html#NetworkFirewall.Client.describe_resource_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client.html#describe_resource_policy)
        """

    def describe_rule_group(
        self, *, RuleGroupName: str = ..., RuleGroupArn: str = ..., Type: RuleGroupTypeType = ...
    ) -> DescribeRuleGroupResponseTypeDef:
        """
        Returns the data objects for the specified rule group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.64/reference/services/network-firewall.html#NetworkFirewall.Client.describe_rule_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client.html#describe_rule_group)
        """

    def disassociate_subnets(
        self,
        *,
        SubnetIds: Sequence[str],
        UpdateToken: str = ...,
        FirewallArn: str = ...,
        FirewallName: str = ...
    ) -> DisassociateSubnetsResponseTypeDef:
        """
        Removes the specified subnet associations from the firewall.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.64/reference/services/network-firewall.html#NetworkFirewall.Client.disassociate_subnets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client.html#disassociate_subnets)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.64/reference/services/network-firewall.html#NetworkFirewall.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client.html#generate_presigned_url)
        """

    def list_firewall_policies(
        self, *, NextToken: str = ..., MaxResults: int = ...
    ) -> ListFirewallPoliciesResponseTypeDef:
        """
        Retrieves the metadata for the firewall policies that you have defined.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.64/reference/services/network-firewall.html#NetworkFirewall.Client.list_firewall_policies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client.html#list_firewall_policies)
        """

    def list_firewalls(
        self, *, NextToken: str = ..., VpcIds: Sequence[str] = ..., MaxResults: int = ...
    ) -> ListFirewallsResponseTypeDef:
        """
        Retrieves the metadata for the firewalls that you have defined.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.64/reference/services/network-firewall.html#NetworkFirewall.Client.list_firewalls)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client.html#list_firewalls)
        """

    def list_rule_groups(
        self, *, NextToken: str = ..., MaxResults: int = ...
    ) -> ListRuleGroupsResponseTypeDef:
        """
        Retrieves the metadata for the rule groups that you have defined.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.64/reference/services/network-firewall.html#NetworkFirewall.Client.list_rule_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client.html#list_rule_groups)
        """

    def list_tags_for_resource(
        self, *, ResourceArn: str, NextToken: str = ..., MaxResults: int = ...
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Retrieves the tags associated with the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.64/reference/services/network-firewall.html#NetworkFirewall.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client.html#list_tags_for_resource)
        """

    def put_resource_policy(self, *, ResourceArn: str, Policy: str) -> Dict[str, Any]:
        """
        Creates or updates an AWS Identity and Access Management policy for your rule
        group or firewall policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.64/reference/services/network-firewall.html#NetworkFirewall.Client.put_resource_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client.html#put_resource_policy)
        """

    def tag_resource(self, *, ResourceArn: str, Tags: Sequence["TagTypeDef"]) -> Dict[str, Any]:
        """
        Adds the specified tags to the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.64/reference/services/network-firewall.html#NetworkFirewall.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client.html#tag_resource)
        """

    def untag_resource(self, *, ResourceArn: str, TagKeys: Sequence[str]) -> Dict[str, Any]:
        """
        Removes the tags with the specified keys from the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.64/reference/services/network-firewall.html#NetworkFirewall.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client.html#untag_resource)
        """

    def update_firewall_delete_protection(
        self,
        *,
        DeleteProtection: bool,
        UpdateToken: str = ...,
        FirewallArn: str = ...,
        FirewallName: str = ...
    ) -> UpdateFirewallDeleteProtectionResponseTypeDef:
        """
        Modifies the flag, `DeleteProtection` , which indicates whether it is possible
        to delete the firewall.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.64/reference/services/network-firewall.html#NetworkFirewall.Client.update_firewall_delete_protection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client.html#update_firewall_delete_protection)
        """

    def update_firewall_description(
        self,
        *,
        UpdateToken: str = ...,
        FirewallArn: str = ...,
        FirewallName: str = ...,
        Description: str = ...
    ) -> UpdateFirewallDescriptionResponseTypeDef:
        """
        Modifies the description for the specified firewall.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.64/reference/services/network-firewall.html#NetworkFirewall.Client.update_firewall_description)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client.html#update_firewall_description)
        """

    def update_firewall_policy(
        self,
        *,
        UpdateToken: str,
        FirewallPolicy: "FirewallPolicyTypeDef",
        FirewallPolicyArn: str = ...,
        FirewallPolicyName: str = ...,
        Description: str = ...,
        DryRun: bool = ...
    ) -> UpdateFirewallPolicyResponseTypeDef:
        """
        Updates the properties of the specified firewall policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.64/reference/services/network-firewall.html#NetworkFirewall.Client.update_firewall_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client.html#update_firewall_policy)
        """

    def update_firewall_policy_change_protection(
        self,
        *,
        FirewallPolicyChangeProtection: bool,
        UpdateToken: str = ...,
        FirewallArn: str = ...,
        FirewallName: str = ...
    ) -> UpdateFirewallPolicyChangeProtectionResponseTypeDef:
        """
        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/network-
        firewall-2020-11-12/UpdateFirewallPolicyChangeProtection>`_ **Request Syntax**
        response = client.update_firewall_policy_change_protection(
        UpdateToken='string', FirewallArn='string', Firew...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.64/reference/services/network-firewall.html#NetworkFirewall.Client.update_firewall_policy_change_protection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client.html#update_firewall_policy_change_protection)
        """

    def update_logging_configuration(
        self,
        *,
        FirewallArn: str = ...,
        FirewallName: str = ...,
        LoggingConfiguration: "LoggingConfigurationTypeDef" = ...
    ) -> UpdateLoggingConfigurationResponseTypeDef:
        """
        Sets the logging configuration for the specified firewall.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.64/reference/services/network-firewall.html#NetworkFirewall.Client.update_logging_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client.html#update_logging_configuration)
        """

    def update_rule_group(
        self,
        *,
        UpdateToken: str,
        RuleGroupArn: str = ...,
        RuleGroupName: str = ...,
        RuleGroup: "RuleGroupTypeDef" = ...,
        Rules: str = ...,
        Type: RuleGroupTypeType = ...,
        Description: str = ...,
        DryRun: bool = ...
    ) -> UpdateRuleGroupResponseTypeDef:
        """
        Updates the rule settings for the specified rule group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.64/reference/services/network-firewall.html#NetworkFirewall.Client.update_rule_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client.html#update_rule_group)
        """

    def update_subnet_change_protection(
        self,
        *,
        SubnetChangeProtection: bool,
        UpdateToken: str = ...,
        FirewallArn: str = ...,
        FirewallName: str = ...
    ) -> UpdateSubnetChangeProtectionResponseTypeDef:
        """
        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/network-
        firewall-2020-11-12/UpdateSubnetChangeProtection>`_ **Request Syntax** response
        = client.update_subnet_change_protection( UpdateToken='string',
        FirewallArn='string', FirewallName='string',...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.64/reference/services/network-firewall.html#NetworkFirewall.Client.update_subnet_change_protection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/client.html#update_subnet_change_protection)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_firewall_policies"]
    ) -> ListFirewallPoliciesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.64/reference/services/network-firewall.html#NetworkFirewall.Paginator.ListFirewallPolicies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/paginators.html#listfirewallpoliciespaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_firewalls"]) -> ListFirewallsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.64/reference/services/network-firewall.html#NetworkFirewall.Paginator.ListFirewalls)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/paginators.html#listfirewallspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_rule_groups"]) -> ListRuleGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.64/reference/services/network-firewall.html#NetworkFirewall.Paginator.ListRuleGroups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/paginators.html#listrulegroupspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_tags_for_resource"]
    ) -> ListTagsForResourcePaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.64/reference/services/network-firewall.html#NetworkFirewall.Paginator.ListTagsForResource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/paginators.html#listtagsforresourcepaginator)
        """
