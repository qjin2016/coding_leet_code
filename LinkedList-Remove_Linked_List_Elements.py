'''
203

Remove all elements from a linked list of integers that have value val.

Example
Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
Return: 1 --> 2 --> 3 --> 4 --> 5

'''

class ListNode(object):
	def __init__(self, val):
		self.val = val
		self.next = None

	def __repr__(self):
		if self:
			return '{} -> {}'.format(self.val, self.next)


class Solution(object):
	def removeElements(self, head, val):
		dummy = ListNode(0)
		dummy.next = head
		cur = pre = dummy
		while cur and cur.next:
			if cur.val == val:
				pre.next = cur.next
			else:
				pre = cur
			cur = cur.next
		if cur.val == val:
			pre.next = None
		return dummy.next



if __name__ == '__main__':
	l1 = ListNode(0)
	l1.next = ListNode(1)
	# l1.next.next = ListNode(2)
	print Solution().removeElements(l1, 0)
