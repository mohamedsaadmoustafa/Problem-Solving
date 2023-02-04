# Time Limit Exceeded 
class Solution(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        n = list(range(1, n+1))
        for x in n:
            if sum(n[:x]) == sum(n[x-1:]):
                return x
        return -1

#  Correct

class Solution(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        """
        sum of 1 to x = sum of x to n
        1 + [2 + ... + (x-1)] + x = x + (x+1) ... + (n-1) + n
        (1 + x) * x // 2 = (x + n) * (n - x + 1) // 2
        x + x^2          = nx - x^2 + x + n^2 - nx + n
        2 * x^2          = n^2 + n
        x = sqrt((n^2 + n) // 2)
        """
        import math
        if n == 0: return 0
        N = (n*n+n)//2
        sq_N = int(math.sqrt(N))
        if sq_N**2 != N: return -1
        return sq_N
