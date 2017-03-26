'''
53,
https://leetcode.com/problems/maximum-subarray/#/description

Kadane's algorithm

a nice explanation here: http://www.geeksforgeeks.org/largest-sum-contiguous-subarray/
'''

class Solution(object):

	def maxSubArray(self, nums):
		if max(nums) < 0:
			return max(nums)
		local_max = 0
		global_max = float('-Inf')
		for num in nums:
			local_max = max(0, local_max + num)
			global_max = max(global_max, local_max)
		return global_max