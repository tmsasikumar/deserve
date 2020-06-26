import unittest

from src.Constants import X_SYMBOL
from src.game import Game
from src.tic_tac_board import TicTacBoard

class GameTests(unittest.TestCase):

    def test_check_if_game_is_over(self):
        board = TicTacBoard(3)
        game = Game(board)
        self.assertFalse(game.is_over())

    def test_game_over_if_diagnol_continous_block(self):
        board = TicTacBoard(3)
        game = Game(board)
        board.place_position((0,0), "X")
        board.place_position((1,1), "X")
        board.place_position((2,2), "X")
        self.assertTrue(game.is_success_player((2, 2), "X"))

    def test_game_over_if_reverse_diagnol_continous_block(self):
        board = TicTacBoard(3)
        game = Game(board)
        board.place_position((1,1), "X")
        board.place_position((0,2), "X")
        board.place_position((2,0), "X")
        self.assertTrue(game.is_success_player((2, 0), "X"))

    def test_game_over_if_straight_continous_blocks(self):
        board = TicTacBoard(3)
        game = Game(board)
        board.place_position((0,0), "O")
        board.place_position((1,0), "O")
        board.place_position((2,0), "O")
        self.assertTrue(game.is_success_player((2,0), "O"))

    def test_game_over_if_straight_continous_blocks(self):
        board = TicTacBoard(3)
        game = Game(board)
        board.place_position((0,0), "O")
        board.place_position((0,1), "O")
        board.place_position((0,2), "O")
        self.assertTrue(game.is_success_player((0,1), "O"))



    def test_game_failure_if_straight_continous_blocks(self):
        board = TicTacBoard(3)
        game = Game(board)
        board.place_position((0,0), "O")
        board.place_position((0,1), "X")
        board.place_position((0,2), "O")
        self.assertFalse(game.is_success_player((0,2), "O"))

if __name__ == "__main__":
    unittest.main()
