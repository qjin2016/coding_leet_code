'''
46,

https://leetcode.com/problems/permutations/#/description

A nice writing about backtracking:
http://www.geeksforgeeks.org/write-a-c-program-to-print-all-permutations-of-a-given-string/

'''

# recursion
class Solution(object):
	# @param num, a list of integer
	# @return a list of lists of integers
	def permute(self, num):
		result = []
		used = [False] * len(num)
		self.permuteRecu(result, used, [], num)
		return result

	# permute every possibility
	def permuteRecu(self, result, used, cur, num):
		if len(cur) == len(num):
			result.append(cur + [])
			return
		for i in range(len(num)):
			if not used[i]:
				used[i] = True
				cur.append(num[i])
				self.permuteRecu(result, used, cur, num)
				cur.pop()
				used[i] = False

# backtracking
# http://www.geeksforgeeks.org/write-a-c-program-to-print-all-permutations-of-a-given-string/
class Solution2(object):
	def __init__(self):
		self.a_list = []
	def permute(self, a, l, r):
		if l == r:
			self.a_list.append(a)
		else:
			for i in range(l, r+1):
				a[l], a[i] = a[i], a[l]
				self.permute(a, l+1, r)
				a[l], a[i] = a[i], a[l] # backtrack

if __name__ == '__main__':
	# print(Solution().permute([1,2,3]))
	so = Solution2()
	so.permute([1,2,3], 0, 2)
	print(so.a_list)