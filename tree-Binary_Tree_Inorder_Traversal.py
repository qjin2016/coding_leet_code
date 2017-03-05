'''
94,

Binary Tree Inorder Traversal
'''

# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	# recursive
	traversed = []
	def inorderTraversal(self, root):
		if root is None:
			return []
		if root.left:
			self.inorderTraversal(root.left)
		
		self.traversed.append(root.val)

		if root.right:
			self.inorderTraversal(root.right)
		return self.traversed

if __name__ == '__main__':
	t = TreeNode(1)
	t.left = TreeNode(2)
	t.right = TreeNode(3)
	print(Solution().inorderTraversal(t))