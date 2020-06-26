from src.Constants import X_SYMBOL, O_SYMBOL
from src.game import Game
from src.player import Player
from src.tic_tac_board import TicTacBoard

board = TicTacBoard(3)
game = Game(board)

player1_name = input("Enter player1 name:")
player1_symbol = input("Enter player1 symbol:")

if not player1_symbol.strip():
    player1_symbol = X_SYMBOL

player2_name = "Computer"
player2_symbol = O_SYMBOL

if player2_symbol == player1_symbol:
    print(player2_symbol+" is already used")
    player2_symbol = O_SYMBOL if player1_symbol == X_SYMBOL else X_SYMBOL
    print("Hence allocating - " + player2_symbol)


player1 = Player(player1_name, player1_symbol)
player2 = Player(player2_name, player2_symbol)


board.print_board()


def manual_player_choose_input(player_name, player_symbol):
    global input_position, position
    while True:
        input_position = input("Enter %s's position as X,Y coordinates (e.g 2,2) :" % (player_name))
        position = tuple(int(x) for x in input_position.split(','))
        if board.is_position_valid(position):
            break
    board.place_position(position, player_symbol)
    board.print_board()


while True:
    manual_player_choose_input(player1_name, player1_symbol)
    if game.is_success_player(position, player1_symbol):
        print("%s wins" %(player1_name))
        break
    if game.is_over():
        print("It is a tie")
        break

    computer_next_position = player2.get_next_position(board.open_positions())
    board.place_position(computer_next_position, player2_symbol)
    board.print_board()
    if game.is_success_player(position, player2_symbol):
        print("%s wins" %(player2_name))
        break
    if game.is_over():
        print("It is a tie")
        break
