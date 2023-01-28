class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a, b = list(map(int, a)), list(map(int, b))
        len_a, len_b = len(a), len(b)
        max_len = max(len_a, len_b)

        if len_a > len_b:
            b = (([0] * (len_a - len_b)) + b)
        if len_a < len_b:
            a = (([0] * (len_b - len_a)) + a)
        carry, res = 0, ""

        for i in reversed(range(max_len)):
            if a[i] == 1 and b[i] == 1:
                if carry:
                    res += '1'
                else:
                    res += '0'
                carry = 1
            elif (a[i] == 0 and b[i] == 1) or (a[i] == 1 and b[i] == 0):
                # no change in carry
                if carry:
                    res += '0'
                else:
                    res += '1'
            elif a[i] == 0 and b[i] == 0:
                res += str(carry)
                carry = 0

        if carry:
            res += str(carry)
        return res[::-1]


