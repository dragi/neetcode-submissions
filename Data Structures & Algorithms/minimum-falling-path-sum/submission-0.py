class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = matrix[0][:]

        for r in range(1, n):
            new_dp = [0] * n
            for i in range(len(matrix[r])):
                if i == 0:
                    new_dp[i] = min(dp[i], dp[i+1]) + matrix[r][i]
                elif i == n - 1:
                    new_dp[i] = min(dp[i], dp[i-1]) + matrix[r][i]
                else:
                    new_dp[i] = min(dp[i-1], dp[i], dp[i+1]) + matrix[r][i]
            dp = new_dp

        return min(dp)