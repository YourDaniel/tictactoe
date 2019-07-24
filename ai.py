from random import choice
from tiles import *
from time import sleep

class TicTacAi:
    def __init__(self, go_first, name):
        self.go_first = go_first
        assert go_first in [True, False]
        if go_first:
            self.mark = MARK_1
        else:
            self.mark = MARK_2
        self.valid_moves = []
        self.name = name

    def check_win(self):
        pass

    def check_threat(self):
        pass

    def check_for_valid_moves(self, board):
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == EMPTY_TILE:
                    self.valid_moves.append((i, j))


class LevelZero(TicTacAi):
    def make_move(self, game_board):
        sleep(1)
        self.valid_moves = []
        self.check_for_valid_moves(game_board)
        x, y = choice(self.valid_moves)
        return x, y

class LevelOne(TicTacAi):
    pass
class LevelTwo(TicTacAi):
    pass
class LevelThree(TicTacAi):
    pass
