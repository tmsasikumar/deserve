class Game():

    def __init__(self, board):
        self.tic_tac_board = board

    def getBoardSize(self):
        return self.tic_tac_board.size

    def getBoard(self):
        return self.tic_tac_board.grid

    def is_over(self):
        all_places_covered = not self.tic_tac_board.open_positions()
        return all_places_covered

    def is_success_player(self, last_position, symbol):
        success_counter = 0
        for i in range(0, self.getBoardSize()):
            if self.getBoard()[i][last_position[1]] == symbol:
                success_counter += 1
        if success_counter == self.getBoardSize():
            return True
        success_counter = 0
        for i in range(0, self.getBoardSize()):
            if self.getBoard()[last_position[0]][i] == symbol:
                success_counter += 1
        if success_counter == self.getBoardSize():
            return True
        if self.check_straight_diagnols(symbol):
            return True
        return self.check_reverse_diagnols(symbol, self.getBoardSize()-1, -1, -1)


    def check_straight_diagnols(self, symbol):
        success_counter = 0
        for i in range(0, self.getBoardSize()):
            if self.getBoard()[i][i] == symbol:
                success_counter += 1
        if success_counter == self.getBoardSize():
            return True

    def check_reverse_diagnols(self, symbol, param, param1, param2):
        success_counter = 0
        j = self.getBoardSize()
        for i in range(0, self.getBoardSize()):
            j -= 1;
            if self.getBoard()[i][j] == symbol:
                success_counter += 1
        if success_counter == self.getBoardSize():
            return True
