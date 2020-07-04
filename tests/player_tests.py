import unittest

from src.game import Game
from src.player import Player
from src.tic_tac_board import TicTacBoard


class PlayerTests(unittest.TestCase):

     def test_initialize_player_with_name_symbol(self):
        player = Player("Sasi", "X")
        self.assertEqual(player.name, "Sasi")
        self.assertEqual(player.symbol, "X")


     def test_block_opponent_from_winning(self):
         player = Player("Sasi", "X")
         board = TicTacBoard(3)
         game = Game(board)
         board.place_position((1,1), "X")
         board.place_position((2,2), "O")
         board.place_position((0,1), "X")
         self.assertEqual(player.get_next_position(game, "O", "X"), (2,1))

     def test_should_take_winning_position(self):
         player = Player("Sasi", "X")
         board = TicTacBoard(3)
         game = Game(board)
         board.place_position((1,1), "X")
         board.place_position((2,2), "O")
         board.place_position((1,0), "X")
         board.place_position((1,2), "O")
         board.place_position((2,0), "X")
         self.assertEqual(player.get_next_position(game, "O", "X"), (0,2))

     def test_find_best_position_for_player(self):
         player = Player("Sasi", "X")
         board = TicTacBoard(3)
         game = Game(board)
         board.place_position((1,1), "X")
         self.assertEqual(player.get_next_position(game, "O", "X"), (2,2))
