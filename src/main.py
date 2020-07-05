from src.Botplayer import BotPlayer
from src.Constants import X_SYMBOL, O_SYMBOL, DRAW
from src.botplayable.bot_easy_playable import BotEasyPlayable
from src.botplayable.bot_hard_playable import BotHardPlayable
from src.botplayable.bot_medium_playable import BotMediumPlayable
from src.botplayable.bot_very_hard_playable import BotVeryHardPlayable
from src.difficulty_level import Difficult_level
from src.game import Game
from src.player import Player
from src.tic_tac_board import TicTacBoard

board = TicTacBoard(3)
difficulty_level = int(input("Enter difficulty level (1,2,3,4,5):"))

game = Game(board, difficulty_level)

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


def createPlayable(difficulty_level):
    if(difficulty_level == Difficult_level.EASY.value):
        return BotEasyPlayable()
    elif difficulty_level == Difficult_level.MEDIUM.value:
        return BotMediumPlayable()
    elif difficulty_level == Difficult_level.HARD.value:
        return BotHardPlayable()
    elif difficulty_level == Difficult_level.VERY_HARD.value:
        return BotVeryHardPlayable()


player2 = BotPlayer(player2_name, player2_symbol, createPlayable(difficulty_level))

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
    return position


while True:
    last_position = manual_player_choose_input(player1_name, player1_symbol)
    if game.is_completed_with_win(game.getBoard()) != DRAW:
        print("%s wins" %(player1_name))
        break
    if game.is_over():
        print("It is a tie")
        break

    computer_next_position = player2.get_next_position(game,player2_symbol, player1_symbol)
    board.place_position(computer_next_position, player2_symbol)
    board.print_board()
    if game.is_completed_with_win(game.getBoard()) != DRAW:
        print("%s wins" %(player2_name))
        break
    if game.is_over():
        print("It is a tie")
        break
