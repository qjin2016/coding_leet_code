'''
169

Given an array of size n, find the majority element. 

The majority element is the element that appears more than [n/2] times.

You may assume that the array is non-empty and the majority element always exist in the array.

'''

class Solution(object):

	def majorityElement(self, nums):
		num_dict = {}
		total_len = len(nums)
		if total_len == 1:
			return nums[0]
		for num in nums:
			if num not in num_dict:
				num_dict[num] = 1
			else:
				num_dict[num] += 1
				if num_dict[num] > (total_len // 2):
					return num

	def majorityElement2(self, nums):
		idx, cn = 0, 1
		for i in range(1, len(nums)):
			if nums[i] == nums[idx]:
				cn += 1
			else:
				cn -= 1
				if cn == 0:
					idx = i
					cn = 1
		return nums[idx]

	def majorityElement3(self, nums):
		from collections import Counter
		return sorted(Counter(nums).items(), key=lambda a:a[1], reverse=True)[0][0]

if __name__ == '__main__':
	print Solution().majorityElement([1])
	print Solution().majorityElement2([1, 2, 3, 2, 4, 2, 5, 2, 6, 2])
	print Solution().majorityElement3([1, 2, 3, 2, 4, 2, 5, 2, 6, 2])
