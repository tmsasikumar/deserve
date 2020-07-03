import random

from src.Constants import X_SYMBOL, O_SYMBOL, BLANK, X_WINS, DRAW, O_WINS, O_SYMBOL
import copy
from src.game import Game
from src.tic_tac_board import TicTacBoard
# Square definitions

class Player():
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def get_next_position(self, game, player2_symbol, player1_symbol, last_position):

        # todo Add logic to get possible win for current player
        # current_win_pos = game.possible_win_for_opponent(player2_symbol, last_position)

        # todo add diagonal case
        win_pos = game.possible_win_for_opponent(player1_symbol, last_position)
        if win_pos:
            return win_pos
        board = game.getGameBoard()
        open_positions = board.open_positions()

        for open_pos in open_positions:
            new_board = copy.deepcopy(board)
            best_position = ()
            new_board.place_position(open_pos, player2_symbol)
            current_grid = new_board.grid
            res = self.solve(current_grid, game)
            # res = self.solve([['X', 'O', 'X'], ['O', 'X', '_'], ['O', '_', 'X']])
            if player2_symbol == O_SYMBOL:
                if res == O_WINS:
                    best_position = open_pos
                    break
                elif res == DRAW:
                    best_position = open_pos
                else:
                    if not best_position:
                        best_position = open_pos
            else:
                if res == X_WINS:
                    best_position = open_pos
                    break
                elif res == DRAW:
                    best_position = open_pos
                else:
                    if not best_position:
                        best_position = open_pos
        # print(best_position)
        return best_position

    # Returns true if X's turn to move, false otherwise
    def is_X_turn(self, pos):
        x_count = 0
        for row in pos:
            x_count += row.count(X_SYMBOL)
            x_count -= row.count(O_SYMBOL)
        return x_count == 0

    def get_branches(self, pos, X_turn):
        #fills each possible empty position for the next immediate turn and returns list of grids with all options of next immediate turn
        symbol = X_SYMBOL if X_turn else O_SYMBOL
        branches = []
        for row in range(3):
            for square in range(3):
                if pos[row][square] == BLANK:
                    branches.append(copy.deepcopy(pos))
                    branches[-1][row][square] = symbol

        return branches

    def is_full(self, pos):
        for row in pos:
            if BLANK in row:
                return False
        return True

    def solve(self, pos, game):
        #check if player has won in the given position
        X_turn = self.is_X_turn(pos)

        static_eval = game.is_completed_with_win(pos)

        if static_eval != DRAW:
            return static_eval

        # Check for full board to see current position is draw
        if self.is_full(pos):
            return DRAW

        # Based on position find whose turn is next turn if x turn return true
        branches = self.get_branches(pos, X_turn)
        branch_evals = [self.solve(branch, game) for branch in branches]

        # Returning the result assuming best play
        if X_turn:
            # X options from best to worst
            if X_WINS in branch_evals:
                return X_WINS
            elif DRAW in branch_evals:
                return DRAW
            else:
                return O_WINS
        else:
            # O options from best to worst
            if O_WINS in branch_evals:
                return O_WINS
            elif DRAW in branch_evals:
                return DRAW
            else:
                return X_WINS
