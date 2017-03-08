'''
1,

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You may assume that each input would have exactly one solution.
Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

class Solution(object):
	def twoSum(self, nums, target):
		dict_table = {}
		for i, v in enumerate(nums):
			j = target - v
			if j in dict_table:
				return [dict_table[j], i]
			dict_table[v] = i
		return []


if __name__ == '__main__':
	print(Solution().twoSum([3, 2, 4], 6))