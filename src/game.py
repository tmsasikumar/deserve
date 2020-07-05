from src.Constants import BLANK, X_SYMBOL, X_WINS, O_SYMBOL, O_WINS, DRAW, LEFT, RIGHT, COLUMN, ROW


class Game():

    def __init__(self, board, difficulty_level):
        self.tic_tac_board = board
        self.difficulty_level = difficulty_level

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
                temp = self.getBoard()[row][col] if order == COLUMN else self.getBoard()[col][row]
                if temp == symbol:
                    symbol_counter += 1
                elif temp == BLANK:
                    blank_counter += 1
                    win_pos = (row, col) if order == COLUMN else (col, row)
                if symbol_counter == self.getBoardSize() - 1 and blank_counter == 1:
                    return win_pos
        return ()

    def possible_win_for_player(self, symbol):
        win_pos = ()
        # Check column for potential win
        functions_to_validate = [self.possible_win_calc(COLUMN, symbol), self.possible_win_calc(ROW, symbol),
                                 self.possible_win_calc_diagonal(LEFT, symbol),self.possible_win_calc_diagonal(RIGHT, symbol) ]

        for func in functions_to_validate:
            win_pos = func
            if win_pos:
                return  win_pos
        return win_pos

    def is_completed_with_win(self, pos):
        potential_wins = []
        # Three in a row
        for row in pos:
            potential_wins.append(set(row))
        # Three in a column
        for i in range(self.getBoardSize()):
            potential_wins.append(set([pos[k][i] for k in range(self.getBoardSize())]))
        # Three in a diagonal
        potential_wins.append(set([pos[i][i] for i in range(self.getBoardSize())]))
        potential_wins.append(set([pos[i][self.getBoardSize()-1 - i] for i in range(self.getBoardSize())]))

        # Checking if any three are the same
        for trio in potential_wins:
            if trio == set([X_SYMBOL]):
                return X_WINS
            elif trio == set([O_SYMBOL]):
                return O_WINS
        return DRAW

    def possible_win_calc_diagonal(self, order, symbol):
        symbol_counter = 0
        blank_counter = 0
        for i in range(0, self.getBoardSize()):
            temp = self.getBoard()[i][i] if order == LEFT else self.getBoard()[i][self.getBoardSize() -1 -i]
            if temp == symbol:
                symbol_counter += 1
            elif temp == BLANK:
                blank_counter += 1
                win_pos = (i,i) if order == LEFT else (i, self.getBoardSize() -1 -i)
            if symbol_counter == self.getBoardSize() -1 and blank_counter == 1:
                return win_pos

        return ()

