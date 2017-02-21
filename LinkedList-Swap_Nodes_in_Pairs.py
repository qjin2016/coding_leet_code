'''
24,

Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.

'''

class LinkedList(object):
	def __init__(self, x):
		self.val = x
		self.next = None

	def __repr__(self):
		if self:
			return "{} -> {}".format(self.val, self.next)


class Solution(object):
	def swapPairs(self, head):
		dummy = LinkedList(0)
		dummy.next = head
		cur = dummy
		while cur.next and cur.next.next:
			next_one, next_two, next_three = cur.next, cur.next.next, cur.next.next.next
			cur.next = next_two
			next_two.next = next_one
			next_one.next = next_three
			cur = next_one
		return dummy.next


if __name__ == '__main__':
	l1 = LinkedList(1)
	l2 = LinkedList(2)
	l3 = LinkedList(3)
	l4 = LinkedList(4)
	l1.next = l2
	l2.next = l3
	l3.next = l4
	print Solution().swapPairs(l1)


