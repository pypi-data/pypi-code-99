# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'IPSetIPAddressVersion',
    'IPSetScope',
    'LoggingConfigurationConditionActionConditionPropertiesAction',
    'LoggingConfigurationFieldToMatchJsonBodyPropertiesInvalidFallbackBehavior',
    'LoggingConfigurationFieldToMatchJsonBodyPropertiesMatchScope',
    'LoggingConfigurationFilterBehavior',
    'LoggingConfigurationFilterRequirement',
    'LoggingConfigurationLoggingFilterPropertiesDefaultBehavior',
    'RegexPatternSetScope',
    'RuleGroupBodyParsingFallbackBehavior',
    'RuleGroupForwardedIPConfigurationFallbackBehavior',
    'RuleGroupIPSetForwardedIPConfigurationFallbackBehavior',
    'RuleGroupIPSetForwardedIPConfigurationPosition',
    'RuleGroupJsonMatchScope',
    'RuleGroupLabelMatchScope',
    'RuleGroupPositionalConstraint',
    'RuleGroupRateBasedStatementAggregateKeyType',
    'RuleGroupScope',
    'RuleGroupSizeConstraintStatementComparisonOperator',
    'RuleGroupTextTransformationType',
    'WebACLBodyParsingFallbackBehavior',
    'WebACLForwardedIPConfigurationFallbackBehavior',
    'WebACLIPSetForwardedIPConfigurationFallbackBehavior',
    'WebACLIPSetForwardedIPConfigurationPosition',
    'WebACLJsonMatchScope',
    'WebACLLabelMatchScope',
    'WebACLPositionalConstraint',
    'WebACLRateBasedStatementAggregateKeyType',
    'WebACLScope',
    'WebACLSizeConstraintStatementComparisonOperator',
    'WebACLTextTransformationType',
]


class IPSetIPAddressVersion(str, Enum):
    """
    Type of addresses in the IPSet, use IPV4 for IPV4 IP addresses, IPV6 for IPV6 address.
    """
    IPV4 = "IPV4"
    IPV6 = "IPV6"


class IPSetScope(str, Enum):
    """
    Use CLOUDFRONT for CloudFront IPSet, use REGIONAL for Application Load Balancer and API Gateway.
    """
    CLOUDFRONT = "CLOUDFRONT"
    REGIONAL = "REGIONAL"


class LoggingConfigurationConditionActionConditionPropertiesAction(str, Enum):
    """
    Logic to apply to the filtering conditions. You can specify that, in order to satisfy the filter, a log must match all conditions or must match at least one condition.
    """
    ALLOW = "ALLOW"
    BLOCK = "BLOCK"
    COUNT = "COUNT"


class LoggingConfigurationFieldToMatchJsonBodyPropertiesInvalidFallbackBehavior(str, Enum):
    """
    What AWS WAF should do if it fails to completely parse the JSON body.
    """
    MATCH = "MATCH"
    NO_MATCH = "NO_MATCH"
    EVALUATE_AS_STRING = "EVALUATE_AS_STRING"


class LoggingConfigurationFieldToMatchJsonBodyPropertiesMatchScope(str, Enum):
    """
    The parts of the JSON to match against using the MatchPattern. If you specify All, AWS WAF matches against keys and values. 
    """
    ALL = "ALL"
    KEY = "KEY"
    VALUE = "VALUE"


class LoggingConfigurationFilterBehavior(str, Enum):
    """
    How to handle logs that satisfy the filter's conditions and requirement. 
    """
    KEEP = "KEEP"
    DROP = "DROP"


class LoggingConfigurationFilterRequirement(str, Enum):
    """
    Logic to apply to the filtering conditions. You can specify that, in order to satisfy the filter, a log must match all conditions or must match at least one condition.
    """
    MEETS_ALL = "MEETS_ALL"
    MEETS_ANY = "MEETS_ANY"


class LoggingConfigurationLoggingFilterPropertiesDefaultBehavior(str, Enum):
    """
    Default handling for logs that don't match any of the specified filtering conditions.
    """
    KEEP = "KEEP"
    DROP = "DROP"


class RegexPatternSetScope(str, Enum):
    """
    Use CLOUDFRONT for CloudFront RegexPatternSet, use REGIONAL for Application Load Balancer and API Gateway.
    """
    CLOUDFRONT = "CLOUDFRONT"
    REGIONAL = "REGIONAL"


class RuleGroupBodyParsingFallbackBehavior(str, Enum):
    """
    The inspection behavior to fall back to if the JSON in the request body is invalid.
    """
    MATCH = "MATCH"
    NO_MATCH = "NO_MATCH"
    EVALUATE_AS_STRING = "EVALUATE_AS_STRING"


class RuleGroupForwardedIPConfigurationFallbackBehavior(str, Enum):
    MATCH = "MATCH"
    NO_MATCH = "NO_MATCH"


class RuleGroupIPSetForwardedIPConfigurationFallbackBehavior(str, Enum):
    MATCH = "MATCH"
    NO_MATCH = "NO_MATCH"


class RuleGroupIPSetForwardedIPConfigurationPosition(str, Enum):
    FIRST = "FIRST"
    LAST = "LAST"
    ANY = "ANY"


class RuleGroupJsonMatchScope(str, Enum):
    """
    The parts of the JSON to match against using the MatchPattern.
    """
    ALL = "ALL"
    KEY = "KEY"
    VALUE = "VALUE"


class RuleGroupLabelMatchScope(str, Enum):
    LABEL = "LABEL"
    NAMESPACE = "NAMESPACE"


class RuleGroupPositionalConstraint(str, Enum):
    """
    Position of the evaluation in the FieldToMatch of request.
    """
    EXACTLY = "EXACTLY"
    STARTS_WITH = "STARTS_WITH"
    ENDS_WITH = "ENDS_WITH"
    CONTAINS = "CONTAINS"
    CONTAINS_WORD = "CONTAINS_WORD"


class RuleGroupRateBasedStatementAggregateKeyType(str, Enum):
    IP = "IP"
    FORWARDED_IP = "FORWARDED_IP"


class RuleGroupScope(str, Enum):
    """
    Use CLOUDFRONT for CloudFront RuleGroup, use REGIONAL for Application Load Balancer and API Gateway.
    """
    CLOUDFRONT = "CLOUDFRONT"
    REGIONAL = "REGIONAL"


class RuleGroupSizeConstraintStatementComparisonOperator(str, Enum):
    EQ = "EQ"
    NE = "NE"
    LE = "LE"
    LT = "LT"
    GE = "GE"
    GT = "GT"


class RuleGroupTextTransformationType(str, Enum):
    """
    Type of text transformation.
    """
    NONE = "NONE"
    COMPRESS_WHITE_SPACE = "COMPRESS_WHITE_SPACE"
    HTML_ENTITY_DECODE = "HTML_ENTITY_DECODE"
    LOWERCASE = "LOWERCASE"
    CMD_LINE = "CMD_LINE"
    URL_DECODE = "URL_DECODE"
    BASE64_DECODE = "BASE64_DECODE"
    HEX_DECODE = "HEX_DECODE"
    MD5 = "MD5"
    REPLACE_COMMENTS = "REPLACE_COMMENTS"
    ESCAPE_SEQ_DECODE = "ESCAPE_SEQ_DECODE"
    SQL_HEX_DECODE = "SQL_HEX_DECODE"
    CSS_DECODE = "CSS_DECODE"
    JS_DECODE = "JS_DECODE"
    NORMALIZE_PATH = "NORMALIZE_PATH"
    NORMALIZE_PATH_WIN = "NORMALIZE_PATH_WIN"
    REMOVE_NULLS = "REMOVE_NULLS"
    REPLACE_NULLS = "REPLACE_NULLS"
    BASE64_DECODE_EXT = "BASE64_DECODE_EXT"
    URL_DECODE_UNI = "URL_DECODE_UNI"
    UTF8_TO_UNICODE = "UTF8_TO_UNICODE"


class WebACLBodyParsingFallbackBehavior(str, Enum):
    """
    The inspection behavior to fall back to if the JSON in the request body is invalid.
    """
    MATCH = "MATCH"
    NO_MATCH = "NO_MATCH"
    EVALUATE_AS_STRING = "EVALUATE_AS_STRING"


class WebACLForwardedIPConfigurationFallbackBehavior(str, Enum):
    MATCH = "MATCH"
    NO_MATCH = "NO_MATCH"


class WebACLIPSetForwardedIPConfigurationFallbackBehavior(str, Enum):
    MATCH = "MATCH"
    NO_MATCH = "NO_MATCH"


class WebACLIPSetForwardedIPConfigurationPosition(str, Enum):
    FIRST = "FIRST"
    LAST = "LAST"
    ANY = "ANY"


class WebACLJsonMatchScope(str, Enum):
    """
    The parts of the JSON to match against using the MatchPattern.
    """
    ALL = "ALL"
    KEY = "KEY"
    VALUE = "VALUE"


class WebACLLabelMatchScope(str, Enum):
    LABEL = "LABEL"
    NAMESPACE = "NAMESPACE"


class WebACLPositionalConstraint(str, Enum):
    """
    Position of the evaluation in the FieldToMatch of request.
    """
    EXACTLY = "EXACTLY"
    STARTS_WITH = "STARTS_WITH"
    ENDS_WITH = "ENDS_WITH"
    CONTAINS = "CONTAINS"
    CONTAINS_WORD = "CONTAINS_WORD"


class WebACLRateBasedStatementAggregateKeyType(str, Enum):
    IP = "IP"
    FORWARDED_IP = "FORWARDED_IP"


class WebACLScope(str, Enum):
    """
    Use CLOUDFRONT for CloudFront WebACL, use REGIONAL for Application Load Balancer and API Gateway.
    """
    CLOUDFRONT = "CLOUDFRONT"
    REGIONAL = "REGIONAL"


class WebACLSizeConstraintStatementComparisonOperator(str, Enum):
    EQ = "EQ"
    NE = "NE"
    LE = "LE"
    LT = "LT"
    GE = "GE"
    GT = "GT"


class WebACLTextTransformationType(str, Enum):
    """
    Type of text transformation.
    """
    NONE = "NONE"
    COMPRESS_WHITE_SPACE = "COMPRESS_WHITE_SPACE"
    HTML_ENTITY_DECODE = "HTML_ENTITY_DECODE"
    LOWERCASE = "LOWERCASE"
    CMD_LINE = "CMD_LINE"
    URL_DECODE = "URL_DECODE"
    BASE64_DECODE = "BASE64_DECODE"
    HEX_DECODE = "HEX_DECODE"
    MD5 = "MD5"
    REPLACE_COMMENTS = "REPLACE_COMMENTS"
    ESCAPE_SEQ_DECODE = "ESCAPE_SEQ_DECODE"
    SQL_HEX_DECODE = "SQL_HEX_DECODE"
    CSS_DECODE = "CSS_DECODE"
    JS_DECODE = "JS_DECODE"
    NORMALIZE_PATH = "NORMALIZE_PATH"
    NORMALIZE_PATH_WIN = "NORMALIZE_PATH_WIN"
    REMOVE_NULLS = "REMOVE_NULLS"
    REPLACE_NULLS = "REPLACE_NULLS"
    BASE64_DECODE_EXT = "BASE64_DECODE_EXT"
    URL_DECODE_UNI = "URL_DECODE_UNI"
    UTF8_TO_UNICODE = "UTF8_TO_UNICODE"
