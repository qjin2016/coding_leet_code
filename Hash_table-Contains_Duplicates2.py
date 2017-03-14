'''
219,

https://leetcode.com/problems/contains-duplicate-ii/#/description

'''

class Solution(object):

	# solution one, too through
	def containsNearbyDuplicate(self, nums, k):
		if len(nums) in [0,1]:
			return False
		num_dist = {}
		nearbyDu = False
		for i, num in enumerate(nums):
			if num not in num_dist:
				num_dist[num] = i
			else:
				if num_dist[num] != True and i - num_dist[num] > k:
					num_dist[num] = i
					nearbyDu = False
				elif i - num_dist[num] <= k:
					num_dist[num] = True
					nearbyDu = True
					
		return nearbyDu

	# solution two,
	def containsNearbyDuplicate(self, nums, k):
		num_dist = {}
		for i, num in enumerate(nums):
			if num not in num_dist:
				num_dist[num] = i
			elif i - num_dist[num] <= k:
				return True
			elif i - num_dist[num] > k:
				num_dist[num] = i
		return False