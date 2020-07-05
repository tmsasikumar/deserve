import unittest

from src.botplayable.bot_easy_playable import BotEasyPlayable
from src.botplayable.bot_hard_playable import BotHardPlayable
from src.botplayable.bot_medium_playable import BotMediumPlayable
from src.difficulty_level import Difficult_level
from src.game import Game
from src.tic_tac_board import TicTacBoard
import unittest.mock as mock


class HardPlayableTests(unittest.TestCase):

    def choice1000(self, values):
        return (0,1)


    def test_should_identify_winning_position_if_there_is_a_win(self):
        board = TicTacBoard(3)
        game = Game(board, Difficult_level.HARD)
        board.place_position((1,1), "X")
        board.place_position((2,2), "O")
        board.place_position((1,0), "X")
        board.place_position((1,2), "O")
        board.place_position((2,1), "X")
        bot_medium_playable = BotHardPlayable()

        self.assertEqual(bot_medium_playable.make_next_move(game, "X", "O"), (0,2))

    def test_should_block_opponents_win_if_opponent_has_chance_to_win(self):
        board = TicTacBoard(3)
        game = Game(board, Difficult_level.HARD)
        board.place_position((1,1), "O")
        board.place_position((2,2), "X")
        board.place_position((1,0), "O")
        board.place_position((1,2), "X")
        board.place_position((2,1), "O")
        bot_medium_playable = BotHardPlayable()

        self.assertEqual(bot_medium_playable.make_next_move(game, "O", "X"), (0,2))

    def test_should_pick_random_if_no_win_option_for_player_opponent(self):
        board = TicTacBoard(3)
        game = Game(board, Difficult_level.HARD)
        board.place_position((1,1), "X")
        board.place_position((2,2), "O")
        bot_medium_playable = BotHardPlayable()

        with mock.patch('random.choice', self.choice1000):
           self.assertEqual(bot_medium_playable.make_next_move(game, "X", "O"), (0,1))


