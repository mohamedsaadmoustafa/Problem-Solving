class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        print('\n')
        length = len(nums)
        if length == 0: return 1
        
        array = [0] * (length + 1)
        print(array)

        for i in range(length):
            if nums[i] > 0 and nums[i] <= length:
                print(nums[i])
                array[nums[i]] = 1
        print(array)

        for i in range(1, length + 1):
            print(i, '->', array[i])
            if array[i] == 0:
                return i
        return length + 1
