class Solution:
    def differenceOfSum(self, nums) -> int:
        return sum(nums) - sum(int(num) for num in ''.join(map(str, nums)))
        
        
# Better Solution
class Solution:
    def to_digits(self, n):
        sum = 0
        while n:
            sum += n % 10
            n //= 10
        return sum

    def differenceOfSum(self, nums) -> int:
        sum = digit_sum = 0
        for num in nums:
            digit_sum += num if num < 10 else self.to_digits(num)
            sum += num
        return abs(sum - digit_sum)
