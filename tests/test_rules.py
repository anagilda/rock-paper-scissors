"""
Test suite for Rock-Paper-Scissors game rules.
"""
import unittest

from server.game_pb2 import GameResponse, Symbol
from server.rules import play_rock_paper_scissors


class RulesTest(unittest.TestCase):

    def test_tie_rock_rock(self):
        """
        When: both players play the same symbol - rock.
        Then: the result should be a tie.
        """
        result = play_rock_paper_scissors(player_one_play=Symbol.ROCK, player_two_play=Symbol.ROCK)
        self.assertEqual(GameResponse.Result.TIE, result)

    def test_tie_paper_paper(self):
        """
        When: both players play the same symbol - paper.
        Then: the result should be a tie.
        """
        result = play_rock_paper_scissors(player_one_play=Symbol.PAPER, player_two_play=Symbol.PAPER)
        self.assertEqual(GameResponse.Result.TIE, result)

    def test_tie_scissors_scissors(self):
        """
        When: both players play the same symbol - scissors.
        Then: the result should be a tie.
        """
        result = play_rock_paper_scissors(player_one_play=Symbol.SCISSORS, player_two_play=Symbol.SCISSORS)
        self.assertEqual(GameResponse.Result.TIE, result)

    def test_win_rock_scissors(self):
        """
        When: player one plays rock, and player two plays scissors.
        Then: the result should be a win - player ONE wins.
        """
        result = play_rock_paper_scissors(player_one_play=Symbol.ROCK, player_two_play=Symbol.SCISSORS)
        self.assertEqual(GameResponse.Result.WIN, result)

    def test_win_paper_rock(self):
        """
        When: player one plays paper, and player two plays rock.
        Then: the result should be a win - player ONE wins.
        """
        result = play_rock_paper_scissors(player_one_play=Symbol.PAPER, player_two_play=Symbol.ROCK)
        self.assertEqual(GameResponse.Result.WIN, result)

    def test_win_scissors_paper(self):
        """
        When: player one plays scissors, and player two plays paper.
        Then: the result should be a win - player ONE wins.
        """
        result = play_rock_paper_scissors(player_one_play=Symbol.SCISSORS, player_two_play=Symbol.PAPER)
        self.assertEqual(GameResponse.Result.WIN, result)

    def test_loss_rock_paper(self):
        """
        When: player one plays rock, and player two plays paper.
        Then: the result should be a loss - player ONE loses.
        """
        result = play_rock_paper_scissors(player_one_play=Symbol.ROCK, player_two_play=Symbol.PAPER)
        self.assertEqual(GameResponse.Result.LOSS, result)

    def test_loss_scissors_rock(self):
        """
        When: player one plays scissors, and player two plays rock.
        Then: the result should be a loss - player ONE loses.
        """
        result = play_rock_paper_scissors(player_one_play=Symbol.SCISSORS, player_two_play=Symbol.ROCK)
        self.assertEqual(GameResponse.Result.LOSS, result)

    def test_loss_paper_scissors(self):
        """
        When: player one plays paper, and player two plays scissors.
        Then: the result should be a loss - player ONE loses.
        """
        result = play_rock_paper_scissors(player_one_play=Symbol.PAPER, player_two_play=Symbol.SCISSORS)
        self.assertEqual(GameResponse.Result.LOSS, result)
