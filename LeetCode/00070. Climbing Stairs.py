# Time Limit Exceeded
# Time Complexity: O(2^n)
class Solution:
    def fib(self, n):
        if n <= 1:
            return n
        return self.fib(n-1) + self.fib(n-2)
    
    def climbStairs(self, n):
        return self.fib(n+1)
  
  
# Top-down - Memoization
class Solution:
    def fib(self, n):
        if n <= 1: return 1 # if n stairs == 1 then return 1
        if self.dp[n] != -1: return self.dp[n] # if fib(n) exist in dp array then return result
        self.dp[n] = self.fib(n-1) + self.fib(n-2) # if not exist then calculate fib(n) = fib(n-1)-fib(n-2)
        return self.dp[n]
  
    def climbStairs(self, n):
        if n == 0: return 0 # no stairs
        if n <= 1: return 1 # no stairs
        self.dp = [-1]*(n+1)    # create array with n+1 size filled with -1s
        self.fib(n)     # calculate fib(n)
        return self.dp[n]        # return result from dp list
      
      
      
#  bottom-up - Tabulation
class Solution:
    def fib(self, n):
        self.dp = [0, 1]
        for i in range(2, n+1):
            print(i, self.dp)
            self.dp.append(self.dp[i-1] + self.dp[i-2])
  
    def climbStairs(self, n):
        x = n + 1
        self.fib(x)          # calculate fib(n)
        return self.dp[x]   # return result from dp list
      
      
      
# Space Optimized
class Solution:
    def fib(self, n):
        a, b = 0, 1
        for _ in range(2, n+1):
            a, b = b, a + b
        return b
  
    def climbStairs(self, n):
        if n == 0: return 0
        return self.fib(n + 1)          # calculate fib(n+1)
