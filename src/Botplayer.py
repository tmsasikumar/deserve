import random

from src.Constants import X_SYMBOL, O_SYMBOL, BLANK, X_WINS, DRAW, O_WINS, O_SYMBOL
import copy
from src.game import Game
from src.tic_tac_board import TicTacBoard
# Square definitions


class BotPlayer():
    def __init__(self, name, symbol, playable):
        self.name = name
        self.symbol = symbol
        self.playable = playable

    def get_next_position(self, game, player2_symbol, player1_symbol):

        return self.playable.make_next_move(game, player2_symbol, player1_symbol)
