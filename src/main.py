from src.player import Player
from src.tic_tac_board import TicTacBoard

board = TicTacBoard(3)

player1 = Player("Sasi", "X")
player2 = Player("Kumar", "O")


while not board.is_game_over():
    player1.get_next_position(board.open_positions())
    player2.get_next_position(board.open_positions())
    board.print_board()

