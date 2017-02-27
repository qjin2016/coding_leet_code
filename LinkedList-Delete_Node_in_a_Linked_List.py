'''
237,

Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.

Supposed the linked list is 1 -> 2 -> 3 -> 4 and you are given the third node with value 3, 

the linked list should become 1 -> 2 -> 4 after calling your function.


'''

class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

	def __repr__(self):
		if self:
			return '{} -> {}'.format(self.val, self.next)

class Solution(object):
	def deleteNode(self, node):
		if node and node.next:
			node_2_delete = node.next
			node.val = node_2_delete.val
			node.next = node_2_delete.next
			del node_2_delete



# if __name__ == '__main__':
# 	l1 = ListNode(0)
# 	l1.next = ListNode(1)
# 	l1.next.next = ListNode(2)
# 	print(Solution().deleteNode(l1.next))

