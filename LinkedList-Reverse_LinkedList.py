'''
206

Reverse a singly linked list.

'''

class ListNode(object):

	def __init__(self, val):
		self.val = val
		self.next = None

	def __repr__(self):
		if self:
			return '{} -> {}'.format(self.val, self.next)

class Solution(object):

	# destructive reversal
	def reverseList(self, head):

		# recursion

		dummy = ListNode(float('Inf'))

		# i = 0

		while head:
			dummy.next, head.next, head = head, dummy.next, head.next
		# 	i += 1

		return dummy.next


	# an iterative approach
	# https://www.youtube.com/watch?v=XwIivDg1BlY
	def reverseList2(self, head):
		dummy = None # this is where we build the reversed linkedlist
		while head:
			prev = head 
			head = prev.next 
			prev.next = dummy
			dummy = prev
		return dummy


	# an recursive solution
	def reverseList3(self, head):
		if not head.next:
			return head
		else:
			new_start = self.reverseList3(head.next)
		head.next.next = head
		head.next = None
		return new_start






if __name__ == '__main__':
	l = ListNode(0)
	l.next = ListNode(1)
	l.next.next = ListNode(2)
	l.next.next.next = ListNode(3)
	print Solution().reverseList3(l)
		