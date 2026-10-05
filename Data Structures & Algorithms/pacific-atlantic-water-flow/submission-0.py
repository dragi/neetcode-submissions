class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()
        directions = [[1,0], [0,1], [-1,0], [0,-1]]

        def in_bounds(r, c):
            return 0 <= r < ROWS and 0 <= c < COLS

        def dfs(r, c, seen, previousHeight):
            if (r, c) in seen or not in_bounds(r, c) or previousHeight > heights[r][c]:
                return
            seen.add((r, c))

            for dr, dc in directions:
                dfs(r + dr, c + dc, seen, heights[r][c])

        for c in range(COLS):            
            dfs(0, c, pacific, heights[0][c])
            dfs(ROWS - 1, c, atlantic, heights[ROWS - 1][c])
        
        for r in range(ROWS):            
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, COLS - 1, atlantic, heights[r][COLS - 1])

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in atlantic and (r, c) in pacific:
                    res.append([r, c]) 
        
        return res
        
        
