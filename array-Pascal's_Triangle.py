'''
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''
class Solution(object):
	def generate(self, numRows):
		if numRows == 0:
			pascal = []
		elif numRows == 1:
			pascal = [[1]]
		elif numRows == 2:
			pascal = [[1], [1,1]]
		elif numRows == 3:
			pascal = [[1], [1,1], [1,2,1]]
		else:
			pascal = [[1], [1,1], [1,2,1]]
			for i in range(4, numRows+1):
				each_row = [1]
				for j in range(1, i-1):
					each_row.append(pascal[i-2][j-1] + pascal[i-2][j])
				each_row.append(1)
				pascal.append(each_row)
		return pascal

	def generate2(self, numRows):
		pascal = []
		for i in range(numRows):
			pascal.append([])
			for j in range(i+1):
				if j in [0, i]:
					pascal[i].append(1)
				else:
					pascal[i].append(pascal[i-1][j-1] + pascal[i-1][j])
		return pascal

	def generate3(self, numRows):
		if not numRows: 
			return []
		else:
			pascal = [[1]]
			for i in range(1, numRows):
				# print [map(lambda x, y: x+y, pascal[-1]+[0], [0]+pascal[-1])]
				pascal += [map(lambda x, y: x+y, pascal[-1]+[0], [0]+pascal[-1])]
		return pascal

	def generate4(self, numRows):
		if numRows == 0: return []
		if numRows == 1: return [[1]]
		pascal = [[1], [1, 1]]
		def gen_num(pre_nums):
			new_num = []
			for i in range(len(pre_nums)+1):
				if i in [0, len(pre_nums)]:
					new_num.append(1)
				else:
					new_num.append(pre_nums[i-1] + pre_nums[i])
			return new_num
		while len(pascal) < numRows:
			pascal.append(gen_num(pascal[-1]))
		return pascal




if __name__ == '__main__':
	import time
	prior = time.time()
	result = Solution().generate3(5)
	after = time.time()
	print 'result:' 
	print result
	print 'time:' + str(after-prior)


