# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return False
        return max(self.maxDepth(root.right), self.maxDepth(root.left)) + 1

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        if abs(self.maxDepth(root.right) - self.maxDepth(root.left)) <= 1:
            return self.isBalanced(root.right) and self.isBalanced(root.left)
        return False
