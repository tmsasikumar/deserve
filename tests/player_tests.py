import unittest

from src.game import Game
from src.player import Player
from src.tic_tac_board import TicTacBoard


class PlayerTests(unittest.TestCase):

     def test_initialize_player_with_name_symbol(self):
        player = Player("Sasi", "X")
        self.assertEqual(player.name, "Sasi")
        self.assertEqual(player.symbol, "X")

