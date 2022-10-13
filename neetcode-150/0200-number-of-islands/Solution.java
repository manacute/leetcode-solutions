class Solution {

    private int m, n;
    
    public int numIslands(char[][] grid) {
        int count = 0;
        n = grid.length;
        m = grid[0].length;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[j][i] == '1') {
                    count++;
                    dfs(grid, i, j);
                }
            }
        }
        
        return count;
    }
    
    public void dfs(char[][] grid, int i, int j) {
        if (i < 0 || j < 0 || i >= m || j >= n || grid[j][i] == '0') return;
        grid[j][i] = '0';
        dfs(grid, i + 1, j);
        dfs(grid, i - 1, j);
        dfs(grid, i, j + 1);
        dfs(grid, i, j - 1);
    }
}