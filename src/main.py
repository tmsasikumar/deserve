from src.Constants import X_SYMBOL, O_SYMBOL
from src.player import Player
from src.tic_tac_board import TicTacBoard

board = TicTacBoard(3)

player1_name = input("Enter player1 name:")
player1_symbol = input("Enter player1 symbol:")

player2_name = input("Enter player2 name:")
player2_symbol = input("Enter player2 symbol:")

if player2_symbol == player1_symbol:
    print(player2_symbol+" is already used")
    player2_symbol = O_SYMBOL if player1_symbol == X_SYMBOL else X_SYMBOL
    print("Hence allocating - " + player2_symbol)


player1 = Player(player1_name, player1_symbol)
player2 = Player(player2_name, player2_symbol)


board.print_board()
while True:
    while True:
        input_position = input("Enter %s's position as X,Y coordinates (e.g 2,2) :" %(player1_name))
        position = tuple(int(x) for x in input_position.split(','))
        if board.is_position_valid(position):
            break
    # position = player1.get_next_position(board.open_positions())
    board.place_position(position, player1_symbol)
    board.print_board()
    if board.is_success_player(position, player1_symbol):
        print("%s wins" %(player1_name))
        break
    if board.is_game_over():
        print("It is a tie")
        break

    while True:
        input_position = input("Enter %s's position as X,Y coordinates (e.g 2,2) :" %(player2_name))
        position = tuple(int(x) for x in input_position.split(','))
        if board.is_position_valid(position):
            break

    board.place_position(position, player2_symbol)
    board.print_board()
    if board.is_success_player(position, player2_symbol):
        print("%s wins" %(player2_name))
        break
    if board.is_game_over():
        print("It is a tie")
        break
