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

# assigning values to the grid
board = [[3,0,6,5,0,8,4,0,0], [5,2,0,0,0,0,0,0,0], [0,8,7,0,0,0,0,3,1], [0,0,3,0,1,0,0,8,0], [9,0,0,8,6,3,0,0,5], [0,5,0,0,9,0,6,0,0], [1,3,0,0,0,0,2,5,0], [0,0,0,0,0,0,0,7,4], [0,0,5,2,0,6,3,0,0]]
# solution
# 3 1 6 5 7 8 4 9 2  
# 5 2 9 1 3 4 7 6 8  
# 4 8 7 6 2 9 5 3 1  
# 2 6 3 4 1 5 9 8 7  
# 9 7 4 8 6 3 1 2 5  
# 8 5 1 7 9 2 6 4 3  
# 1 3 8 9 4 7 2 5 6  
# 6 9 2 3 5 1 8 7 4  
# 7 4 5 2 8 6 3 1 9 

# board = [[5,1,7,6,0,0,0,3,4],[2,8,9,0,0,4,0,0,0],[3,4,6,2,0,5,0,9,0],[6,0,2,0,0,0,0,1,0],[0,3,8,0,0,6,0,4,7],[0,0,0,0,0,0,0,0,0],[0,9,0,0,0,0,0,7,8],[7,0,3,4,0,0,5,6,0],[0,0,0,0,0,0,0,0,0]]
# solution
# 5 1 7 6 9 8 2 3 4  
# 2 8 9 1 3 4 7 5 6  
# 3 4 6 2 7 5 8 9 1  
# 6 7 2 8 4 9 3 1 5  
# 1 3 8 5 2 6 9 4 7  
# 9 5 4 7 1 3 6 8 2  
# 4 9 5 3 6 2 1 7 8  
# 7 2 3 4 8 1 5 6 9  
# 8 6 1 9 5 7 4 2 3  


# board = [
#     [8,0,0,0,0,0,0,0,0],
#     [0,0,3,6,0,0,0,0,0],
#     [0,7,0,0,9,0,2,0,0],
#     [0,5,0,0,0,7,0,0,0],
#     [0,0,0,0,4,5,7,0,0],
#     [0,0,0,1,0,0,0,3,0],
#     [0,0,1,0,0,0,0,6,8],
#     [0,0,8,5,0,0,0,1,0],
#     [0,9,0,0,0,0,4,0,0]]

# solution 
# 8 1 2 7 5 3 6 4 9  
# 9 4 3 6 8 2 1 7 5  
# 6 7 5 4 9 1 2 8 3  
# 1 5 4 2 3 7 8 9 6  
# 3 6 9 8 4 5 7 2 1  
# 2 8 7 1 6 9 5 3 4  
# 5 2 1 9 7 4 3 6 8  
# 4 3 8 5 2 6 9 1 7  
# 7 9 6 3 1 8 4 5 2 

# start solving
solved = solve_sudoku(board)

# print whether solution is possible
print(solved)