# Sudoku Solving Program

# function to print board in well-formatted way
def print_board(board):
	for i in range(9):
		for j in range(9):
			print(board[i][j]),
		print(' ')

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
	# finding which 3x3 square is for x and y
	temp_x = x - x % 3
	temp_y = y - y % 3

	for i in range(3):
		for j in range(3):
			if board[i + temp_x][j + temp_y] == n:
				return False

	# Otherwise valid
	return True

# function to find if any space on board is unassigned
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
		print_board(board)
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

# creating a 2D array for the grid
board = [[0 for x in range(9)]for y in range(9)]
# board = np.zeros((9, 9)) 
# assigning values to the grid
board = [[3,0,6,5,0,8,4,0,0], [5,2,0,0,0,0,0,0,0], [0,8,7,0,0,0,0,3,1], [0,0,3,0,1,0,0,8,0], [9,0,0,8,6,3,0,0,5], [0,5,0,0,9,0,6,0,0], [1,3,0,0,0,0,2,5,0], [0,0,0,0,0,0,0,7,4], [0,0,5,2,0,6,3,0,0]]

# start solving
solved = solve_sudoku(board)

# print whether solution is possible
print(solved)