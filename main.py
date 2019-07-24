from readchar import readchar
from random import randint
import ai
from tiles import *

# NEW RELEASE BRANCH
# Makes ANSI sequences work
import ctypes
kernel32 = ctypes.windll.kernel32
kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)


def clear():
    print('\x1b[2J', end='')


def generate_table(size):
    return [[EMPTY_TILE] * size for i in range(size)]


def draw_table():
    clear()
    for i in range(table_size):
        for j in range(table_size):
            print(GAME_BOARD[i][j], end=' ')
        print(end='\n')
    return()


def place_mark(x, y, mark):
    GAME_BOARD[x][y] = mark


class Player:
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark

    def make_move(self, board):
        print(f"{self.name}'s turn (1-9): ")
        c_str = readchar()
        if c_str.isdigit() and 0 < int(c_str) < 10:
            c = int(c_str)
            if board[key_map[c - 1][0]][key_map[c - 1][1]] == EMPTY_TILE:
                return key_map[c - 1][0], key_map[c - 1][1]
            else:
                print('This cell is marked. Try again')
                self.make_move(board)
        else:
            print('Invalid input. Try again')
            self.make_move(board)


def check_winner(mark):
    # Rows check
    for i in range(table_size):
        L = GAME_BOARD[i]
        if L.count(mark) == 3:
            return True
    # Columns check
    for x in range(table_size):
        L = [i[x] for i in GAME_BOARD]
        if L.count(mark) == 3:
            return True
    # \ diagonal check
    L = []
    for i in range(table_size):
        L.append(GAME_BOARD[i][i])
    if L.count(mark) == 3:
        return True
    # / diagonal check
    L = []
    for i in range(table_size):
        L.append(GAME_BOARD[2 - i][i])
    if L.count(mark) == 3:
        return True
    return False


def check_for_tie():
    for i in range(table_size):
        for j in range(table_size):
            if GAME_BOARD[i][j] == EMPTY_TILE:
                return False
    else:
        return True


table_size = 3
players = []
key_map = ((2, 0), (2, 1), (2, 2), (1, 0), (1, 1), (1, 2), (0, 0), (0, 1), (0, 2))
GAME_BOARD = generate_table(table_size)


def main():
    clear()
    print('>> T I C - T A C - T O E <<')
    name_1 = input('Player I, enter your name: ')
    players.append(Player(name_1, MARK_1))
    print('Press 1 to play vs AI, 2 to play vs Human: ')
    game_mode = readchar()
    # TODO: Add exception handler for ValueError
    if int(game_mode) == 1:
        print('Choose AI level (0-3): ')
        ai_level = readchar()
        if int(ai_level) == 0:
            players.append(ai.LevelZero(f'AI level {int(ai_level)}'))
        elif int(ai_level) == 1:
            players.append(ai.LevelOne(f'AI level {int(ai_level)}'))
        elif ai_level == '2':
            players.append(ai.LevelTwo(f'AI level {ai_level}'))
        elif ai_level == '3':
            players.append(ai.LevelThree(f'AI level {ai_level}'))

    elif int(game_mode) == 2:
        name_2 = input('Player II, enter your name: ')
        players.append(Player(name_2, MARK_2))

    draw_table()

    player_n = randint(0, 1)
    while True:
        x, y = players[player_n].make_move(GAME_BOARD)
        place_mark(x, y, players[player_n].mark)
        draw_table()
        if check_winner(players[player_n].mark):
            winner = players[player_n].name
            print(f'The winner is {winner}! One more? (Y/N): ', end='')
            break
        else:
            if check_for_tie():
                print("It's a tie! One more? (Y/N): ", end='')
                break

        if player_n == 0:
            player_n = 1
        else:
            player_n = 0
    print('Game End')


if __name__ == '__main__':
    main()
