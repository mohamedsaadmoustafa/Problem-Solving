# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root, val):
        if not root: return
        if root.val == val: return root
        elif not root.left and root.right: return self.searchBST(root.right, val)
        elif not root.right and root.left: return self.searchBST(root.left, val)
        return self.searchBST(root.left, val) or self.searchBST(root.right, val)
      
      
      
# since it's Binary Search Trees so left < head < right 
class Solution:
    def searchBST(self, root, val):
        if not root: return
        if root.val == val: return root
        elif val > root.val: return self.searchBST(root.right, val)
        else: return self.searchBST(root.left, val)
