import datetime
import unittest

import grpc_testing

from server import game_pb2
from server.main import RockPaperScissorsServicer


class BaseTest(unittest.TestCase):

    def setUp(self):
        self._service = game_pb2.DESCRIPTOR.services_by_name['RockPaperScissors']
        test_time = grpc_testing.strict_fake_time(datetime.datetime.utcnow())
        self._test_server = grpc_testing.server_from_dictionary(
            descriptors_to_servicers={self._service: RockPaperScissorsServicer}, time=test_time,
        )

    def _call_rpc(self, name, request):
        rpc = self._test_server.invoke_unary_unary(
            method_descriptor=self._service.methods_by_name[name],
            invocation_metadata={},
            request=request,
            timeout=None,
        )
        response, _, code, details = rpc.termination()
        return response, code, details

    def Game(self, request):
        return self._call_rpc('Game', request)
