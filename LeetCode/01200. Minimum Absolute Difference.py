# Time Limit Exceeded Solution
class Solution:
    def minimumAbsDifference(self, arr):
        res = []
        min_distance = float("inf")
        arr.sort()
        for x in range(len(arr)):
            for y in range(x+1, len(arr)):
                diff = abs(arr[x] - arr[y])
                if diff < min_distance:
                    min_distance = diff
                    res = []
                if diff == min_distance:
                    res.append([arr[x], arr[y]])
        return res
        
# Solution: only one loop
class Solution:
    def minimumAbsDifference(self, arr):
        res = []
        min_distance = float("inf")
        arr.sort()
        for x in range(len(arr)-1):
            y = x + 1
            diff = abs(arr[x] - arr[y])
            if diff < min_distance:
                min_distance = diff
                res = []
            if diff == min_distance:
                res.append([arr[x], arr[y]])
        return res
