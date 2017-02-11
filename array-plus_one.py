"""
Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.

"""

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        current_pos = len(digits) - 1
        carry = 1
        while current_pos >= 0:
        	current_val = digits[current_pos] + carry
        	current_mol = current_val % 10
        	digits[current_pos] = current_mol
        	if current_mol:
        		carry = 0
        		return digits
        	current_pos -= 1
        if carry:
        	digits = [1] + digits
        return digits

    def plusOne_2(self, digits):
    	num = 0
    	for i, v in enumerate(reversed(digits)):
    		num += v * 10**i
    	num += 1
    	return [int(j) for j in str(num)]

    def plusOne_3(self, digits):
    	digits = [str(i) for i in digits]
    	num = int(''.join(digits)) + 1
    	return [int(j) for j in str(num)]




if __name__ == '__main__':
	print Solution().plusOne([9, 9])
	print Solution().plusOne_2([9, 9, 9])
	print Solution().plusOne_3([9, 9, 9, 9])