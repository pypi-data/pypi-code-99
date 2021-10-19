# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from evmosproto.cosmos.authz.v1beta1 import tx_pb2 as cosmos_dot_authz_dot_v1beta1_dot_tx__pb2


class MsgStub(object):
    """Msg defines the authz Msg service.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Grant = channel.unary_unary(
                '/cosmos.authz.v1beta1.Msg/Grant',
                request_serializer=cosmos_dot_authz_dot_v1beta1_dot_tx__pb2.MsgGrant.SerializeToString,
                response_deserializer=cosmos_dot_authz_dot_v1beta1_dot_tx__pb2.MsgGrantResponse.FromString,
                )
        self.Exec = channel.unary_unary(
                '/cosmos.authz.v1beta1.Msg/Exec',
                request_serializer=cosmos_dot_authz_dot_v1beta1_dot_tx__pb2.MsgExec.SerializeToString,
                response_deserializer=cosmos_dot_authz_dot_v1beta1_dot_tx__pb2.MsgExecResponse.FromString,
                )
        self.Revoke = channel.unary_unary(
                '/cosmos.authz.v1beta1.Msg/Revoke',
                request_serializer=cosmos_dot_authz_dot_v1beta1_dot_tx__pb2.MsgRevoke.SerializeToString,
                response_deserializer=cosmos_dot_authz_dot_v1beta1_dot_tx__pb2.MsgRevokeResponse.FromString,
                )


class MsgServicer(object):
    """Msg defines the authz Msg service.
    """

    def Grant(self, request, context):
        """Grant grants the provided authorization to the grantee on the granter's
        account with the provided expiration time. If there is already a grant
        for the given (granter, grantee, Authorization) triple, then the grant
        will be overwritten.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Exec(self, request, context):
        """Exec attempts to execute the provided messages using
        authorizations granted to the grantee. Each message should have only
        one signer corresponding to the granter of the authorization.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Revoke(self, request, context):
        """Revoke revokes any authorization corresponding to the provided method name on the
        granter's account that has been granted to the grantee.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MsgServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Grant': grpc.unary_unary_rpc_method_handler(
                    servicer.Grant,
                    request_deserializer=cosmos_dot_authz_dot_v1beta1_dot_tx__pb2.MsgGrant.FromString,
                    response_serializer=cosmos_dot_authz_dot_v1beta1_dot_tx__pb2.MsgGrantResponse.SerializeToString,
            ),
            'Exec': grpc.unary_unary_rpc_method_handler(
                    servicer.Exec,
                    request_deserializer=cosmos_dot_authz_dot_v1beta1_dot_tx__pb2.MsgExec.FromString,
                    response_serializer=cosmos_dot_authz_dot_v1beta1_dot_tx__pb2.MsgExecResponse.SerializeToString,
            ),
            'Revoke': grpc.unary_unary_rpc_method_handler(
                    servicer.Revoke,
                    request_deserializer=cosmos_dot_authz_dot_v1beta1_dot_tx__pb2.MsgRevoke.FromString,
                    response_serializer=cosmos_dot_authz_dot_v1beta1_dot_tx__pb2.MsgRevokeResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'cosmos.authz.v1beta1.Msg', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Msg(object):
    """Msg defines the authz Msg service.
    """

    @staticmethod
    def Grant(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.authz.v1beta1.Msg/Grant',
            cosmos_dot_authz_dot_v1beta1_dot_tx__pb2.MsgGrant.SerializeToString,
            cosmos_dot_authz_dot_v1beta1_dot_tx__pb2.MsgGrantResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Exec(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.authz.v1beta1.Msg/Exec',
            cosmos_dot_authz_dot_v1beta1_dot_tx__pb2.MsgExec.SerializeToString,
            cosmos_dot_authz_dot_v1beta1_dot_tx__pb2.MsgExecResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Revoke(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.authz.v1beta1.Msg/Revoke',
            cosmos_dot_authz_dot_v1beta1_dot_tx__pb2.MsgRevoke.SerializeToString,
            cosmos_dot_authz_dot_v1beta1_dot_tx__pb2.MsgRevokeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
