class Solution:
    def findMiddleIndex(self, nums):
        length = len(nums)
        for index in range(length):
            left = sum(nums[:index]) if index > 0 else 0
            # +1 to exclode nums[index] value from Summation
            right = sum(nums[index+1:]) if index < length else 0
            if left == right: return index
        return -1
