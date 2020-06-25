import unittest

from src import tic_tac_board
from src.tic_tac_board import TicTacBoard


class TicTacToeTests(unittest.TestCase):

    def should_create_an_empty_tictactoe_board(self):
        board = TicTacBoard()
        self.assertIsNotNone(board)


    def should_validate_move_position(self):
        #Todo move this to setup
        board = TicTacBoard()
        isValid = board.placePosition("X", (0,-1))
        self.assertFalse(isValid)

    def should_place_item_in_position_if_valid(self):
        board = TicTacBoard()
        isValid = board.placePosition("X", (1,1))
        self.assertTrue(isValid)


    def should_check_if_game_is_over(self):
        board = TicTacBoard
        self.assertTrue(board.isGameOver())

    def should_return_false_if_game_is_not_over(self):
        board = TicTacBoard
        self.assertFalse(board.isGameOver())
