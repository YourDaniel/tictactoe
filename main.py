import os
from readchar import readchar

# NEW RELEASE BRANCH
# Makes ANSI sequences work
import ctypes
kernel32 = ctypes.windll.kernel32
kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)


def clear():
    print('\x1b[2J', end='')


def generate_table(size):
    return [[tile] * size for i in range(size)]


def draw_table():
    clear()
    for i in range(tableSize):
        for j in range(tableSize):
            print(A[i][j], end=' ')
        print(end='\n')
    return()


def make_turn(player):
    if player == 0:
        mark = mark_0
    else:
        mark = mark_1

    print(f"{players[player]}'s turn (1-9): ")
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



# Initialization (don't change any values except marks here)
tableSize = 3
players = []
tile = '■'
mark_0 = 'X'
mark_1 = 'O'
keyMap = ((2, 0), (2, 1), (2, 2), (1, 0), (1, 1), (1, 2), (0, 0), (0, 1), (0, 2))

A = generate_table(tableSize)
def main():
    quit_game = False
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
                quit_game = True
                break
            elif turn_count == 9:
                quit_game = True
                print("It's a tie! One more? (Y/N): ", end='')
                return ()
        if quit_game:
            break
    print('Game has ended! The winner is ' + winner + '! One more? (Y/N): ', end='')
    new = input()


if __name__ == '__main__':
    main()
