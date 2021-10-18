# coding=utf-8
# *** WARNING: this file was generated by pulumigen. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs
from ... import meta as _meta

__all__ = [
    'AggregationRule',
    'ClusterRole',
    'ClusterRoleBinding',
    'PolicyRule',
    'Role',
    'RoleBinding',
    'RoleRef',
    'Subject',
]

@pulumi.output_type
class AggregationRule(dict):
    """
    AggregationRule describes how to locate ClusterRoles to aggregate into the ClusterRole
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "clusterRoleSelectors":
            suggest = "cluster_role_selectors"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in AggregationRule. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        AggregationRule.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        AggregationRule.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 cluster_role_selectors: Optional[Sequence['_meta.v1.outputs.LabelSelector']] = None):
        """
        AggregationRule describes how to locate ClusterRoles to aggregate into the ClusterRole
        :param Sequence['_meta.v1.LabelSelectorArgs'] cluster_role_selectors: ClusterRoleSelectors holds a list of selectors which will be used to find ClusterRoles and create the rules. If any of the selectors match, then the ClusterRole's permissions will be added
        """
        if cluster_role_selectors is not None:
            pulumi.set(__self__, "cluster_role_selectors", cluster_role_selectors)

    @property
    @pulumi.getter(name="clusterRoleSelectors")
    def cluster_role_selectors(self) -> Optional[Sequence['_meta.v1.outputs.LabelSelector']]:
        """
        ClusterRoleSelectors holds a list of selectors which will be used to find ClusterRoles and create the rules. If any of the selectors match, then the ClusterRole's permissions will be added
        """
        return pulumi.get(self, "cluster_role_selectors")


@pulumi.output_type
class ClusterRole(dict):
    """
    ClusterRole is a cluster level, logical grouping of PolicyRules that can be referenced as a unit by a RoleBinding or ClusterRoleBinding. Deprecated in v1.17 in favor of rbac.authorization.k8s.io/v1 ClusterRole, and will no longer be served in v1.20.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "aggregationRule":
            suggest = "aggregation_rule"
        elif key == "apiVersion":
            suggest = "api_version"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ClusterRole. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ClusterRole.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ClusterRole.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 aggregation_rule: Optional['outputs.AggregationRule'] = None,
                 api_version: Optional[str] = None,
                 kind: Optional[str] = None,
                 metadata: Optional['_meta.v1.outputs.ObjectMeta'] = None,
                 rules: Optional[Sequence['outputs.PolicyRule']] = None):
        """
        ClusterRole is a cluster level, logical grouping of PolicyRules that can be referenced as a unit by a RoleBinding or ClusterRoleBinding. Deprecated in v1.17 in favor of rbac.authorization.k8s.io/v1 ClusterRole, and will no longer be served in v1.20.
        :param 'AggregationRuleArgs' aggregation_rule: AggregationRule is an optional field that describes how to build the Rules for this ClusterRole. If AggregationRule is set, then the Rules are controller managed and direct changes to Rules will be stomped by the controller.
        :param str api_version: APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
        :param str kind: Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
        :param '_meta.v1.ObjectMetaArgs' metadata: Standard object's metadata.
        :param Sequence['PolicyRuleArgs'] rules: Rules holds all the PolicyRules for this ClusterRole
        """
        if aggregation_rule is not None:
            pulumi.set(__self__, "aggregation_rule", aggregation_rule)
        if api_version is not None:
            pulumi.set(__self__, "api_version", 'rbac.authorization.k8s.io/v1beta1')
        if kind is not None:
            pulumi.set(__self__, "kind", 'ClusterRole')
        if metadata is not None:
            pulumi.set(__self__, "metadata", metadata)
        if rules is not None:
            pulumi.set(__self__, "rules", rules)

    @property
    @pulumi.getter(name="aggregationRule")
    def aggregation_rule(self) -> Optional['outputs.AggregationRule']:
        """
        AggregationRule is an optional field that describes how to build the Rules for this ClusterRole. If AggregationRule is set, then the Rules are controller managed and direct changes to Rules will be stomped by the controller.
        """
        return pulumi.get(self, "aggregation_rule")

    @property
    @pulumi.getter(name="apiVersion")
    def api_version(self) -> Optional[str]:
        """
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
        """
        return pulumi.get(self, "api_version")

    @property
    @pulumi.getter
    def kind(self) -> Optional[str]:
        """
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def metadata(self) -> Optional['_meta.v1.outputs.ObjectMeta']:
        """
        Standard object's metadata.
        """
        return pulumi.get(self, "metadata")

    @property
    @pulumi.getter
    def rules(self) -> Optional[Sequence['outputs.PolicyRule']]:
        """
        Rules holds all the PolicyRules for this ClusterRole
        """
        return pulumi.get(self, "rules")


@pulumi.output_type
class ClusterRoleBinding(dict):
    """
    ClusterRoleBinding references a ClusterRole, but not contain it.  It can reference a ClusterRole in the global namespace, and adds who information via Subject. Deprecated in v1.17 in favor of rbac.authorization.k8s.io/v1 ClusterRoleBinding, and will no longer be served in v1.20.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "roleRef":
            suggest = "role_ref"
        elif key == "apiVersion":
            suggest = "api_version"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ClusterRoleBinding. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ClusterRoleBinding.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ClusterRoleBinding.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 role_ref: 'outputs.RoleRef',
                 api_version: Optional[str] = None,
                 kind: Optional[str] = None,
                 metadata: Optional['_meta.v1.outputs.ObjectMeta'] = None,
                 subjects: Optional[Sequence['outputs.Subject']] = None):
        """
        ClusterRoleBinding references a ClusterRole, but not contain it.  It can reference a ClusterRole in the global namespace, and adds who information via Subject. Deprecated in v1.17 in favor of rbac.authorization.k8s.io/v1 ClusterRoleBinding, and will no longer be served in v1.20.
        :param 'RoleRefArgs' role_ref: RoleRef can only reference a ClusterRole in the global namespace. If the RoleRef cannot be resolved, the Authorizer must return an error.
        :param str api_version: APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
        :param str kind: Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
        :param '_meta.v1.ObjectMetaArgs' metadata: Standard object's metadata.
        :param Sequence['SubjectArgs'] subjects: Subjects holds references to the objects the role applies to.
        """
        pulumi.set(__self__, "role_ref", role_ref)
        if api_version is not None:
            pulumi.set(__self__, "api_version", 'rbac.authorization.k8s.io/v1beta1')
        if kind is not None:
            pulumi.set(__self__, "kind", 'ClusterRoleBinding')
        if metadata is not None:
            pulumi.set(__self__, "metadata", metadata)
        if subjects is not None:
            pulumi.set(__self__, "subjects", subjects)

    @property
    @pulumi.getter(name="roleRef")
    def role_ref(self) -> 'outputs.RoleRef':
        """
        RoleRef can only reference a ClusterRole in the global namespace. If the RoleRef cannot be resolved, the Authorizer must return an error.
        """
        return pulumi.get(self, "role_ref")

    @property
    @pulumi.getter(name="apiVersion")
    def api_version(self) -> Optional[str]:
        """
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
        """
        return pulumi.get(self, "api_version")

    @property
    @pulumi.getter
    def kind(self) -> Optional[str]:
        """
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def metadata(self) -> Optional['_meta.v1.outputs.ObjectMeta']:
        """
        Standard object's metadata.
        """
        return pulumi.get(self, "metadata")

    @property
    @pulumi.getter
    def subjects(self) -> Optional[Sequence['outputs.Subject']]:
        """
        Subjects holds references to the objects the role applies to.
        """
        return pulumi.get(self, "subjects")


@pulumi.output_type
class PolicyRule(dict):
    """
    PolicyRule holds information that describes a policy rule, but does not contain information about who the rule applies to or which namespace the rule applies to.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "apiGroups":
            suggest = "api_groups"
        elif key == "nonResourceURLs":
            suggest = "non_resource_urls"
        elif key == "resourceNames":
            suggest = "resource_names"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in PolicyRule. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        PolicyRule.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        PolicyRule.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 verbs: Sequence[str],
                 api_groups: Optional[Sequence[str]] = None,
                 non_resource_urls: Optional[Sequence[str]] = None,
                 resource_names: Optional[Sequence[str]] = None,
                 resources: Optional[Sequence[str]] = None):
        """
        PolicyRule holds information that describes a policy rule, but does not contain information about who the rule applies to or which namespace the rule applies to.
        :param Sequence[str] verbs: Verbs is a list of Verbs that apply to ALL the ResourceKinds and AttributeRestrictions contained in this rule.  VerbAll represents all kinds.
        :param Sequence[str] api_groups: APIGroups is the name of the APIGroup that contains the resources.  If multiple API groups are specified, any action requested against one of the enumerated resources in any API group will be allowed.
        :param Sequence[str] non_resource_urls: NonResourceURLs is a set of partial urls that a user should have access to.  *s are allowed, but only as the full, final step in the path Since non-resource URLs are not namespaced, this field is only applicable for ClusterRoles referenced from a ClusterRoleBinding. Rules can either apply to API resources (such as "pods" or "secrets") or non-resource URL paths (such as "/api"),  but not both.
        :param Sequence[str] resource_names: ResourceNames is an optional white list of names that the rule applies to.  An empty set means that everything is allowed.
        :param Sequence[str] resources: Resources is a list of resources this rule applies to.  '*' represents all resources in the specified apiGroups. '*/foo' represents the subresource 'foo' for all resources in the specified apiGroups.
        """
        pulumi.set(__self__, "verbs", verbs)
        if api_groups is not None:
            pulumi.set(__self__, "api_groups", api_groups)
        if non_resource_urls is not None:
            pulumi.set(__self__, "non_resource_urls", non_resource_urls)
        if resource_names is not None:
            pulumi.set(__self__, "resource_names", resource_names)
        if resources is not None:
            pulumi.set(__self__, "resources", resources)

    @property
    @pulumi.getter
    def verbs(self) -> Sequence[str]:
        """
        Verbs is a list of Verbs that apply to ALL the ResourceKinds and AttributeRestrictions contained in this rule.  VerbAll represents all kinds.
        """
        return pulumi.get(self, "verbs")

    @property
    @pulumi.getter(name="apiGroups")
    def api_groups(self) -> Optional[Sequence[str]]:
        """
        APIGroups is the name of the APIGroup that contains the resources.  If multiple API groups are specified, any action requested against one of the enumerated resources in any API group will be allowed.
        """
        return pulumi.get(self, "api_groups")

    @property
    @pulumi.getter(name="nonResourceURLs")
    def non_resource_urls(self) -> Optional[Sequence[str]]:
        """
        NonResourceURLs is a set of partial urls that a user should have access to.  *s are allowed, but only as the full, final step in the path Since non-resource URLs are not namespaced, this field is only applicable for ClusterRoles referenced from a ClusterRoleBinding. Rules can either apply to API resources (such as "pods" or "secrets") or non-resource URL paths (such as "/api"),  but not both.
        """
        return pulumi.get(self, "non_resource_urls")

    @property
    @pulumi.getter(name="resourceNames")
    def resource_names(self) -> Optional[Sequence[str]]:
        """
        ResourceNames is an optional white list of names that the rule applies to.  An empty set means that everything is allowed.
        """
        return pulumi.get(self, "resource_names")

    @property
    @pulumi.getter
    def resources(self) -> Optional[Sequence[str]]:
        """
        Resources is a list of resources this rule applies to.  '*' represents all resources in the specified apiGroups. '*/foo' represents the subresource 'foo' for all resources in the specified apiGroups.
        """
        return pulumi.get(self, "resources")


@pulumi.output_type
class Role(dict):
    """
    Role is a namespaced, logical grouping of PolicyRules that can be referenced as a unit by a RoleBinding. Deprecated in v1.17 in favor of rbac.authorization.k8s.io/v1 Role, and will no longer be served in v1.20.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "apiVersion":
            suggest = "api_version"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in Role. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        Role.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        Role.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 api_version: Optional[str] = None,
                 kind: Optional[str] = None,
                 metadata: Optional['_meta.v1.outputs.ObjectMeta'] = None,
                 rules: Optional[Sequence['outputs.PolicyRule']] = None):
        """
        Role is a namespaced, logical grouping of PolicyRules that can be referenced as a unit by a RoleBinding. Deprecated in v1.17 in favor of rbac.authorization.k8s.io/v1 Role, and will no longer be served in v1.20.
        :param str api_version: APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
        :param str kind: Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
        :param '_meta.v1.ObjectMetaArgs' metadata: Standard object's metadata.
        :param Sequence['PolicyRuleArgs'] rules: Rules holds all the PolicyRules for this Role
        """
        if api_version is not None:
            pulumi.set(__self__, "api_version", 'rbac.authorization.k8s.io/v1beta1')
        if kind is not None:
            pulumi.set(__self__, "kind", 'Role')
        if metadata is not None:
            pulumi.set(__self__, "metadata", metadata)
        if rules is not None:
            pulumi.set(__self__, "rules", rules)

    @property
    @pulumi.getter(name="apiVersion")
    def api_version(self) -> Optional[str]:
        """
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
        """
        return pulumi.get(self, "api_version")

    @property
    @pulumi.getter
    def kind(self) -> Optional[str]:
        """
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def metadata(self) -> Optional['_meta.v1.outputs.ObjectMeta']:
        """
        Standard object's metadata.
        """
        return pulumi.get(self, "metadata")

    @property
    @pulumi.getter
    def rules(self) -> Optional[Sequence['outputs.PolicyRule']]:
        """
        Rules holds all the PolicyRules for this Role
        """
        return pulumi.get(self, "rules")


@pulumi.output_type
class RoleBinding(dict):
    """
    RoleBinding references a role, but does not contain it.  It can reference a Role in the same namespace or a ClusterRole in the global namespace. It adds who information via Subjects and namespace information by which namespace it exists in.  RoleBindings in a given namespace only have effect in that namespace. Deprecated in v1.17 in favor of rbac.authorization.k8s.io/v1 RoleBinding, and will no longer be served in v1.20.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "roleRef":
            suggest = "role_ref"
        elif key == "apiVersion":
            suggest = "api_version"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in RoleBinding. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        RoleBinding.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        RoleBinding.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 role_ref: 'outputs.RoleRef',
                 api_version: Optional[str] = None,
                 kind: Optional[str] = None,
                 metadata: Optional['_meta.v1.outputs.ObjectMeta'] = None,
                 subjects: Optional[Sequence['outputs.Subject']] = None):
        """
        RoleBinding references a role, but does not contain it.  It can reference a Role in the same namespace or a ClusterRole in the global namespace. It adds who information via Subjects and namespace information by which namespace it exists in.  RoleBindings in a given namespace only have effect in that namespace. Deprecated in v1.17 in favor of rbac.authorization.k8s.io/v1 RoleBinding, and will no longer be served in v1.20.
        :param 'RoleRefArgs' role_ref: RoleRef can reference a Role in the current namespace or a ClusterRole in the global namespace. If the RoleRef cannot be resolved, the Authorizer must return an error.
        :param str api_version: APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
        :param str kind: Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
        :param '_meta.v1.ObjectMetaArgs' metadata: Standard object's metadata.
        :param Sequence['SubjectArgs'] subjects: Subjects holds references to the objects the role applies to.
        """
        pulumi.set(__self__, "role_ref", role_ref)
        if api_version is not None:
            pulumi.set(__self__, "api_version", 'rbac.authorization.k8s.io/v1beta1')
        if kind is not None:
            pulumi.set(__self__, "kind", 'RoleBinding')
        if metadata is not None:
            pulumi.set(__self__, "metadata", metadata)
        if subjects is not None:
            pulumi.set(__self__, "subjects", subjects)

    @property
    @pulumi.getter(name="roleRef")
    def role_ref(self) -> 'outputs.RoleRef':
        """
        RoleRef can reference a Role in the current namespace or a ClusterRole in the global namespace. If the RoleRef cannot be resolved, the Authorizer must return an error.
        """
        return pulumi.get(self, "role_ref")

    @property
    @pulumi.getter(name="apiVersion")
    def api_version(self) -> Optional[str]:
        """
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
        """
        return pulumi.get(self, "api_version")

    @property
    @pulumi.getter
    def kind(self) -> Optional[str]:
        """
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def metadata(self) -> Optional['_meta.v1.outputs.ObjectMeta']:
        """
        Standard object's metadata.
        """
        return pulumi.get(self, "metadata")

    @property
    @pulumi.getter
    def subjects(self) -> Optional[Sequence['outputs.Subject']]:
        """
        Subjects holds references to the objects the role applies to.
        """
        return pulumi.get(self, "subjects")


@pulumi.output_type
class RoleRef(dict):
    """
    RoleRef contains information that points to the role being used
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "apiGroup":
            suggest = "api_group"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in RoleRef. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        RoleRef.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        RoleRef.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 api_group: str,
                 kind: str,
                 name: str):
        """
        RoleRef contains information that points to the role being used
        :param str api_group: APIGroup is the group for the resource being referenced
        :param str kind: Kind is the type of resource being referenced
        :param str name: Name is the name of resource being referenced
        """
        pulumi.set(__self__, "api_group", api_group)
        pulumi.set(__self__, "kind", kind)
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="apiGroup")
    def api_group(self) -> str:
        """
        APIGroup is the group for the resource being referenced
        """
        return pulumi.get(self, "api_group")

    @property
    @pulumi.getter
    def kind(self) -> str:
        """
        Kind is the type of resource being referenced
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name is the name of resource being referenced
        """
        return pulumi.get(self, "name")


@pulumi.output_type
class Subject(dict):
    """
    Subject contains a reference to the object or user identities a role binding applies to.  This can either hold a direct API object reference, or a value for non-objects such as user and group names.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "apiGroup":
            suggest = "api_group"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in Subject. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        Subject.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        Subject.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 kind: str,
                 name: str,
                 api_group: Optional[str] = None,
                 namespace: Optional[str] = None):
        """
        Subject contains a reference to the object or user identities a role binding applies to.  This can either hold a direct API object reference, or a value for non-objects such as user and group names.
        :param str kind: Kind of object being referenced. Values defined by this API group are "User", "Group", and "ServiceAccount". If the Authorizer does not recognized the kind value, the Authorizer should report an error.
        :param str name: Name of the object being referenced.
        :param str api_group: APIGroup holds the API group of the referenced subject. Defaults to "" for ServiceAccount subjects. Defaults to "rbac.authorization.k8s.io" for User and Group subjects.
        :param str namespace: Namespace of the referenced object.  If the object kind is non-namespace, such as "User" or "Group", and this value is not empty the Authorizer should report an error.
        """
        pulumi.set(__self__, "kind", kind)
        pulumi.set(__self__, "name", name)
        if api_group is not None:
            pulumi.set(__self__, "api_group", api_group)
        if namespace is not None:
            pulumi.set(__self__, "namespace", namespace)

    @property
    @pulumi.getter
    def kind(self) -> str:
        """
        Kind of object being referenced. Values defined by this API group are "User", "Group", and "ServiceAccount". If the Authorizer does not recognized the kind value, the Authorizer should report an error.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the object being referenced.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="apiGroup")
    def api_group(self) -> Optional[str]:
        """
        APIGroup holds the API group of the referenced subject. Defaults to "" for ServiceAccount subjects. Defaults to "rbac.authorization.k8s.io" for User and Group subjects.
        """
        return pulumi.get(self, "api_group")

    @property
    @pulumi.getter
    def namespace(self) -> Optional[str]:
        """
        Namespace of the referenced object.  If the object kind is non-namespace, such as "User" or "Group", and this value is not empty the Authorizer should report an error.
        """
        return pulumi.get(self, "namespace")


