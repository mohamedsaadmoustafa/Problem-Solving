# No use for + or -
class Solution:
    def getSum(self, a, b):
        return a + b
      
      
# Time Limit Exceeded
# at a=-1, b=1
class Solution:
    def getSum(self, a, b):
        while a != 0 and b != 0:
            AND, XOR = a & b,  a ^ b
            a, b = AND << 1, XOR
        if a!= 0: return a
        else: return b
        
        
# Recurtion 
# Time Limit Exceeded
# at a=-1, b=1
class Solution:
    def getSum(self, a, b):
        return a if (b == 0) else self.getSum((a^b), (a&b) << 1);
      
### Accepted  ###
class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFF
        while b: a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        return a if a < 1000 else ~(a ^ mask)
