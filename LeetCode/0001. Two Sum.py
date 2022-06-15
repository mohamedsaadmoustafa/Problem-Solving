# O(n²)
class Solution:    
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
                    
                    
                    
# O(n)
class Solution:    
    def twoSum(self, nums, target):
        values = {}
        for i, value in enumerate(nums):
            print(f'#{i}: {target} - {value} = {target - value}')
            if target - value in values:
                return [values[target - value], i]
            else:
                values[value] = i
