import itertools

class TicTacBoard():
    def __init__(self, n):
        self.size = n
        temp = itertools.count(1)
        self.board= [["-" for i in range(n)] for i in range(n)]

    def place_position(self, position, symbol):
        is_outside = position[0] > self.size or position[0] < 0 or position[1] > self.size or position[1] < 0
        if is_outside or self.board[position[0]][position[1]] != "-":
            return False
        else:
           self.board[position[0]][position[1]] = symbol
           return True


    def open_positions(self):
        open_positions = []
        for i in range(0, self.size):
            for j in range(0, self.size):
                if self.board[i][j] == "-":
                    open_positions.append((i,j))
        return open_positions

    def is_game_over(self):
        self.is_success_player()
        all_places_covered = not self.open_positions()
        return all_places_covered

    def print_board(self):
        print("printing board")
        for i in range(0, self.size):
            for j in range(0, self.size):
                 print(self.board[i][j], end ="|")
            print("")
            print("_______")

    def is_success_player(self):
        pass
