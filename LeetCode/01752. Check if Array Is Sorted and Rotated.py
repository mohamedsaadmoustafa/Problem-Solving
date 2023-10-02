class Solution:
    def check(self, nums: List[int]) -> bool:
        rotates, n = 0, len(nums)
        for i in range(n):
            if nums[i] > nums[(i + 1) % n]: rotates += 1
            if rotates > 1: return False
        return True
        
