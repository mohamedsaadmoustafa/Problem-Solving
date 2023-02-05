class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if len(arr) <= 1: return True
        arr.sort()
        diff = arr[1]-arr[0]
        idial = [arr[0]]*len(arr)
        for i in range(len(idial)): idial[i] += diff * i
        return arr == idial or arr[::-1] == idial[::-1] 
