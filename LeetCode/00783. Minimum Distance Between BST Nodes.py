# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.min, self.last_val = float('inf'), -float('inf')
        
    def minDiffInBST(self, root):
        if root.left:  self.minDiffInBST(root.left)
        self.min = min(self.min, abs(root.val - self.last_val))
        self.last_val = root.val
        if root.right: self.minDiffInBST(root.right)
        return self.min
