from src.Constants import BLANK, X_SYMBOL, X_WINS, O_SYMBOL, O_WINS, DRAW


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

    def possible_win_calc(self, order, symbol):

        for row in range(0, self.getBoardSize()):
            symbol_counter = 0
            blank_counter = 0
            for col in range(0, self.getBoardSize()):
                temp = self.getBoard()[row][col] if order == "COLUMN" else self.getBoard()[col][row]
                if temp == symbol:
                    symbol_counter += 1
                elif temp == BLANK:
                    blank_counter += 1
                    win_pos = (row, col) if order == "COLUMN" else (col, row)
                if symbol_counter == self.getBoardSize() - 1 and blank_counter == 1:
                    return win_pos
        return ()

    def possible_win_for_opponent(self, symbol):
        win_pos = ()
        # Check column for potential win
        win_pos = self.possible_win_calc("COLUMN", symbol)
        if win_pos:
            return win_pos
        # Check row for potential win
        win_pos = self.possible_win_calc("ROW", symbol)
        return win_pos

    def is_completed_with_win(self, pos):
        potential_wins = []
        # Three in a row
        for row in pos:
            potential_wins.append(set(row))
        # Three in a column
        for i in range(3):
            potential_wins.append(set([pos[k][i] for k in range(3)]))
        # Three in a diagonal
        potential_wins.append(set([pos[i][i] for i in range(3)]))
        potential_wins.append(set([pos[i][2 - i] for i in range(3)]))

        # Checking if any three are the same
        for trio in potential_wins:
            if trio == set([X_SYMBOL]):
                return X_WINS
            elif trio == set([O_SYMBOL]):
                return O_WINS
        return DRAW
