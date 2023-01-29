# another solution
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = []
        for num in nums:
            if num in x:
                temp.remove(num)
            else:
                temp.append(num)
        return temp[0]

# Another Solution
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return 2*sum(set(nums))-sum(nums)
    
# Better Solution
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
