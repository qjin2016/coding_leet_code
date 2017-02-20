'''
21
Merge two sorted linked lists and return it as a new list. 
The new list should be made by splicing together the nodes of the first two lists.

'''


# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

	def __repr__(self):
		if self:
			return "{} -> {}".format(self.val, self.next)

class Solution():
	def mergeTwoLists(self, l1, l2):

		cur = dummy = ListNode(0)

		while l1 and l2:
			if l1.val < l2.val:
				cur.next = l1
				l1 = l1.next
			else:
				cur.next = l2
				l2 = l2.next

			cur = cur.next

		cur.next = l1 or l2

		return dummy.next






if __name__ == '__main__':
	l1 = ListNode(1)
	l1.next = ListNode(4)
	l2 = ListNode(2)
	l2.next = ListNode(3)
	print Solution().mergeTwoLists(l1, l2)