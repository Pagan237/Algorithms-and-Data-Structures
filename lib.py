import copy
def move_white(board, undo, redo):
	valid = 1
	undone = 0
	redone = 0
	while True:
		if len(redo) == 0:
			board2 = copy.deepcopy(board)
			undo.insert(0, board2)
			break
		else:
			break
	if len(redo) > 0:
		while True:
			board4 = board
			y(board, undo, redo)
			if board != board4:
				redone = 0
				break
			else:
				redone = 1
				break
	if len(undo) > 1:
		while True:
			board3 = copy.deepcopy(board)
			u(board, undo, redo)
			if board == board3:
				break
			else:
				undone = 1
				break
	while undone == 0 and redone == 0:
		coord_y = int(input("Enter Column white of piece: "))		
		coord_x = int(input("Enter Row white of piece: "))
		if board[coord_y][coord_x] == "W" or board[coord_y][coord_x] == "w":
			valid = 0 
			redo.clear()
			break	
		else:
			print("Please select white piece")
			continue
	while valid == 0:
		force_white(board)
		if board[coord_y][coord_x] == "W" or board[coord_y][coord_x] == "w":
			new_y = int(input("column to move to: "))
			new_x = int(input("row to move to: "))
			displacement = (new_x - coord_x) * (new_x - coord_x)
			if new_y == coord_y + 1 and displacement == 1:
				if board[new_y][new_x] == " ":
					board[new_y][new_x] = "w"
					board[coord_y][coord_x] = " "
					break
				else:
					print("Invalid Move")
			else: 
				print("Invalid Move")
		else:
			break
	acca = 0
	for i in board[8]:
		if i == "w":
			board[8][acca] = "W"
		acca = acca + 1
	for i in board:
		print(i)


def move_black(board, undo, redo):
	valid = 1
	undone = 0
	redone = 0
	while True:
		if len(redo) == 0:
			board2 = copy.deepcopy(board)
			undo.insert(0, board2)
			break
		else:
			break 
	if len(redo) > 0:
		while True:
			board4 = board
			y(board, undo, redo)
			if board != board4:
				redone == 0
				break
			else:
				redone = 1
				print("LOL")
				break 
	if len(undo) > 0 and redone != 1:
		while True:
			board3 = copy.deepcopy(board)
			u(board, undo, redo)
			if board == board3:
				break
			else:
				break
	while redone == 0 and undone == 0:
		coord_y = int(input("Enter Column of black piece: "))		
		coord_x = int(input("Enter Row of piece: "))
		if board[coord_y][coord_x] == "b" or board[coord_y][coord_x] == "B":
			valid = 0
			break
		else:
			print ("Select a black piece")
			continue
	while valid == 0:
		force_black(board)
		if board[coord_y][coord_x] == "b" or board[coord_y][coord_x] == "B":
			new_y = int(input("column to move to: "))
			new_x = int(input("row to move to: "))
			displacement = (new_x - coord_x) * (new_x - coord_x)
			if (new_y == coord_y - 1 or new_y == coord_y + 1) and displacement == 1:
				if board[new_y][new_x] == " ":
					board[new_y][new_x] = "B"
					board[coord_y][coord_x] = " "
					break
				else:
					print("Invalid Move")
			else:
				print("Invalid Move")
		break
	acca = 0
	for i in board[1]:
		if i == "b":
			board[1][acca] = "B"
			acca = acca + 1
	for i in board:
		print(i)

def force_white(board):
	for i in range (8):
		for j in range (9):
			if i < 7 and j < 7:
				if (board[i + 1][j + 1] == "b" or board[i + 1][j + 1] == "B") and board[i + 2][j + 2] == " ":
					if board[i][j] == "W":
						board[i + 2][j + 2] = "W"
						board[i][j] = " "
						board[i+1][j+1] = " "
					else:
						board[i + 2][j + 2] = "w"
						board[i][j] = " "
						board[i+1][j+1] = " "
			if i < 7 and j > 1:
				if board[i + 1][j - 1] == "B" or board[i + 1][j - 1] == "b" and board[i + 2][j - 2] == " ":
					if board[i][j] == "W":
						board[i + 2][j - 2] = "W"
						board[i + 1][j - 1] = " "
						board[i][j] == " "
					else:
						board[i + 2][j - 2] = "w"
						board[i][j] = " "
						board[i+1][j-1] = " "
			if i > 2 and j > 1:
				if (board[i - 1][j - 1] == "B" or board[i - 1][j - 1] == "b") and board[i - 2][j - 2] == " " and board[i][j] == "W":
					board[i - 2][j - 2] = "W"
					board[i][j] = " "
					board[i - 1][j - 1] = " "
			if i > 2 and j < 7:	
				if (board[i - 1][j + 1] == "B" or board[i - 1][j + 1] == "b") and board[i - 2][j + 2] == " " and board[i][j] == "W":
					board[i - 2][j + 2] = "W"
					board[i][j] = " "
					board[i - 1][j + 1] = " "

def force_black(board):
	for i in range (8):
		for j in range (9):
			if i > 1 and j > 1:
				if (board[i - 1][j - 1] == "w" or board[i -1][j - 1] == "W") and board[i - 2][j - 2] == " ":
					if board[i][j] == "B":
						board[i][j] = " "
						board[i - 1][j - 1] = " "
						board[i - 2][j - 2] = "B"			
					else:
						board[i][j] = " "
						board[i-1][j-1] = " "
						board[i-2][j-2] = "b"
			if i > 2 and j < 7:
				if (board[i - 1][j + 1] == "w" or board[i -1][j + 1] == "W") and board[i - 2][j + 2] == " ":
					if board[i][j] == "B":
						board[i][j] = " "
						board[i - 1][j + 1] = " "
						board[i - 2][j + 2] = "B"
					else:
						board[i][j] = " "
						board[i-1][j-1] = " "
						board[i-2][j-2] = "b" 
			if i < 7 and j > 1:	
				if (board[i + 1][j - 1] == "w" or board[i - 1][j - 1] == "W") and board[i + 2][j - 2] == " " and board[i][j] == "B":
					board[i][j] = " "
					board[i - 1][j - 1] = " "
					board[i - 2][j - 2] = "B"
			if i < 7 and j < 7:	
				if (board[i + 1][j + 1] == "w" or board[i - 1][j + 1] == "W") and board[i + 2][j + 2] == " " and board[i][j] == "B":
					board[i][j] = " "
					board[i - 1][j + 1] = " "
					board[i - 2][j + 2] = "B" 
 
def u(board, undo, redo):
	while True:
		choice = input("Y to undo, N to continue?: ")
		if choice == "Y" or choice == "y":
			redo_board = copy.deepcopy(board)
			redo.insert(0, redo_board)
			for i in range (8):
				for j in range(8):
					board[i][j] = undo[1][i][j]
			del undo[0]
			break
		if choice == "n" or "N":
			break
		else:
			print ("Please enter Y or N") 
			continue

def y(board, undo, redo):
	while True:
		choice2 = input("Y to redo, N to continue: ")
		if choice2 == "Y" or choice2 == "y":
			undo_board = copy.deepcopy(board)
			undo.insert(0, undo_board)
			for i in range(8):
				for j in range(8):
					board[i][j] = redo[0][i][j]
			del redo[0]
			print(len(redo))
			break
		if choice2 == "n" or choice2 == "N":
			break
		else:
			print("please enter y or n")
			continue