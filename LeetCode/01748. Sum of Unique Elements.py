class Solution:
    def sumOfUnique(self, nums):
        if len(nums) == 1:
            return nums[0]
        nums = sorted(nums)
        sum = 0
        for index, num in enumerate(nums):
            if num not in nums[index+1:] and num != nums[index-1]:
                sum += nums[index]
        return sum


# another solution
from collections import defaultdict

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1

        return sum(key for key in counts if counts[key] == 1)
