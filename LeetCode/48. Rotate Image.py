#  myPow(34.00515 , -3)
class Solution:
  def rotate(self, matrix):
    for min in range(len(matrix) // 2):
      max = len(matrix) - min - 1
      for i in range(min, max):
        offset = i - min
        top = matrix[min][i]
        matrix[min][i] = matrix[max - offset][min]
        matrix[max - offset][min] = matrix[max][max - offset]
        matrix[max][max - offset] = matrix[i][max]
        matrix[i][max] = top
    #return matrix
    
    
    
from copy import deepcopy
class Solution:
    def rotate(self, matrix):
        tmp, rows = deepcopy(matrix), len(matrix)
        for row in range(rows):
            for col in range(rows):
                matrix[row][col] = tmp[(rows-1)-col][row]
        #return matrix]
        
        
class Solution:
    def rotate(self, matrix):
        matrix.reverse()
        rows, columns = len(matrix), len(matrix[0])
        for row in range(rows):
            for column in range(row):
            #for column in range(row, columns):
                matrix[row][column], matrix[column][row] = matrix[column][row], matrix[row][column]
        #return matrix
        
