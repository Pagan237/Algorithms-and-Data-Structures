import copy
def move_white(board, undo, redo, undo_move, redo_move):
	valid = 0
	moved = 0
	while True:
		if undo_move == 0:
			board2 = copy.deepcopy(board)
			undo.insert(0, board2)
			break
		else:
			break
	while undo_move == 1:
		re = input("Y to redo, N to continue: ")
		if re == "N" or re == "n":
			moved = 0
			break
		if re == "Y" or re == "y":
			board = redo[0]
			del redo[0]
			valid = 1
			moved = 1
			redo_move == 1
			undo.insert(0, board)
			if len(redo) == 0:
				undo_move = 0
				break
		else:
			print ("Please enter y or n")
			continue
		if len(undo) > 1:
			board3 = copy.deepcopy(board)
			u(board, undo, redo, undo_move, moved, valid)
			if board == board3:
				break
			else:
				moved = 1
				valid = 1
				undo_move = 1
				break
	while undo_move == 0:
		if len(undo) > 1:
			board3 = copy.deepcopy(board)
			u(board, undo, redo, undo_move, moved, valid)
			if board == board3:
				break
			else:
				moved = 1
				valid = 1
				undo_move = 1
				break
		else:
			break
	while moved == 0:
		coord_y = int(input("Enter Column of piece: "))		
		coord_x = int(input("Enter Row of piece: "))
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
	for i in board2[8]:
		if i == "w":
			board2[8][acca] = "W"
		acca = acca + 1
	for i in board:
		print(i)


def move_black(board, undo, redo, undo_move, redo_move):
	valid = 0
	moved = 0
	while True:
		if undo_move == 0:
			board2 = copy.deepcopy(board)
			undo.insert(0, board2)
			break
		else:
			break
	while undo_move == 1:
		re = input("Y to redo, N to continue: ")
		if re == "N" or re == "n":
			moved = 0
			continue
		if re == "Y" or re == "y":
			board = redo[0]
			redo.pop[0]
			valid = 1
			moved = 1
			redo_move == 0
			undo.insert(0, board)
			if len(redo) == 0:
				undo_move = 1
				break
		else:
			print ("Please enter y or n")
			continue
		if len(undo) > 0:
			board3 = copy.deepcopy(board)
			u(board, undo, redo, undo_move, moved, valid)
			if board == board3:
				break
			else:
				moved = 1
				valid = 1
				undo_move = 1
				break
	while undo_move == 0:
		if len(undo) > 0:
			print("A")
			board4 = copy.deepcopy(board)
			u(board, undo, redo, undo_move, moved, valid)
			if board == board4:
				print("L")
				break
			else:
				moved = 1
				valid = 1
				undo_move = 1
				break
	while moved == 0:
		coord_y = int(input("Enter Column of piece: "))		
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

def u(board, undo, redo, undo_move, moved, valid):
	while True:
		choice = input("Y to undo, N to continue?: ")
		if choice == "Y" or choice == "y":
			redo.insert(0, board)
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
"""board2 = board
for i in range(8):
for j in range(8):
if board2[i][j] == "W":
if board2[i+1][j-1] == "B":
if board2[i+2][j-2] == " ":
board2[i][j] = " "
board2[i+1][j-1]= " "
board2[i+2][j-2] = "W"
valid = 1
for n in board:
print(n)
break					
elif board2[i+1][j+1] == "B":
if board2[i+2][j+2] == " ":
board2[i][j] = " "
board2[i+1][j+1]= " "
board2[i+2][j+2] = "W"
valid = 1
else:
continue
"""	 	