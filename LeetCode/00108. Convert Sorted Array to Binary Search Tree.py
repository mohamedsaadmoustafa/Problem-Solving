# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums: return
        mid = (len(nums))//2
        return TreeNode(
            val = nums[mid],
            left = self.sortedArrayToBST(nums[:mid]),
            right = self.sortedArrayToBST(nums[mid+1:])
        )
