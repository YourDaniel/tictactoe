#Functionality

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
	
	c = int(input(players[player]+"'s turn (1-9): "))
	if 0 < c < 10:
		if A[keyMap[c-1][0]][keyMap[c-1][1]] == tile:
			A[keyMap[c-1][0]][keyMap[c-1][1]] = mark
		else:
			print('This cell is marked. Try again')
			makeTurn(player)
	else:
		print('Invalid input. Try again')
		makeTurn(player)
	return()

def checkWinner(Z,player): #Z - gameTable

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
	drawTable()
	while True:
		for i in range(len(players)):
			makeTurn(i)
			drawTable()
			if checkWinner(A,i) == 1:
				winner = players[i]
				q = 1     #workaround to end the game
				break
		if q == 1:
			break					#end of workaround	
	return(winner)

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
	winPlayer = newGame(quit)
	new = input(('Game has ended! The winner is '+ winPlayer +'! One more? (Y/N):'))
	if new == 'N':
		break
