// https://leetcode.com/problems/unique-paths/description/

function uniquePaths(m: number, n: number): number {
  let dp: number[][] = [];
  for (let i = 0; i < m; i++) {
    dp[i] = Array(n).fill(0);
  }

  for (let i = 0; i < m; i++) {
    dp[i][0] = 1; // First column
  }

  for (let j = 0; j < n; j++) {
    dp[0][j] = 1; // First row
  }

  for (let i = 1; i < m; i++) {
    for (let j = 1; j < n; j++) {
      dp[i][j] = dp[i - 1][j] + dp[i][j - 1]; // Sum of paths from top and left
    }
  }

  return dp[m - 1][n - 1]; // Return the bottom-right corner value
}

console.log(uniquePaths(3, 2)); // Example usage, should return 3
