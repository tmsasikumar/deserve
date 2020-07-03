from src.Constants import BLANK


class Game():

    def __init__(self, board):
        self.tic_tac_board = board

    def getBoardSize(self):
        return self.tic_tac_board.size

    def getBoard(self):
        return self.tic_tac_board.grid

    def getGameBoard(self):
        return self.tic_tac_board

    def is_over(self):
        all_places_covered = not self.tic_tac_board.open_positions()
        return all_places_covered

    def possible_win_calc(self, order, symbol, last_position):
        symbol_counter = 0
        blank_counter = 0
        for i in range(0, self.getBoardSize()):
            temp = self.getBoard()[last_position[0]][i]
            if order == 'COLUMN':
                temp = self.getBoard()[i][last_position[1]]
            if temp == symbol:
                symbol_counter += 1
            elif temp == BLANK:
                blank_counter += 1
                win_pos = (i, last_position[1]) if order == "COLUMN" else ((last_position[0], i))
            if symbol_counter == self.getBoardSize() - 1 and blank_counter == 1:
                return win_pos
        return ()

    def possible_win_for_opponent(self, symbol, last_position):
        win_pos = ()
        # Check column for potential win
        win_pos = self.possible_win_calc("COLUMN", symbol, last_position)
        if win_pos:
            return win_pos
        # Check row for potential win
        win_pos = self.possible_win_calc("ROW", symbol, last_position)
        return win_pos

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
