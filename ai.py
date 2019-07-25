from random import choice
from tiles import *
from time import sleep


class TicTacAi:
    def __init__(self, name):
        self.mark = MARK_2
        self.valid_moves = []
        self.winning_moves = []
        self.name = name

    def check_win(self, board, mark):
        self.winning_moves = []
        # Check rows
        for i in range(len(board)):
            if EMPTY_TILE in board[i] and board[i].count(mark) == 2:
                self.winning_moves.append((i, board[i].index(EMPTY_TILE)))
        # Check columns
        for i in range(len(board)):
            column = [board[j][i] for j in range(len(board))]
            if EMPTY_TILE in column and column.count(mark) == 2:
                self.winning_moves.append((column.index(EMPTY_TILE), i))
        # Check diagonals
        diag_1 = [board[i][i] for i in range(len(board))]
        diag_2 = [board[2-i][i] for i in range(len(board))]
        if EMPTY_TILE in diag_1 and diag_1.count(mark) == 2:
            self.winning_moves.append((diag_1.index(EMPTY_TILE), diag_1.index(EMPTY_TILE)))
        if EMPTY_TILE in diag_2 and diag_2.count(mark) == 2:
            self.winning_moves.append((2-diag_2.index(EMPTY_TILE), diag_2.index(EMPTY_TILE)))

    def check_threat(self, board):
        self.check_win(board, MARK_1)

    def check_for_valid_moves(self, board):
        self.valid_moves = []
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == EMPTY_TILE:
                    self.valid_moves.append((i, j))


class LevelZero(TicTacAi):
    def make_move(self, game_board):
        print('AI is thinking...')
        sleep(1)
        self.check_for_valid_moves(game_board)
        x, y = choice(self.valid_moves)
        return x, y


class LevelOne(TicTacAi):
    def make_move(self, game_board):
        print('AI is thinking...')
        sleep(1)
        self.check_win(game_board, self.mark)
        if len(self.winning_moves) > 0:
            x, y = choice(self.winning_moves)
            return x, y
        else:
            self.check_threat(game_board)
            if len(self.winning_moves) > 0:
                x, y = choice(self.winning_moves)
                return x, y
        self.check_for_valid_moves(game_board)
        x, y = choice(self.valid_moves)
        return x, y


class LevelTwo(TicTacAi):
    pass

class LevelThree(TicTacAi):

    pass
