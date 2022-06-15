# Time Limit Exceeded
class Solution:
    def addSpaces(self, s, spaces):
        string = ''
        for index, char in enumerate(s):
            if index in spaces: # index in spaces makes it worth
                string += ' '
            string += char
        return string
      
# Accepted
class Solution:
    def addSpaces(self, s, spaces):
        string = ''
        spaces_index = 0  # spaces' index
        for index, char in enumerate(s):
            if spaces_index < len(spaces) and index == spaces[spaces_index]:
                string += ' '
                spaces_index += 1
            string += char
        return string
      
      
# Another Solution
class Solution:
    def addSpaces(self, s, spaces):
        space = ' '
        last_index = 0
        string = ''
        for index in spaces:
            string += s[last_index:index] + ' '
            last_index = index
        string += s[last_index:]
        return string
