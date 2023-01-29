class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        index_map = {}
        for index, value in enumerate(nums):
            if value in index_map and index - index_map[value] <= k:
                return True
            index_map[value]=index
