# Functionality
import os
from readchar import readchar

'''
class Player:
    pass


class GameBoard:
    def __init__(self, ):
        self.board = []

    def draw(self):
        pass
'''

def clear():
    os.system('cls')


def generate_table(size):
    return [[tile for i in range(size)] for j in range(size)]


def draw_table():
    clear()
    for i in range(tableSize):
        for j in range(tableSize):
            print(A[i][j], end=' ')
        print(end='\n')
    return()


def draw_game_log():
    for line in game_log:
        print(line)


def make_turn(player):
    if player == 0:
        mark = mark_0
    else:
        mark = mark_1

    message = f"{players[player]}'s turn (1-9): "

    draw_game_log()
    game_log.append(message)
    c_str = readchar()
    if c_str.isdigit() and 0 < int(c_str) < 10:
        c = int(c_str)
        if A[keyMap[c - 1][0]][keyMap[c - 1][1]] == tile:
            A[keyMap[c - 1][0]][keyMap[c - 1][1]] = mark
        else:
            print('This cell is marked. Try again')
            make_turn(player)
    else:
        print('Invalid input. Try again')
        make_turn(player)

    return()


def check_winner(z, player):
    if player == 0:
        mark = mark_0
    else:
        mark = mark_1

    # Rows check
    for i in range(tableSize):
        L = z[i]
        if L.count(mark) == 3:
            return 1

    # Columns check
    for x in range(tableSize):
        L = [i[x] for i in z]
        if L.count(mark) == 3:
            return 1

    # \ diagonal check
    L = []
    for i in range(tableSize):
        L.append(z[i][i])
    if L.count(mark) == 3:
        return 1

    # / diagonal check
    L = []
    for i in range(tableSize):
        L.append(z[2 - i][i])
    if L.count(mark) == 3:
        return 1

    return 0


def name_players():
    players.append(input('Player I, enter your name: '))
    players.append(input('Player II, enter your name: '))


def new_game(q):
    clear()
    print('>> T I C - T A C - T O E <<')
    name_players()
    draw_table()
    turn_count = 0
    while True:
        for i in range(len(players)):
            make_turn(i)
            turn_count += 1
            draw_table()
            if check_winner(A, i) == 1:
                winner = players[i]
                q = 1  # flag variable q to end the game
                break
            elif turn_count == 9:
                q = 1
                print("It's a tie! One more? (Y/N): ", end='')
                return ()
        if q == 1:
            break
    print('Game has ended! The winner is ' + winner + '! One more? (Y/N): ', end='')
    return ()

# Main Program
# Initialization (don't change any values except marks here)


tableSize = 3
players = []
tile = '■'
mark_0 = 'X'
mark_1 = 'O'
game_log = []
keyMap = ((2, 0), (2, 1), (2, 2), (1, 0), (1, 1), (1, 2), (0, 0), (0, 1), (0, 2))

# New Game
while True:
    A = generate_table(tableSize)
    quitGame = 0
    winPlayer = new_game(quitGame)
    new = input()
    players = []
    if new == 'N':
        break
