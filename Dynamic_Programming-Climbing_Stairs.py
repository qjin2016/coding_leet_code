'''
70,
https://leetcode.com/problems/climbing-stairs/#/description
'''

class Solution():
	def climbStairs(self, n):
		num_steps = [0] * (n + 1)
		for i in range(n+1):
			if i == 0:
				num_steps[i] = 0
			elif i == 1:
				num_steps[1] = 1
			elif i == 2:
				num_steps[2] = 2
			else:
				num_steps[i] = num_steps[i-1] + num_steps[i-2]
		return num_steps[n]

if __name__ == '__main__':
	print(Solution().climbStairs(1))