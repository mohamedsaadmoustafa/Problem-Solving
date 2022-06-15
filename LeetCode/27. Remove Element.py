class Solution:
    def removeElement(self, nums, val) -> int:
        indeces = []

        for index, num in enumerate(nums):
            if num == val:
                indeces += [index]
                
        for i in indeces[::-1]:
            del nums[i]
