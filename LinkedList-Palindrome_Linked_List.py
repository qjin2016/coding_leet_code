'''
234,

Given a singly linked list, determine if it is a palindrome.

Could you do it in O(n) time and O(1) space?

'''

class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

	def __repr__(self):
		if self:
			return '{} -> {}'.format(self.val, self.next)

# class Solution(object):
# 	def isPalindrome(self, head):



if __name__ == '__main__':
	l1 = ListNode(0)
	l1.next = ListNode(1)
	l1.next.next = ListNode(2)
	l1.next.next.next = ListNode(1)
	l1.next.next.next.next = ListNode(0)
	print(l1)
