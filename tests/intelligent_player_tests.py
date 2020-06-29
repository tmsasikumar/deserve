import unittest

from src.Intelligent_player import IntelligentPlayer
from src.player import Player
from src.tic_tac_board import TicTacBoard


class IntelligentPlayerTests(unittest.TestCase):

     def test_initialize_player_with_name_symbol(self):
        player = IntelligentPlayer("Sasi", "X")
        self.assertEqual(player.name, "Sasi")
        self.assertEqual(player.symbol, "X")


     def test_tell_right_position_for_symbol_placement(self):
         player = IntelligentPlayer("Sasi", "X")
         board = TicTacBoard(3)
         self.assertEquals(player.get_next_position(board.open_positions()), (1,1))



     def test_block_opponent_from_winning(self):
         player = IntelligentPlayer("Sasi", "X")
         board = TicTacBoard(3)
         board.place_position((1,1), "O")
         board.place_position((2,2), "X")
         board.place_position((0,2), "O")
         self.assertEquals(player.get_next_position(board.open_positions()), (2,0))
