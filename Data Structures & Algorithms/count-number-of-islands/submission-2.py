class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1,0], [0,1], [-1, 0], [0,-1]]

        def dfs(r, c):
            if 0 > r or r >= len(grid) or 0 > c or c >= len(grid[0]) or grid[r][c] == "0":
                return
            grid[r][c] = "0"

            for dr, dc in directions:
                dfs(r + dr, c + dc)

        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    dfs(r, c)
                    count += 1
        return count