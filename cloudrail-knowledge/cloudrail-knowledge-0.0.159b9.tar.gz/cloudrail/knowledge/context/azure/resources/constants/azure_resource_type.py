from enum import Enum


class AzureResourceType(Enum):
    NONE = 'none'
    AZURERM_RESOURCE_GROUP = 'azurerm_resource_group'
    AZURERM_SQL_SERVER = 'azurerm_sql_server'
    AZURERM_POSTGRESQL_SERVER = 'azurerm_postgresql_server'
    AZURERM_MYSQL_SERVER = 'azurerm_mysql_server'
    AZURERM_MSSQL_SERVER = 'azurerm_mssql_server'
    AZURERM_SQL_FIREWALL_RULE = 'azurerm_sql_firewall_rule'
    AZURERM_APP_SERVICE = 'azurerm_app_service'
    AZURERM_NETWORK_SECURITY_GROUP = 'azurerm_network_security_group'
    AZURERM_SUBNET_NETWORK_SECURITY_GROUP_ASSOCIATION = 'azurerm_subnet_network_security_group_association'
    AZURERM_NETWORK_INTERFACE_SECURITY_GROUP_ASSOCIATION = 'azurerm_network_interface_security_group_association'
    AZURERM_SUBNET = 'azurerm_subnet'
    AZURERM_NETWORK_INTERFACE = 'azurerm_network_interface'
    AZURERM_FUNCTION_APP = 'azurerm_function_app'
    AZURERM_SECURITY_CENTER_AUTO_PROVISIONING = 'azurerm_security_center_auto_provisioning'
    AZURERM_SECURITY_CENTER_CONTACT = 'azurerm_security_center_contact'
    AZURERM_VIRTUAL_NETWORK_GATEWAY = 'azurerm_virtual_network_gateway'
    AZURERM_KEY_VAULT = 'azurerm_key_vault'
    AZURERM_MONITOR_DIAGNOSTIC_SETTING = 'azurerm_monitor_diagnostic_setting'
    AZURERM_SECURITY_CENTER_SUBSCRIPTION_PRICING = 'azurerm_security_center_subscription_pricing'
    AZURERM_MSSQL_SERVER_EXTENDED_AUDITING_POLICY = 'azurerm_mssql_server_extended_auditing_policy'
    AZURERM_STORAGE_ACCOUNT = 'azurerm_storage_account'
    AZURERM_STORAGE_ACCOUNT_NETWORK_RULES = 'azurerm_storage_account_network_rules'
    AZURERM_PUBLIC_IP = 'azurerm_public_ip'
    AZURERM_VIRTUAL_MACHINE = 'azurerm_virtual_machine'
    AZURERM_LINUX_VIRTUAL_MACHINE = 'azurerm_linux_virtual_machine'
    AZURERM_WINDOWS_VIRTUAL_MACHINE = 'azurerm_windows_virtual_machine'
    AZURERM_NETWORK_SECURITY_RULE = 'azurerm_network_security_rule'
    AZURERM_APPLICATION_SECURITY_GROUP = 'azurerm_application_security_group'
    AZURERM_NETWORK_INTERFACE_APPLICATION_SECURITY_GROUP_ASSOCIATION = 'azurerm_network_interface_application_security_group_association'
    AZURERM_KUBERNETES_CLUSTER = 'azurerm_kubernetes_cluster'
    AZURERM_MANAGED_DISK = 'azurerm_managed_disk'
    AZURERM_VIRTUAL_MACHINE_SCALE_SET = 'azurerm_virtual_machine_scale_set'
    AZURERM_LINUX_VIRTUAL_MACHINE_SCALE_SET = 'azurerm_linux_virtual_machine_scale_set'
    AZURERM_WINDOWS_VIRTUAL_MACHINE_SCALE_SET = 'azurerm_windows_virtual_machine_scale_set'
    AZURERM_COSMOSDB_ACCOUNT = 'azurerm_cosmosdb_account'
