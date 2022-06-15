# Output Limit Exceeded
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if len(s) == 2 and s[0] == s[1]: return True
        if len(s) == 3 and s[0] == s[1] and s[0] == s[2]: return True

        for i in range(len(s)):
            if i>1 and s[:i] == s[i:i+i] and s[:i] == s[-i:]:
                return True
        return False
      
# Accepted
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # Duplicate string and remove first char and last char; if it's repeated pattern it will return True 
        return s in (s + s)[1:-1]
