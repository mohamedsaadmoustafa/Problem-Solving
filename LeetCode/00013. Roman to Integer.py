class Solution:
    def romanToInt(self, s: str) -> int:
        Symbol = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        sum = Symbol[s[-1]]
        for index in range(len(s)-1):
            #print(s[index], s[index+1])
            if Symbol[s[index]] >= Symbol[s[index+1]]:
                sum += Symbol[s[index]]
            else:
                sum -= Symbol[s[index]]
        return sum
