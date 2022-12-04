# Maps score output of game based on choice made and game outcome
def gameScore(pair):
	scores = {
		"AX": [7,3],
		"AY": [4,4],
		"AZ": [1,8],
		"BX": [8,1],
		"BY": [5,5],
		"BZ": [2,9],
		"CX": [9,2],
		"CY": [6,6],
		"CZ": [3,7]
	}
	return scores[pair][0], scores[pair][1]

# Sums all scores in a round per player
def roundWinner(input_data):
	player1 = 0 
	player2 = 0 
	for item in input_data:
		score = gameScore(item)
		player1 = player1 + score[0]
		player2 = player2 + score[1]
		print("Player 1: " + str(player1) +" to Player 2: " + str(player2))
	if player1 > player2:
		print("Player 1 Wins! " + str(player1) + " to " + str(player2))
	if player1 == player2:
		print("It's a Draw! " + str(player1) + " to " + str(player2))
	if player1 < player2:
		print("Player 2 Wins! " + str(player1) + " to " + str(player2))

# Cleans up puzzle input
def gameInput(filename):
	file = open(filename)
	game_list =[]
	for item in file:
		x = item
		x = x.strip()
		x = x.replace(" ", "")
		game_list.append(x)
	return game_list

roundWinner(gameInput("input.txt"))

