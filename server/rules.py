"""
Game rules for the game Rock-Paper-Scissors.
"""
from server.game_pb2 import GameResponse, Symbol


def play_rock_paper_scissors(player_one_play, player_two_play):
    """
    Simulate a Rock-Paper-Scissors game, receiving two players' plays and computing a game result.

    A player's play can be one of the following symbols as Symbol enum: rock, paper, scissors.
    The game result is according to player_one, and can be: win, loss, tie.

    Arguments:
        - player_one_play (enum): a symbol played by one player.
        - player_two_play (enum): a symbol played by a second player.

    Returns:
        - an enum with the decision for the match, from the perspective of player one.
    """
    if player_one_play == player_two_play:
        return GameResponse.Result.TIE

    if player_one_play == Symbol.ROCK and player_two_play == Symbol.SCISSORS:
        return GameResponse.Result.WIN

    if player_one_play == Symbol.PAPER and player_two_play == Symbol.ROCK:
        return GameResponse.Result.WIN

    if player_one_play == Symbol.SCISSORS and player_two_play == Symbol.PAPER:
        return GameResponse.Result.WIN

    return GameResponse.Result.LOSS
