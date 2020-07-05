import unittest

from src.botplayable.bot_easy_playable import BotEasyPlayable
from src.difficulty_level import Difficult_level
from src.game import Game
from src.tic_tac_board import TicTacBoard
import unittest.mock as mock


class EasyPlayableTests(unittest.TestCase):

    def choice1000(self, values):
        return (2,2)

    def test_should_move_to_random_position_without_blocking_win(self):
        board = TicTacBoard(3)
        game = Game(board, Difficult_level.EASY)
        bot_easy_playable = BotEasyPlayable()

        with mock.patch('random.choice', self.choice1000):
           self.assertEqual( bot_easy_playable.make_next_move(game, "X", "O"), (2,2))

