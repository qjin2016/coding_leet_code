'''
303,
https://leetcode.com/problems/range-sum-query-immutable/#/description
'''
class NumArray(object):
	def __init__(self, nums):
		self.acc = reduce(lambda c, x: c + [c[-1] + x], nums, [0])
		# self.acc = [0]
		# for num in nums:
		# 	self.acc.append(self.acc[-1] + num)

	def sumRange(self, i, j):
		return self.acc[j + 1] - self.acc[i]