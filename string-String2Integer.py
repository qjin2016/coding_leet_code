'''
8

Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. 

If you want a challenge, please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). 

You are responsible to gather all the input requirements up front.

The atoi() function takes a string (which represents an integer) as an argument and returns its value.

'''

class Solution(object):

	def myAtoi(self, str):
		result = 0
		result_str = ''
		INT_MAX, INT_MIN = 2147483647, -2147483648

		if not str:
			return result

		i = 0

		# blank space
		while i < len(str) and not str[i]:
			i += 1

		# sign, + or -
		sign = 1
		if str[i] == '+':
			i += 1
		elif str[i] == '-':
			sign = -1
			i += 1

		while i < len(str) and str[i] >= '0' and str[i] <= '9':
			if result > (INT_MAX - (ord(str[i]) - ord('0')))/10:
				if sign == 1:
					return INT_MAX
				elif sign == -1:
					return INT_MIN

			result = result*10 + (ord(str[i]) - ord('0'))/10
			i += 1

		result *= sign






if __name__ == '__main__':
	print Solution().atoi("")
	print Solution().atoi("-1")
	print Solution().atoi("2147483647") 
	print Solution().atoi("2147483648")
	print Solution().atoi("-2147483648")  
	print Solution().atoi("-2147483649")






