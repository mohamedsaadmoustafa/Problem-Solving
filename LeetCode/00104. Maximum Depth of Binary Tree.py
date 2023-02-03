class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return False
        return max(self.maxDepth(root.right), self.maxDepth(root.left)) + 1
