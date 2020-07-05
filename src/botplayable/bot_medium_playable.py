import random

from src.botplayable.bot_playable import BotPlayable


# Square definitions



class BotMediumPlayable(BotPlayable):


    def make_next_move(self, game, player1_symbol, player2_symbol):


      current_win_pos = game.possible_win_for_player(player2_symbol)
      if current_win_pos:
          return current_win_pos

      return random.choice(game.getGameBoard().open_positions())
