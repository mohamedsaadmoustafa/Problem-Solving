# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self): 
        self.a = set()
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        if not root: return -1
        self.a.add(root.val)
        if root.left:  self.findSecondMinimumValue(root.left)
        if root.right: self.findSecondMinimumValue(root.right)
        if len(self.a)>=2:
            return sorted(list(self.a))[1]
        else:
            return -1
          
          
# 
