import unittest
from src.player import Player
from src.tic_tac_board import TicTacBoard


class PlayerTests(unittest.TestCase):

     def test_initialize_player_with_name_symbol(self):
        player = Player("Sasi", "X")
        self.assertEqual(player.name, "Sasi")
        self.assertEqual(player.symbol, "X")


     def test_tell_a_position_for_symbol_placement(self):
         player = Player("Sasi", "X")
         board = TicTacBoard(3)
         self.assertIsNotNone(player.get_next_position(board.open_positions()))
