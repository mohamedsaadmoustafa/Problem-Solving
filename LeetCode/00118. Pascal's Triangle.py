class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        l = []
        for i in range(numRows):
            l.append([])
            for j in range(i+1):
                if i==j or j==0: x = 1
                else: x = l[i-1][j-1]+l[i-1][j]
                l[i].append(x)
        return l
