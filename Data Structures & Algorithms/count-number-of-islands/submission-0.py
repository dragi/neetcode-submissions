class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
            count = 0
            seen = set()
            
            def in_bounds(r, c) -> bool:
                return 0 <= r < len(grid) and 0 <= c < len(grid[0])

            def dfs(r, c):
                if not in_bounds(r, c) or (r, c) in seen or grid[r][c] == "0":
                    return

                seen.add((r, c))
                
                directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
                for dr, dc in directions:
                    dfs(r + dr, c + dc)

            for r in range(len(grid)):
                for c in range(len(grid[0])):
                    if (r, c) not in seen and grid[r][c] == "1":
                        count += 1
                        dfs(r, c) 

            return count