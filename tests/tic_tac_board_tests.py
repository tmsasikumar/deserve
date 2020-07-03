import unittest
from src.tic_tac_board import TicTacBoard

class TicTacToeTests(unittest.TestCase):

    def test_create_an_empty_tictactoe_board(self):
        board = TicTacBoard(3)
        self.assertIsNotNone(board)

    def test_validate_move_position(self):
        #Todo move this to setup
        board = TicTacBoard(3)
        isValid = board.place_position((0,-1), "X")
        self.assertFalse(isValid)

    def test_place_item_in_position_if_valid(self):
        board = TicTacBoard(3)
        isValid = board.place_position((1,1), "X")
        self.assertTrue(isValid)


    def test_if_item_position_in_open_position(self):
        board = TicTacBoard(3)
        self.assertTrue(board.is_position_valid((0,0)))

    def test_if_item_position_in_open_position(self):
        board = TicTacBoard(3)
        board.place_position((0,0), "X")
        self.assertFalse(board.is_position_valid((0,0)))


    def test_should_get_all_possible_combos(self):
        board = TicTacBoard(3)
        print(board.get_all_possible_combos())
