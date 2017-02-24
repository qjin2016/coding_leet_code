'''
160,
https://leetcode.com/problems/intersection-of-two-linked-lists/?tab=Description

Write a program to find the node at which the intersection of two singly linked lists begins.

NOTE:
1, If the two linked lists have no intersection at all, return null.
2, The linked lists must retain their original structure after the function returns.
3, You may assume there are no cycles anywhere in the entire linked structure.
4, Your code should preferably run in O(n) time and use only O(1) memory.

'''

class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

	def __repr__(self):
		if self:
			return '{} -> {}'.format(self.val, self.next)

class Solution(object):
	def getIntersectionNode(self, headA, headB):
		curA, curB = headA, headB
		intersection, tailA, tailB = None, None, None

		while curA and curB:
			if curA == curB:
				intersection = curA
				break

			if curA.next:
				curA = curA.next
			elif tailA is None:
				tailA = curA
				curA = headB
			else:
				break


			if curB.next:
				curB = curB.next
			elif tailB is None:
				tailB = curB
				curB = headA
			else:
				break


		return intersection



if __name__ == '__main__':
	l1 = ListNode(0)
	l1.next = ListNode(1)
	intersection = ListNode(2)
	intersection.next = ListNode(3)
	l1.next.next = intersection
	l2 = ListNode(-1)
	l2.next = intersection
	print Solution().getIntersectionNode(l1, l2)


