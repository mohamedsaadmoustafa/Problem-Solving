# using pow function
class Solution:
    def mySqrt(self, x):
        #if x == 0: return 0
        return int(pow(x, 0.5))
      
# using math library: x=2147395600: 
# Output: 46339
# Expected: 46340
import math
class Solution:
    def mySqrt(self, x):
        if x == 0: return 0
        return int(np.exp(0.5*np.log(x)))
      

## Newton method for calculating the square root of 2
class Solution:
    def mySqrt(self, x):
        if x == 0: return 0
        last_f = x
        while True:
            f = (last_f + (x / last_f)) / 2
            if (abs(f - last_f) < 0.0001 ): break
            last_f = f
        return int(f)
