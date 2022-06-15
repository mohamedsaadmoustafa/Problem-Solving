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
