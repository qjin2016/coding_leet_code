'''
202,

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 19 is a happy number

12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

'''

class Solution(object):
	"""docstring for Solution"""
	def isHappy(self, n):
		results = [] # array might be too expensive to look for an element, use dic to speed things up
		new_m = self.addSquare(n)
		while True:
			if new_m == 1:
				return True
			if new_m in results:
				return False
			results.append(new_m)
			new_m = self.addSquare(new_m)

	def isHappy(self, n):
		results = {}
		new_m = self.addSquare(n)
		while True:
			if new_m == 1:
				return True
			if new_m in results:
				return False
			results[new_m] = 1
			new_m = self.addSquare(new_m)


	def addSquare(self, m):
		m = str(m)
		new_m = 0
		for i in m:
			new_m += int(i)**2
		return new_m

if __name__ == '__main__':
	print(Solution().isHappy(3))
