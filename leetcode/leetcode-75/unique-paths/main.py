# https://leetcode.com/problems/unique-paths/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]

        # init 1 for 1st row
        for i in range(m):
            dp[i][0] = 1

        # init 1 for 1st col
        for j in range(n):
            dp[0][j] = 1
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m - 1][n - 1] 

# Example Usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.uniquePaths(3, 7))  # Expected output: 28
    print(sol.uniquePaths(3, 2))  # Expected output: 3