# import logging
# import logging.config
import time
from concurrent import futures

import grpc

from server.game_pb2_grpc import add_RockPaperScissorsServicer_to_server, RockPaperScissorsServicer
from server.game_pb2 import GameResponse, Symbol
from server.config.config import MAX_WORKERS, SERVER_ADDRESS, ONE_DAY_IN_SECONDS


class RockPaperScissorsServicer(RockPaperScissorsServicer):

    def Game(self, request, context):
        try:
            enemy_play = Symbol.ROCK
            if request.play == enemy_play:
                result = GameResponse.Result.TIE
            elif (
                    request.play == Symbol.ROCK and enemy_play == Symbol.SCISSORS
                    or request.play == Symbol.PAPER and enemy_play == Symbol.ROCK
                    or request.play == Symbol.SCISSORS and enemy_play == Symbol.PAPER
            ):
                result = GameResponse.Results.WIN
            else:
                result = GameResponse.Results.LOSS

            return GameResponse(enemy_play=enemy_play, result=result)

        except ValueError as e:
            context.set_details(str(e))
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            # logging.error('Exception occurred', exc_info=True)


def serve():
    # logging.config.fileConfig(f'{Config.ROOT_DIR}/casafari/lib/logging.conf')
    # logging.info('Server is starting.')

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=MAX_WORKERS))
    add_RockPaperScissorsServicer_to_server(RockPaperScissorsServicer(), server)
    server.add_insecure_port(SERVER_ADDRESS)
    server.start()

    # logging.info('Server is running...')

    try:
        while True:
            time.sleep(ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        # logging.error('Server was manually stopped.')
        server.stop(grace=None)


if __name__ == '__main__':
    serve()
