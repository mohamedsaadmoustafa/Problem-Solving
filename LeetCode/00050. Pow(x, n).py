class Solution:
    def myPow(self, x: float, n: int) -> float:
				return pow(x, n) # xD
      
      
      
# Runtime Error
class Solution:
    def myPow(self, x: float, n: int) -> float:
        # return pow(x, n) # xD
            def myPow(self, x: float, n: int) -> float:
        # return pow(x, n) # xD
        if n == 0: return 1
        elif n == 1: return x
        elif n < 0: return (1 / (x**-n))
        else: return x**n
        
        
# wronge answer at 
#  myPow(34.00515 , -3)
class Solution:
    def __init__(self):
        self.head = None
        
    def abs(self, n):
        if n < 0: n = -n
        return n

    def myPow(self, x: float, n: int) -> float:
        # return pow(x, n) # xD
        result = 1
        if n == 0: return 1
        if n < 0: 
            x, n = 1/x, self.abs(x)
        # Exponentiation by Squaring
        while n:
            if n % 2: result *= x
            x *= x
            n // = 2
        return result
      
#With constant auxiliary memory
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0: 
            return self.myPow( 1/x, -n );
        elif n == 0:
             return  1;
        elif n % 2 == 0:
            return self.myPow( x*x,  n/2 );
        elif n % 2 == 1:
             return x * self.myPow( x*x, (n-1)/2 );
          
          
          
          
class Solution:
    def __myPow(self, y, x, n):
        if n < 0:        return self.__myPow( y, 1/x, -n );
        elif n == 0:     return  1;
        elif n % 2 == 0: return self.__myPow( x*x,  x*x,  n/2 );
        elif n % 2 == 1: return x * self.__myPow( y*x, x*x, (n-1)/2 );

    def myPow(self, x, n):
        return self.__myPow(1, x, n)
      
      
#The iterative version of the algorithm also uses a bounded auxiliary space
class Solution:
    def myPow(self, x: float, n: int) -> float:
        # return pow(x, n) # xD
        y = 1
        if n == 0: return 1
        if n < 0: 
            x, n = 1/x, -n
        # Exponentiation by Squaring
        while n > 1:
            if n % 2 == 0: 
                x *= x
                n /= 2
            else:
                y *= x
                x *= x
                n = (n - 1) / 2
        return x * y
      
