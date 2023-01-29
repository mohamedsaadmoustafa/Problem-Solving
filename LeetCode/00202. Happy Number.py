class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1: return True
        s = set()
        while n != 1:
            n = list(map(int, list(str(n))))
            n = sum(map(lambda x:x*x, n))
            if n in s: return False
            else: s.add(n)
        return True

