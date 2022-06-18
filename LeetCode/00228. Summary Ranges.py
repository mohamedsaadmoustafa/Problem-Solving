class Solution:
    def summaryRanges(self, nums):
        output = []
        length = len(nums)
        index = 0
        while index < length:
            from_ = nums[index]
            while index < length-1 and nums[index] == nums[index+1]-1:
                index += 1
            to_ = nums[index]
            print(to_ , from_)
            if from_ == to_: output += [f'{from_}']
            else:            output += [f'{from_}->{to_}']
            index += 1
        return output
