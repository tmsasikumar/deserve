import itertools

class TicTacBoard():
    def __init__(self, n):
        self.size = n
        temp = itertools.count(1)
        self.grid= [["-" for i in range(n)] for i in range(n)]

    def place_position(self, position, symbol):
        is_outside = position[0] > self.size or position[0] < 0 or position[1] > self.size or position[1] < 0
        if is_outside or self.grid[position[0]][position[1]] != "-":
            return False
        else:
           self.grid[position[0]][position[1]] = symbol
           return True

    def open_positions(self):
        open_positions = []
        for i in range(0, self.size):
            for j in range(0, self.size):
                if self.grid[i][j] == "-":
                    open_positions.append((i,j))
        return open_positions

    def is_position_valid(self, position):
        return position in self.open_positions()

    def print_board(self):
        print("printing board")
        for i in range(0, self.size):
            for j in range(0, self.size):
                 print(self.grid[i][j], end ="|")
            print("")
            print("_______")


    def get_all_possible_combos(self):
        positions = []
        positions.append(self.getLinearPositions(positions))
        return  positions

    def getHorizontalPositions(self, positions):
        for i in range(0, self.size):
            position = []
            for j in range(0, self.size):
                position.append((i, j))
            positions.append(position)


    def getLinearPositions(self, positions):
        for i in range(0, self.size):
            position = []
            for j in range(0, self.size):
                position.append((j, i))
            positions.append(position)
