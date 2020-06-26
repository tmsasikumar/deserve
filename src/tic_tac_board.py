class TicTacBoard():
    def __init__(self, n):
        self.size = n
        items = ["-"]*n
        self.board = [items]*n

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
        return not self.open_positions()

    def print_board(self):
        pass
