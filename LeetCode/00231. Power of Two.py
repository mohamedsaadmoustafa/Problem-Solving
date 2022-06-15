class Solution:
    def isPowerOfTwo(self, n):
        if n == 1: return True
        if n <= 0 or n % 2 != 0: return False
        return self.isPowerOfTwo(n/2)
      
      
# Another Solution using numpy log2: n = 2^x -> x = log2(n)
import numpy as np
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0: return False
        # n = 2^x
        x = np.log2(n)
        #return True if x == int(x) else False
        return x == int(x)
      
