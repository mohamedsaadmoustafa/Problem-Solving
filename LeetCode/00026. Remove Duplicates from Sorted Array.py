class Solution:
    def removeDuplicates(self, nums):
        a = sorted(list(set(nums)))
        for i, num in enumerate(a):
            nums[i] = num
        return len(a)
      
      
class Solution:
    def removeDuplicates(self, nums):
        index = 0
        for num in nums:
            if index < 1 or num > nums[index-1]:
                print(num, nums[index-1])
                nums[index], index = num, index+1
        return index
      
      
class Solution:
    def removeDuplicates(self, nums):
        indeces = []
        for index, num in enumerate(nums):
            if num in nums[index+1:]:
                indeces += [index]

        for i in indeces[::-1]: del nums[i]
				return len(nums)
