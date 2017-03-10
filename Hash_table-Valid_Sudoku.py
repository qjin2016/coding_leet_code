'''
36, 

rules: http://sudoku.com.au/TheRules.aspx

'''

class Solution(object):

	def isValidSudoku(self, board):
		# check each col/row
		for i in range(9):
			# by row
			if not self.isValid(board[i]):
				return False
			# by col
			if not self.isValid([board[j][i] for j in range(9)]):
				return False
		
		# check sub-box (3*3 box)
		for i in range(3):
			for j in range(3):
				if not self.isValid([board[m][n] for m in range(3*i, 3*i+3) \
													for n in range(3*j, 3*j+3)]):
					return False

		return True

	# def a check function
	def isValid(self, xs):
		xs = filter(lambda x: x != '.', xs)
		return len(set(xs)) == len(xs)




if __name__ == "__main__":
	board = [[1, '.', '.', '.', '.', '.', '.', '.', '.'],
			['.', 2, '.', '.', '.', '.', '.', '.', '.'],
			['.', '.', 3, '.', '.', '.', '.', '.', '.'],
			['.', '.', '.', 4, '.', '.', '.', '.', '.'],
			['.', '.', '.', '.', 5, '.', '.', '.', '.'],
			['.', '.', '.', '.', '.', 6, '.', '.', '.'],
			['.', '.', '.', '.', '.', '.', 7, '.', '.'],
			['.', '.', '.', '.', '.', '.', '.', 8, '.'],
			['.', '.', '.', '.', '.', '.', '.', '.', 9]]
	print (Solution().isValidSudoku(board))