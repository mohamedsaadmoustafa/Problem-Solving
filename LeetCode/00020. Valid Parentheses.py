class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0: return False
        array = []
        for p in s:
            if   p == '(': array.append(')')
            elif p == '{': array.append('}')
            elif p == '[': array.append(']')
            # p in [')', '}', ']']
            # if array still empty return false
            # pop last item from array; if it !p then return salse
            elif not array or array.pop() != p:
                return False
        return not array
