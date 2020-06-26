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
    #
    # def test_check_if_game_is_over(self):
    #     board = TicTacBoard(3)
    #     self.assertTrue(board.is_game_over(position, X_SYMBOL))
    #
    # def test_return_false_if_game_is_not_over(self):
    #     board = TicTacBoard(3)
    #     self.assertFalse(board.is_game_over(position, X_SYMBOL))


    # def test_return_open_positions_for_game(self):
    #     board = TicTacBoard(3)
    #     self.assertEqual(board.open_positions(), [(1,1), (2,2)])


    def test_game_over_if_diagnol_continous_block(self):
        board = TicTacBoard(3)
        board.place_position((0,0), "X")
        board.place_position((1,1), "X")
        board.place_position((2,2), "X")
        self.assertTrue(board.is_success_player((2, 2), "X"))

    def test_game_over_if_reverse_diagnol_continous_block(self):
        board = TicTacBoard(3)
        board.place_position((1,1), "X")
        board.place_position((0,2), "X")
        board.place_position((2,0), "X")
        self.assertTrue(board.is_success_player((2, 0), "X"))

    def test_game_over_if_straight_continous_blocks(self):
        board = TicTacBoard(3)
        board.place_position((0,0), "O")
        board.place_position((1,0), "O")
        board.place_position((2,0), "O")
        self.assertTrue(board.is_success_player((2,0), "O"))

    def test_game_over_if_straight_continous_blocks(self):
        board = TicTacBoard(3)
        board.place_position((0,0), "O")
        board.place_position((0,1), "O")
        board.place_position((0,2), "O")
        self.assertTrue(board.is_success_player((0,1), "O"))



    def test_game_failure_if_straight_continous_blocks(self):
        board = TicTacBoard(3)
        board.place_position((0,0), "O")
        board.place_position((0,1), "X")
        board.place_position((0,2), "O")
        self.assertFalse(board.is_success_player((0,2), "O"))
