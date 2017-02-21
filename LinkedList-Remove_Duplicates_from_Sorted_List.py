'''
83

Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.

'''

class LinkedList(object):
	def __init__(self, x):
		self.val = x
		self.next = None

	def __repr__(self):
		if self:
			return "{} -> {}".format(self.val, self.next)


class Solution(object):
	def deleteDuplicates(self, head):
		cur = head
		while cur and cur.next:
			if cur.val == cur.next.val:
				cur.next = cur.next.next
			else:
				cur = cur.next
		return head




if __name__ == '__main__':
	l = LinkedList(1)
	l.next = LinkedList(1)
	l.next.next = LinkedList(1)
	print Solution().deleteDuplicates(l)
