class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num>9:
            num = sum(list(map(int, list(str(num)))))
        return num
