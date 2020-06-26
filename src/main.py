from src.Constants import X_SYMBOL, O_SYMBOL
from src.player import Player
from src.tic_tac_board import TicTacBoard

board = TicTacBoard(3)

player1 = Player("Sasi", X_SYMBOL)
player2 = Player("Kumar", O_SYMBOL)


while not board.is_game_over():
    player1.get_next_position(board.open_positions())
    player2.get_next_position(board.open_positions())
    board.print_board()

