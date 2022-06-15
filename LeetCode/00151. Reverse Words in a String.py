class Solution:
    def reverseWords(self, s: str) -> str:
        string  = [word for word in s.split(' ')[::-1] if i!='']
        return (' ').join(string )
      
      
# another solution
class Solution:
    def reverseWords(self, s: str) -> str:
        string = s.split(' ') # split at space
        string = string[::-1] # reverse list
        string = [i for i in string if i!=''] # remove ''
        string = (' ').join( string )   # join list elements/words seperated by space
        return string 
      
      
# another solution
class Solution:
    def __split(self, string, delimiter):
        # Empty Separator
        if not delimiter: raise ValueError("Empty Separator")

        # Empty string
        if not string: return [string]

        result = []
        start_index = 0

        string += delimiter # to add last word

        for index, alpha in enumerate(string):
            if alpha == delimiter:
                result.append(string[start_index: index])
                start_index = index + 1

        # only delimiter ? return string in list
        if not start_index: return [string] 

        #result.append(string[start_index:index + 1]) # to add last word

        # return list of result
        return result

    def __reverse(self, array):
        return array[::-1]

    def __join(self, array, delimiter):
        # Empty Separator
        if not delimiter: raise ValueError("Empty Separator")
        string_result = ''
        for index, word in enumerate(array):
            # at last word add it to string then return string
            if index == len(array)-1:
                string_result += word
                return string_result
            string_result += word + delimiter

    def reverseWords(self, s):
        string = self.__split(s, ' ') # split at space
        string = self.__reverse(string) # reverse list
        string = [i for i in string if i!=''] # remove ''
        string = self.__join( string, ' ' )   # join list elements/words seperated by space
        return string 
