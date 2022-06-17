class Solution:
    def singleNumber(self, nums) -> int:
        if len(nums) == 1: return nums[0]
        d = {}
        for num in nums:
            if num in d.keys(): 
                d[num] += 1
            else:
                d[num] = 1
                
        return min(d, key=d.get)
