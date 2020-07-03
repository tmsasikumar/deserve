import unittest

from src.Intelligent_player import IntelligentPlayer
from src.player import Player
from src.tic_tac_board import TicTacBoard


class IntelligentPlayerTests(unittest.TestCase):

     def test_initialize_player_with_name_symbol(self):
        player = IntelligentPlayer("Sasi", "X")
        self.assertEqual(player.name, "Sasi")
        self.assertEqual(player.symbol, "X")


     def test_if_grid_empty_place_in_center(self):
         player = IntelligentPlayer("Sasi", "X")
         board = TicTacBoard(3)
         self.assertEquals(player.get_next_position(board.grid), (1,1))



     def test_if_possibility_of_computer_win_place_in_position(self):
         player = IntelligentPlayer("Sasi", "X")
         board = TicTacBoard(3)
         board.place_position((1,1), "X")
         board.place_position((1,0), "O")
         board.place_position((0,2), "X")
         self.assertEquals(player.get_next_position(board.grid), (2,2))



     def test_block_opponent_from_winning(self):
         player = IntelligentPlayer("Sasi", "X")
         board = TicTacBoard(3)
         board.place_position((1,1), "O")
         board.place_position((2,2), "X")
         board.place_position((0,2), "O")
         self.assertEquals(player.get_next_position(board.grid), (2,0))



     def test_place_next_best_position(self):
         player = IntelligentPlayer("Sasi", "X")
         board = TicTacBoard(3)
         board.place_position((1,1), "O")
         board.place_position((2,2), "X")
         board.place_position((0,2), "O")
         self.assertEquals(player.get_next_position(board.grid), (2,0))
