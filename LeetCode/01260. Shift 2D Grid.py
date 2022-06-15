class Solution:
    def shiftGrid(self, grid, k):
        for i in range(k):
            m, n = len(grid), len(grid[0])
            ans = [[0] * (n+1) for _ in range(m+1)] # add dim
            for rindex in range(m):
                for cindex in range(n):
                    ans[0][0] = grid[m - 1][n - 1]
                    ans[rindex][cindex + 1] = grid[rindex][cindex]
                    ans[rindex + 1][0] = grid[rindex][n - 1]
            grid = [col[:n] for col in ans[:m]]
        return grid
      
      
# Another Solution
class Solution:
    def shiftGrid(self, grid, k):
        m, n = len(grid), len(grid[0])
        ans = [[0]*n for _ in range(m)] 
        for rindex in range(m):
            for cindex in range(n):
                new_rindex = int((rindex + (cindex + k)/n) % m)
                new_cindex = int((cindex + k) % n)
                print(new_rindex, new_cindex)
                ans[new_rindex][new_cindex] = grid[rindex][cindex]
        return ans
