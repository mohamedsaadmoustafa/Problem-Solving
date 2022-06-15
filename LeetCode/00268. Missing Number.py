class Solution:
    def missingNumber(self, nums) -> int:
        sorted_nums = sorted(nums)
        print(sorted_nums)
        n = max(nums) + 1
        e = set(range(0, max(nums))).difference(sorted_nums)
        try: return list(e)[0]
        except: return n
        
# Another Solution
class Solution:
    def missingNumber(self, nums) -> int:
        maxn = len(nums)+1
        nums.append(maxn)
        sorted_nums = sorted(nums)
        for i, item in enumerate(sorted_nums):
            try:
                if item+1 != sorted_nums[i+1]:
                    return item + 1
            except: 0 # if sorted_nums[i+1] is not exist - out of range
              
              
# Another Solution
class Solution:
    def missingNumber(self, nums) -> int:
		    return sum(range(len(nums)+1)) - sum(nums)
     
    
# Another Solution
class Solution:
    def missingNumber(self, nums) -> int:
        sum_nums = 0
        for index, item in enumerate(nums):
            sum_nums += item - index
        return sum_nums
      
      
# Another Solution
class Solution:
    def missingNumber(self, nums) -> int:
        for i, item in enumerate(nums):
            if i not in nums:
                return i
