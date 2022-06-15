class Solution:
    def secondHighest(self, s: str) -> int:
        array = []
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        for char in s:
            if char not in alphabets:
                array += [int(char)]

        array = set(array)
        if len(array) == 1 or len(array) == 0: return -1
        array = sorted(array)
        array = array[:-1]
        array = max(array)
        return array
      
      
# Another Solution
class Solution:
    def secondHighest(self, s: str) -> int:
        array = []
        for char in s:
            if char.isdigit():
                array += [int(char)]

        array = set(array)
        if len(array) < 2: return -1
        return max(sorted(array)[:-1])
