#Time Limit Exceeded
class Solution:
    def findDisappearedNumbers(self, nums):
        r = []
        for index in range(1, len(nums)+1):
            if index not in nums:
                r.append(index)
        return r

# Accepted
class Solution:
    def findDisappearedNumbers(self, nums):
        e = set(range(1, len(nums)+ 1))
        for num in nums:
            if num in e: e.remove(num)
        return list(e)
      
      
# Another Solution
class Solution:
    def findDisappearedNumbers(self, nums):
        sorted_nums = sorted(nums)
        n = max(nums) + 1
        e = set(range(1, len(nums)+1)).difference(sorted_nums)
        return list(e)
