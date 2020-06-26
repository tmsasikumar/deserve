import random


class Player():
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def get_next_position(self, open_positions):
        return random.choice(open_positions)

