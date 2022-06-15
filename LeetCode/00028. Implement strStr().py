class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack: 
            return haystack.index(needle)
        else: 
            return -1
          

          
          
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for index in range(len(haystack)):
            if haystack[index : index+len(needle)] == needle:
                return index
        return -1
