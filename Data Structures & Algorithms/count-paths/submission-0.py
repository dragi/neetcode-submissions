class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[None for _ in range(n)] for _ in range(m)]

        def dfs(r, c):
            if r == m - 1 and c == n - 1:
                return 1
            
            if dp[r][c] is not None:
                return dp[r][c]
            
            res = 0
            if r < m - 1:
                res += dfs(r + 1, c)
            if c < n - 1:
                res += dfs(r, c + 1)

            dp[r][c] = res
            return res

        return dfs(0, 0)