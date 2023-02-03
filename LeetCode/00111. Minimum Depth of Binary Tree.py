# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        right, left = self.minDepth(root.right), self.minDepth(root.left)
        if root.left and root.right: return min(right, left) + 1
        else: return max(right, left) + 1
