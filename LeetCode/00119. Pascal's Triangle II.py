class Solution:
    def getRow(self, rowIndex: int):
        rowIndex += 1
        out = [1] * rowIndex
        for x in range(2, rowIndex):
            for y in range(1, x):
                z = x-y
                out[z] += out[z-1]
        return out
