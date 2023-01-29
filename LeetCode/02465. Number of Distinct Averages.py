class Solution(object):
    def distinctAverages(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return len(set(nums[index]+nums[len(nums)-index-1] for index in range(len(nums) >> 1)))
