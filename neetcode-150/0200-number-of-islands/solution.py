class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        
        def dfs(grid, i, j) :
            if i < 0 or j < 0 or i >= m or j >= n or grid[j][i] == '0':
                return

            grid[j][i] = '0';
            dfs(grid, i + 1, j);
            dfs(grid, i - 1, j);
            dfs(grid, i, j + 1);
            dfs(grid, i, j - 1);
        
        count = 0
        for j, row in enumerate(grid):
            for i, num in enumerate(row):
                if num == "1":
                    dfs(grid, i, j)
                    count += 1
        return count