import unittest

from src.botplayable.bot_easy_playable import BotEasyPlayable
from src.botplayable.bot_medium_playable import BotMediumPlayable
from src.difficulty_level import Difficult_level
from src.game import Game
from src.tic_tac_board import TicTacBoard
import unittest.mock as mock


class MediumPlayableTests(unittest.TestCase):

    def choice1000(self, values):
        return (0,1)


    def test_should_identify_winning_position_if_there_is_a_win(self):
        board = TicTacBoard(3)
        game = Game(board, Difficult_level.MEDIUM)
        board.place_position((1,1), "X")
        board.place_position((2,2), "O")
        board.place_position((1,0), "X")
        board.place_position((1,2), "O")
        board.place_position((2,1), "X")
        bot_medium_playable = BotMediumPlayable()

        self.assertEqual(bot_medium_playable.make_next_move(game, "X", "O"), (0,2))

    def test_should_pick_random_if(self):
        board = TicTacBoard(3)
        game = Game(board, Difficult_level.MEDIUM)
        board.place_position((1,1), "X")
        board.place_position((2,2), "O")
        board.place_position((1,0), "X")
        board.place_position((0,0), "O")
        board.place_position((2,1), "X")
        bot_medium_playable = BotMediumPlayable()

        with mock.patch('random.choice', self.choice1000):
           self.assertEqual(bot_medium_playable.make_next_move(game, "X", "O"), (0,1))


