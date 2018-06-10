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

def find_empty_space(board):
	for i in range(9):
		for j in range(9):
			if board[i][j] == 0:
				return i, j

	# no empty spaces found, then return 9, 9
	return 9, 9

def solve_sudoku(board):
	# if there are no zeroes then board is solved
	i, j = find_empty_space(board)
	if i == 9 and j == 9:
		print board
		return True
	else:
		for k in range(1, 10):
			# if placing k at (i, j) is valid, then assign k to it
			# and solve for next place
			if is_valid(board, i, j, k):
				board[i][j] = k
				if solve_sudoku(board):
					return True
				# if board doesn't get solved, reset that position to 0
				# and we can try next value of k
				board[i][j] = 0

	return False

# 9x9 matrix
# creating a 2D array for the grid
board = [[0 for x in range(9)]for y in range(9)]
# board = np.zeros((9, 9)) 
# assigning values to the grid
board = [[3,0,6,5,0,8,4,0,0], [5,2,0,0,0,0,0,0,0], [0,8,7,0,0,0,0,3,1], [0,0,3,0,1,0,0,8,0], [9,0,0,8,6,3,0,0,5], [0,5,0,0,9,0,6,0,0], [1,3,0,0,0,0,2,5,0], [0,0,0,0,0,0,0,7,4], [0,0,5,2,0,6,3,0,0]]
solved = solve_sudoku(board)

print(solved)