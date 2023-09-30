class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        output, first, last = 0, 0, len(mat[0])-1
        for index, array in enumerate(mat):
            output += array[last-index]
            if first+index != last-index:
                output += array[first+index]
        return output
