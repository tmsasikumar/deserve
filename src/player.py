import random

from src.Constants import X_SYMBOL, O_SYMBOL, BLANK, X_WINS, DRAW, O_WINS, O_SYMBOL
import copy
from src.game import Game
from src.tic_tac_board import TicTacBoard
# Square definitions

"""
  1 - system makes Random moves
  2 - if there is a win for the system,it will take win , else play randomly
  3 - if there is a win for the system,it will take win. if there is a win for the player it will block. else it will play
  randomly
  4 - if there is a win for the system,it will take win. if there is a win for the player it will block.else it will create a tree 
  and find best possible move 
  5 - 4 + it should find probability value for wins 
"""

class Player():
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
