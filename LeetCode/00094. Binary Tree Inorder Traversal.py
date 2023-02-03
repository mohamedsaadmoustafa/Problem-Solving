# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        self.answer = []
        self.inorder_rec(root)
        return self.answer

    def inorder_rec(self, root):
        if root is None: return
        self.inorder_rec(root.left)
        self.answer.append(root.val)
        self.inorder_rec(root.right)
