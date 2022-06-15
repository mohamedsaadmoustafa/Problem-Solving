class Solution:
    def __init__(self):
        self.alpha_lower = 'abcdefghijklmnopqrstuvwxyz'
        self.alpha_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.digits = '0123456789'

    def lower(self, string):
        result_string = ''
        for index, char in enumerate(string):
            if char in self.alpha_upper:
                upper_index = self.alpha_upper.index(char)
                result_string += self.alpha_lower[upper_index]
            else:
                result_string += char
        return result_string

    def remove_punctuation(self, string):
        result_string = ''
        for char in string:
            if char in self.digits or char in self.alpha_lower:
                result_string += char
        return result_string 

    def isPalindrome(self, s: str) -> bool:
        string = s
        string = self.lower(string)
        string = self.remove_punctuation(string)

        n = len(string)
        for idx in range(n):
            if string[idx] != string[n-idx-1]:
                return False
        return True
      
      
# another solution
class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ''
        for char in s:
            if char.isalnum(): string += char.lower() 
        return string == string[::-1]
