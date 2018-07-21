#Functionality
import os

def clear():
	os.system( 'cls' )

def generateTable(size):
	return [[tile for i in range(size)] for j in range(size)]

def drawTable():
  for i in range(tableSize):
    for j in range(tableSize):
      print(A[i][j], end=' ')
    print(end='\n')
  return()

def makeTurn(player):

	if player == 0:
		mark = mark_0
	else:
		mark = mark_1
	
	cStr = input(players[player]+"'s turn (1-9): ")
	if cStr.isdigit() and 0 < int(cStr) < 10:
		c = int(cStr)
		if A[keyMap[c-1][0]][keyMap[c-1][1]] == tile:
			A[keyMap[c-1][0]][keyMap[c-1][1]] = mark
		else:
			print('This cell is marked. Try again')
			makeTurn(player)
	else:
		print('Invalid input. Try again')
		makeTurn(player)

	return()

def checkWinner(Z,player):

	if player == 0:
		mark = mark_0
	else:
		mark = mark_1

	#Rows check
	for i in range(tableSize):
		L = Z[i]
		if L.count(mark) == 3:
			return 1

	#Columns check
	for x in range(tableSize):
		L = [i[x] for i in Z]
		if L.count(mark) == 3:
			return 1

	#\ diagonal check
	L = []
	for i in range(tableSize):
		L.append(Z[i][i])
	if L.count(mark) == 3:
		return 1

	#/ diagonal check
	L = []
	for i in range(tableSize):
		L.append(Z[2-i][i])
	if L.count(mark) == 3:	
		return 1

	return 0

def namePlayers():
	players.append(input('Player I, enter your name:'))
	players.append(input('Player II, enter your name:'))

def newGame(q):
	namePlayers()
	clear()
	drawTable()
	turnCount = 0
	while True:
		for i in range(len(players)):
			makeTurn(i)
			turnCount += 1
			drawTable()
			if checkWinner(A,i) == 1:
				winner = players[i]
				q = 1     #workaround to end the game
				break
			elif turnCount == 9:
				q = 1
				print("It's a tie! One more? (Y/N): ",end="")
				return()
		if q == 1:
			break					#end of workaround
	print('Game has ended! The winner is '+ winner +'! One more? (Y/N): ',end='')
	return()

#Main Program

#Initialization (don't change any values except marks here)
tableSize = 3
players = []
tile = '■'
mark_0 = 'X'
mark_1 = 'O'
keyMap = [[2,0],[2,1],[2,2],[1,0],[1,1],[1,2],[0,0],[0,1],[0,2]]

#New Game
while True:
	A = generateTable(tableSize)
	quit = 0
	turnCount = 0
	winPlayer = newGame(quit)
	new = input()
	players = []
	if new == 'N':
		break
