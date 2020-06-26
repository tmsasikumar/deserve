from src.Constants import X_SYMBOL, O_SYMBOL
from src.player import Player
from src.tic_tac_board import TicTacBoard

board = TicTacBoard(3)

player1_name = input("Enter the player1 name:")
player1_symbol = input("Enter the player1 symbol:")

player2_name = input("Enter the player2 name:")
player2_symbol = input("Enter the player2 symbol:")

if player2_symbol == player1_symbol:
    print(player2_symbol+" is Already used")
    player2_symbol = O_SYMBOL if player1_symbol == X_SYMBOL else X_SYMBOL
    print("Hence allocating - " + player2_symbol)


player1 = Player(player1_name, player1_symbol)
player2 = Player(player2_name, player2_symbol)


while not board.is_game_over():
    position = player1.get_next_position(board.open_positions())
    board.place_position(position, player1_symbol)
    if board.is_game_over():
        break
    position = player2.get_next_position(board.open_positions())
    board.place_position(position, player2_symbol)
    board.print_board()
