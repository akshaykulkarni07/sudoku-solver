# Sudoku Solving Program

# checking validity of putting n at (x, y) on the board
def is_valid(board, x, y, n):
	# checking 'x'th row
	for i in range(9):
		if board[x][i] == n:
			return False

	# checking 'y'th column
	for i in range(9):
		if board[i][y] == n:
			return False

	# checking 3x3 square
	temp_x = 0
	temp_y = 0
	# finding which 3x3 square is for x and y
	if x > 2 and x < 6:
		temp_x = 3
	elif x > 5 and x < 9:
		temp_x = 6

	if y > 2 and y < 6:
		temp_y = 3
	elif y > 5 and y < 9:
		temp_y = 6

	for i in range(temp_x, temp_x + 3):
		for j in range(temp_y, temp_y + 3):
			if board[temp_x][temp_y] == n:
				return False

	# Otherwise valid
	return True