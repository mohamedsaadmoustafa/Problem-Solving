# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        return self.isSymmetric_(root.left, root.right)

    def isSymmetric_(self, left, right):
        if not left and not right: return True
        if not left or not right:  return False
        if left.val != right.val:  return False
        return self.isSymmetric_(left.left, right.right) and self.isSymmetric_(left.right, right.left)

