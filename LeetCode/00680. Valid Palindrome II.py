class Solution:
    def Palindrome(self, s, left, right):
        while left < right:
            print(s[left], s[right])
            if s[left] == s[right]: left, right = left+1, right-1
            else: return False
        return True

    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1
        while left < right:
            print(s[left], s[right])
            if s[left] == s[right]: left, right = left+1, right-1
            else: return self.Palindrome(s, left+1, right) or self.Palindrome(s, left, right-1)
        return True
