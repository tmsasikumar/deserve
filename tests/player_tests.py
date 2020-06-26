import unittest
from src.player import Player

class PlayerTests(unittest.TestCase):
     def should_initialize_player_with_name_symbol(self):
        player = Player("Sasi", "X")
        self.assertEquals(player.name, "Sasi")
        self.assertEquals(player.symbol, "X")


     def should_tell_a_position_for_symbol_placement(self):
         player = Player("Sasi", "X")
         self.assertEquals(player.getNextPosition(), (2,3))
