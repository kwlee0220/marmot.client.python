# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import base_pb2 as base__pb2
import dataset_pb2 as dataset__pb2
import stream_pb2 as stream__pb2
import type_pb2 as type__pb2


class DataSetServiceStub(object):
    """Missing associated documentation comment in .proto file"""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.createDataSet = channel.unary_unary(
                '/proto.dataset.DataSetService/createDataSet',
                request_serializer=dataset__pb2.CreateDataSetRequest.SerializeToString,
                response_deserializer=dataset__pb2.DataSetInfoResponse.FromString,
                )
        self.deleteDataSet = channel.unary_unary(
                '/proto.dataset.DataSetService/deleteDataSet',
                request_serializer=base__pb2.StringProto.SerializeToString,
                response_deserializer=base__pb2.BoolResponse.FromString,
                )
        self.readDataSet = channel.stream_stream(
                '/proto.dataset.DataSetService/readDataSet',
                request_serializer=stream__pb2.UpMessage.SerializeToString,
                response_deserializer=stream__pb2.DownMessage.FromString,
                )
        self.readDataSet2 = channel.unary_stream(
                '/proto.dataset.DataSetService/readDataSet2',
                request_serializer=base__pb2.StringProto.SerializeToString,
                response_deserializer=type__pb2.RecordResponse.FromString,
                )
        self.writeDataSet = channel.stream_stream(
                '/proto.dataset.DataSetService/writeDataSet',
                request_serializer=stream__pb2.UpMessage.SerializeToString,
                response_deserializer=stream__pb2.DownMessage.FromString,
                )
        self.moveDataSet = channel.unary_unary(
                '/proto.dataset.DataSetService/moveDataSet',
                request_serializer=dataset__pb2.MoveDataSetRequest.SerializeToString,
                response_deserializer=dataset__pb2.DataSetInfoResponse.FromString,
                )
        self.getDataSetInfo = channel.unary_unary(
                '/proto.dataset.DataSetService/getDataSetInfo',
                request_serializer=base__pb2.StringProto.SerializeToString,
                response_deserializer=dataset__pb2.DataSetInfoResponse.FromString,
                )
        self.getDataSetInfoAll = channel.unary_stream(
                '/proto.dataset.DataSetService/getDataSetInfoAll',
                request_serializer=base__pb2.VoidProto.SerializeToString,
                response_deserializer=dataset__pb2.DataSetInfoResponse.FromString,
                )
        self.getDataSetInfoAllInDir = channel.unary_stream(
                '/proto.dataset.DataSetService/getDataSetInfoAllInDir',
                request_serializer=dataset__pb2.DirectoryTraverseRequest.SerializeToString,
                response_deserializer=dataset__pb2.DataSetInfoResponse.FromString,
                )
        self.updateDataSetInfo = channel.unary_unary(
                '/proto.dataset.DataSetService/updateDataSetInfo',
                request_serializer=dataset__pb2.DataSetInfoProto.SerializeToString,
                response_deserializer=dataset__pb2.DataSetInfoResponse.FromString,
                )
        self.getDirAll = channel.unary_stream(
                '/proto.dataset.DataSetService/getDirAll',
                request_serializer=base__pb2.VoidProto.SerializeToString,
                response_deserializer=base__pb2.StringResponse.FromString,
                )
        self.getSubDirAll = channel.unary_stream(
                '/proto.dataset.DataSetService/getSubDirAll',
                request_serializer=dataset__pb2.DirectoryTraverseRequest.SerializeToString,
                response_deserializer=base__pb2.StringResponse.FromString,
                )
        self.getParentDir = channel.unary_unary(
                '/proto.dataset.DataSetService/getParentDir',
                request_serializer=base__pb2.StringProto.SerializeToString,
                response_deserializer=base__pb2.StringResponse.FromString,
                )
        self.moveDir = channel.unary_unary(
                '/proto.dataset.DataSetService/moveDir',
                request_serializer=dataset__pb2.MoveDirRequest.SerializeToString,
                response_deserializer=base__pb2.VoidResponse.FromString,
                )
        self.deleteDir = channel.unary_unary(
                '/proto.dataset.DataSetService/deleteDir',
                request_serializer=base__pb2.StringProto.SerializeToString,
                response_deserializer=base__pb2.VoidResponse.FromString,
                )


class DataSetServiceServicer(object):
    """Missing associated documentation comment in .proto file"""

    def createDataSet(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def deleteDataSet(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def readDataSet(self, request_iterator, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def readDataSet2(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def writeDataSet(self, request_iterator, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def moveDataSet(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getDataSetInfo(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getDataSetInfoAll(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getDataSetInfoAllInDir(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def updateDataSetInfo(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getDirAll(self, request, context):
        """
        DataSet Directory related interface

        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getSubDirAll(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getParentDir(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def moveDir(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def deleteDir(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DataSetServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'createDataSet': grpc.unary_unary_rpc_method_handler(
                    servicer.createDataSet,
                    request_deserializer=dataset__pb2.CreateDataSetRequest.FromString,
                    response_serializer=dataset__pb2.DataSetInfoResponse.SerializeToString,
            ),
            'deleteDataSet': grpc.unary_unary_rpc_method_handler(
                    servicer.deleteDataSet,
                    request_deserializer=base__pb2.StringProto.FromString,
                    response_serializer=base__pb2.BoolResponse.SerializeToString,
            ),
            'readDataSet': grpc.stream_stream_rpc_method_handler(
                    servicer.readDataSet,
                    request_deserializer=stream__pb2.UpMessage.FromString,
                    response_serializer=stream__pb2.DownMessage.SerializeToString,
            ),
            'readDataSet2': grpc.unary_stream_rpc_method_handler(
                    servicer.readDataSet2,
                    request_deserializer=base__pb2.StringProto.FromString,
                    response_serializer=type__pb2.RecordResponse.SerializeToString,
            ),
            'writeDataSet': grpc.stream_stream_rpc_method_handler(
                    servicer.writeDataSet,
                    request_deserializer=stream__pb2.UpMessage.FromString,
                    response_serializer=stream__pb2.DownMessage.SerializeToString,
            ),
            'moveDataSet': grpc.unary_unary_rpc_method_handler(
                    servicer.moveDataSet,
                    request_deserializer=dataset__pb2.MoveDataSetRequest.FromString,
                    response_serializer=dataset__pb2.DataSetInfoResponse.SerializeToString,
            ),
            'getDataSetInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.getDataSetInfo,
                    request_deserializer=base__pb2.StringProto.FromString,
                    response_serializer=dataset__pb2.DataSetInfoResponse.SerializeToString,
            ),
            'getDataSetInfoAll': grpc.unary_stream_rpc_method_handler(
                    servicer.getDataSetInfoAll,
                    request_deserializer=base__pb2.VoidProto.FromString,
                    response_serializer=dataset__pb2.DataSetInfoResponse.SerializeToString,
            ),
            'getDataSetInfoAllInDir': grpc.unary_stream_rpc_method_handler(
                    servicer.getDataSetInfoAllInDir,
                    request_deserializer=dataset__pb2.DirectoryTraverseRequest.FromString,
                    response_serializer=dataset__pb2.DataSetInfoResponse.SerializeToString,
            ),
            'updateDataSetInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.updateDataSetInfo,
                    request_deserializer=dataset__pb2.DataSetInfoProto.FromString,
                    response_serializer=dataset__pb2.DataSetInfoResponse.SerializeToString,
            ),
            'getDirAll': grpc.unary_stream_rpc_method_handler(
                    servicer.getDirAll,
                    request_deserializer=base__pb2.VoidProto.FromString,
                    response_serializer=base__pb2.StringResponse.SerializeToString,
            ),
            'getSubDirAll': grpc.unary_stream_rpc_method_handler(
                    servicer.getSubDirAll,
                    request_deserializer=dataset__pb2.DirectoryTraverseRequest.FromString,
                    response_serializer=base__pb2.StringResponse.SerializeToString,
            ),
            'getParentDir': grpc.unary_unary_rpc_method_handler(
                    servicer.getParentDir,
                    request_deserializer=base__pb2.StringProto.FromString,
                    response_serializer=base__pb2.StringResponse.SerializeToString,
            ),
            'moveDir': grpc.unary_unary_rpc_method_handler(
                    servicer.moveDir,
                    request_deserializer=dataset__pb2.MoveDirRequest.FromString,
                    response_serializer=base__pb2.VoidResponse.SerializeToString,
            ),
            'deleteDir': grpc.unary_unary_rpc_method_handler(
                    servicer.deleteDir,
                    request_deserializer=base__pb2.StringProto.FromString,
                    response_serializer=base__pb2.VoidResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'proto.dataset.DataSetService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DataSetService(object):
    """Missing associated documentation comment in .proto file"""

    @staticmethod
    def createDataSet(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/proto.dataset.DataSetService/createDataSet',
            dataset__pb2.CreateDataSetRequest.SerializeToString,
            dataset__pb2.DataSetInfoResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def deleteDataSet(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/proto.dataset.DataSetService/deleteDataSet',
            base__pb2.StringProto.SerializeToString,
            base__pb2.BoolResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def readDataSet(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/proto.dataset.DataSetService/readDataSet',
            stream__pb2.UpMessage.SerializeToString,
            stream__pb2.DownMessage.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def readDataSet2(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/proto.dataset.DataSetService/readDataSet2',
            base__pb2.StringProto.SerializeToString,
            type__pb2.RecordResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def writeDataSet(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/proto.dataset.DataSetService/writeDataSet',
            stream__pb2.UpMessage.SerializeToString,
            stream__pb2.DownMessage.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def moveDataSet(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/proto.dataset.DataSetService/moveDataSet',
            dataset__pb2.MoveDataSetRequest.SerializeToString,
            dataset__pb2.DataSetInfoResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getDataSetInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/proto.dataset.DataSetService/getDataSetInfo',
            base__pb2.StringProto.SerializeToString,
            dataset__pb2.DataSetInfoResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getDataSetInfoAll(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/proto.dataset.DataSetService/getDataSetInfoAll',
            base__pb2.VoidProto.SerializeToString,
            dataset__pb2.DataSetInfoResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getDataSetInfoAllInDir(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/proto.dataset.DataSetService/getDataSetInfoAllInDir',
            dataset__pb2.DirectoryTraverseRequest.SerializeToString,
            dataset__pb2.DataSetInfoResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def updateDataSetInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/proto.dataset.DataSetService/updateDataSetInfo',
            dataset__pb2.DataSetInfoProto.SerializeToString,
            dataset__pb2.DataSetInfoResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getDirAll(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/proto.dataset.DataSetService/getDirAll',
            base__pb2.VoidProto.SerializeToString,
            base__pb2.StringResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getSubDirAll(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/proto.dataset.DataSetService/getSubDirAll',
            dataset__pb2.DirectoryTraverseRequest.SerializeToString,
            base__pb2.StringResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getParentDir(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/proto.dataset.DataSetService/getParentDir',
            base__pb2.StringProto.SerializeToString,
            base__pb2.StringResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def moveDir(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/proto.dataset.DataSetService/moveDir',
            dataset__pb2.MoveDirRequest.SerializeToString,
            base__pb2.VoidResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def deleteDir(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/proto.dataset.DataSetService/deleteDir',
            base__pb2.StringProto.SerializeToString,
            base__pb2.VoidResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
