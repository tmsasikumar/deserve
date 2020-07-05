import random

from src.botplayable.bot_playable import BotPlayable


# Square definitions



class BotEasyPlayable(BotPlayable):


    def make_next_move(self, game, player1_symbol, player2_symbol):
      return random.choice(game.getGameBoard().open_positions())
