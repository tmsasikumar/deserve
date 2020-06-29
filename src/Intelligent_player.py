import random

from src.player import Player


class IntelligentPlayer(Player):
    
    def get_next_position(self, open_positions):
        return random.choice(open_positions)

