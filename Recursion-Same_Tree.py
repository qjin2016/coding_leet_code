'''
100,

Given two binary trees, write a function to check if they are equal or not.

Two binary trees are considered equal if they are structurally identical and the nodes have the same value.
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
	def isSameTree(self, p, q):
		if p is None and q is None:
			return True

		elif p is not None and q is not None:
			return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

		else:
			return False



if __name__ == '__main__':
	root1, root1.left, root1.right = TreeNode(1), TreeNode(2), TreeNode(3)
	root2, root2.left, root2.right = TreeNode(1), TreeNode(2), TreeNode(3)
	print (Solution().isSameTree(root1, root2))