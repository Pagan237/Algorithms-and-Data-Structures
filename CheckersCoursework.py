import lib
board = [[".", "1", "2", "3", "4", "5", "6", "7", "8"],
		["1", " ", "w", " ", "w", " ", "w", " ", "w"],
		["2", "w", " ", "w", " ", "w", " ", "w", " "],
	 	["3", " ", " ", " ", "w", " ", "w", " ", "w"],
	 	["4", "w", " ", "w", " ", " ", " ", " ", " "],
	 	["5", " ", "b", " ", " ", " ", " ", " ", " "],
		["6", " ", " ", " ", " ", "b", " ", "b", " "],
		["7", " ", "b", " ", "b", " ", "b", " ", "b"],
	 	["8", "b", " ", "b", " ", "b", " ", "b", " "]]
undo = []
redo = []
undo_move = 0
redo_move = 0
moved = 0
for i in board:
	print(i)
def init():
	while True:
		white = 12
		black = 12
		if white != 0:
			black = 0
			white = 0
			lib.move_white(board, undo, redo)
			for i in range (8):
				for j in range(8):
					if board[i][j] == "b" or board[i][j] == "B":
						black = black + 1
			if black == 0:
				print("WHITE WINS")
				break
			else:
				lib.move_black(board, undo, redo)
				for i in range(8):
					for j in range(8):
						if board[i][j] == "w" or board[i][j] == "W":
							white = white + 1
		else:
			print("BLACK WINS")
			break
init(),