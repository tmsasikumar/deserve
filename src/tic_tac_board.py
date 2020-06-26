class TicTacBoard():
    def __init__(self, n):
        self.size = n
        items = ["-"]*n
        self.board = [items]*n

    def place_position(self, position, symbol):
        if position > self.size or position < 0 or self.board[position[0]][position[1]] != "-":
            return False
        else:
           self.board[position[0]][position[1]] = symbol
           return True


    def open_positions(self):
        open_positions = []
        for i in self.size:
            for j in self.size:
                if self.board[i][j] == "-":
                    open_positions.append((i,j))
        return open_positions


