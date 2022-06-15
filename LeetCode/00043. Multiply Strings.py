# with using a built-in BigInteger library or convert the inputs to integer directly.
# class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return str(int(num1) * int(num2))
    
# Without use any built-in BigInteger library or convert the inputs to integer directly.
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        result = [0] * (len(num1) + len(num2))
        for index1 in reversed(range(len(num1))):
            for index2 in reversed(range(len(num2))):
                _product = int(num1[index1]) * int(num2[index2])
                _sum = _product + result[index1 + index2 + 1]
                result[index1 + index2] += _sum // 10
                result[index1 + index2 + 1] = _sum % 10
                
        for index, number in enumerate(result): 
            if number != 0: break
                
        return ''.join(map(str, result[index:]))
      

class Solution:
    def multiply(self, num1, num2):
        length1, length2 = len(num1), len(num2)
        result = 0

        for index1, number1 in enumerate(num1):
            for index2, number2 in enumerate(num2):
                x, y = length1-index1-1, length2-index2-1 
                result += int(number1) * int(number2) * pow(10, x) * pow(10, y)
        return str(result)
