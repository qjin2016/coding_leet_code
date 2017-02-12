'''
Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?
'''
class Solution(object):
	def getRow(self, rowIndex):
		"""
		:type rowIndex: int
		:rtype: List[int]
		"""
		if rowIndex == 0:
			return [1]
		elif rowIndex == 1:
			return [1, 1]
		else:
			ini_row = [1, 2, 1]

			def GenNextRow(ini_row):
				return map(lambda x, y: x+y, [0] + ini_row, ini_row + [0])

			while len(ini_row) < rowIndex+1:
				ini_row = GenNextRow(ini_row)

			return ini_row

	# def getRow2(self, rowIndex):
	# 	result = [0] * (rowIndex + 1)
	# 	print result
	# 	for i in xrange(rowIndex + 1):
	# 		old = result[0] = 1
	# 		for j in xrange(1, i+1):
	# 			old, result[j] = result[j], old + result[j]
	# 			print result
	# 	return result

	def getRow3(self, rowIndex):
		row = [1]
		for _ in range(rowIndex):
			row = [x+y for x, y in zip([0]+row, row+[0])]
		return row

	def getRow4(self, rowIndex):
		row = [1]
		for _ in range(rowIndex):
			row = map(lambda x, y: x+y, [0]+row, row+[0])
		return row




if __name__ == '__main__':
	import time
	start_time = time.time()
	result = Solution().getRow4(4)
	end_time = time.time()
	print 'result: {0}'.format(result)
	print 'time: {0}'.format(end_time-start_time)
