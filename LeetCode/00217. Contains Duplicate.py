# Time Limit Exceeded
class Solution:
    def containsDuplicate(self, nums):
        array = [item for item in nums if nums.count(item)>1]
        if array != []:
            return True
        return False

# wrong answers
class Solution:
    def containsDuplicate(self, nums):
        for item in nums:
            nums.remove(item)
            if item in nums:
                return True
        return False

# Accepted
class Solution:
    def containsDuplicate(self, nums):
        s = set(nums)
        if len(s) != len(nums):
            return True
        return False
