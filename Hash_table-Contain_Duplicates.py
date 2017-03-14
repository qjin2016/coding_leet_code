'''
217, 

https://leetcode.com/problems/contains-duplicate/#/description

'''

class Solution(object):

	# solution 1
	def containsDuplicate(self, nums):
		if not nums:
			return False
		distincts = {}
		for num in nums:
			if num not in distincts:
				distincts[num] = True
			else:
				return True
		return False

	# solution 2
	def containsDuplicate(self, nums):
		return len(nums) == len(set(nums))