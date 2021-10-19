from cloudrail.knowledge.context.aws.resources_builders.scanner.base_aws_scanner_builder import BaseAwsScannerBuilder
from cloudrail.knowledge.context.aws.resources_builders.scanner.cloud_mapper_component_builder import build_internet_gateway
from cloudrail.knowledge.context.aws.resources.ec2.igw_type import IgwType


class EgressOnlyInternetGatewayBuilder(BaseAwsScannerBuilder):

    def get_file_name(self) -> str:
        return 'ec2-describe-egress-only-internet-gateways.json'

    def get_section_name(self) -> str:
        return 'EgressOnlyInternetGateways'

    def do_build(self, attributes: dict):
        return build_internet_gateway(attributes, IgwType.EGRESS_ONLY_IGW, "EgressOnlyInternetGatewayId")
