'''
6

https://leetcode.com/problems/zigzag-conversion/


P    Q 
A   EN
Y  L C  L
C D  D E
D    E

'''

class Solution(object):

	# def convert(self, s, numRows):
	# 	converted_s = ''
	# 	total_len = len(s)
	# 	if numRows == 1:
	# 		return s
	# 	if numRows == total_len-1:
	# 		return s[0] + s[numRows] + s[1:numRows]
	# 	if numRows >= total_len:
	# 		return s
	# 	for nRow in range(numRows):
	# 		if nRow in [0, numRows-1]:
	# 			n = nRow
	# 			while n < total_len:
	# 				converted_s += s[n]
	# 				n += numRows+1
	# 		else:
	# 			n = nRow
	# 			while n < total_len:
	# 				converted_s += s[n]
	# 				n += numRows-1
	# 	return converted_s

	def convert(self, s, numRows):
		if numRows == 1:
			return s
		step, zigzag = 2*numRows - 2, ''
		for i in range(numRows):
			for j in range(i, len(s), step):
				zigzag += s[j]
				if 0<i<numRows-1 and j + step - 2 * i < len(s):
					zigzag += s[j+step-2*i]
		return zigzag


if __name__ == '__main__':
	# print Solution().convert('PAYPALISHIRING', 1)
	print Solution().convert('ABC', 2)




