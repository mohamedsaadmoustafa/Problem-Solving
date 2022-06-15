class Solution:
    def runningSum(self, nums):
        sum = 0
        for index, num in enumerate(nums):
            sum += num
            nums[index] = sum
        return nums
      
# Another Solution
class Solution:
    def runningSum(self, nums):
        for index in range(1, len(nums)):
            nums[index] += nums[index-1]
        return nums
