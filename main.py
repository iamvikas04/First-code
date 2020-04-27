play = True
game_won = True
winner = False
f = True
v = True

#win functions
	# horizontal winner
def horizontally(game):
	global winner
	if game[0] == game[1] == game[2] and game[0] != "-":
		print("player won Horizontally\n Winner!!!!")
		winner = True
	if game[3] == game[4] == game[5] and game[3] != "-":
		print("player won Horizontally\n Winner!!!")
		winner = True
	if game[6] == game[7] == game[8] and game[6] != "-":
		print("player won Horizontally\n Winner!!!")
		winner = True

	#vertical winnery
def vertically(game):
	global winner
	if game[0] == game[3] == game[6] and game[0] != "-":
		print("player won vertically\nwinner")
		winner = True
	if game[1] == game[4] == game[7] and game[1] != "-":
		print("player won vertically\n winner")
		winner = True
	if game[2] == game[5] == game[8] and game[2] != "-":
		print("player won vertically\n winner")
		winner = True
#diagonal winner
def diags(game):
	global winner
	if game[0] == game[4] == game[8] and game[4] != "-":
		print("player won diagonally\n winner")
		winner = True
	if game[2] == game[4] == game[6] and game[4] != "-":
		print("player won diagonally\n winner")
		winner = True

game = ["-","-","-",
        "-","-","-",
        "-","-","-"]

def display_board():
	print(game[0] + " | "+ game[1] + " | " + game[2])
	print(game[3] + " | "+ game[4] + " | " + game[5])
	print(game[6] + " | "+ game[7] + " | " + game[8])

def handle_turn(current_player):
	global f
	pos = input("Chooose your position(1/9): ")

	if pos not in ["1","2","3","4","5","6","7","8","9"]:
		print("invalid input")
		f = False
		return False
	else:
		f = True
		pos = int(pos) - 1
		if game[pos] != "-":
			print("You Can't go there Try Again")
			f = False
			return
		else:
			f = True
		game[pos] = current_player
		display_board()

def win(game):
	horizontally(game)
	vertically(game)
	diags(game)

def flip_player():
	global f
	global player
	if f == True:
		if player == "X":
			player = "O"
		elif player == "O":
			player = "X"

player = "X"
while play:
	display_board()
	while game_won:
		print(player)
		handle_turn(player)
		win(game)
		flip_player()
		if winner == True:
			game_won = False
	play = False