# https://leetcode.com/problems/longest-common-subsequence/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]

        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i + 1][j + 1] + 1
                else:
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])
        
        return dp[0][0]

# Example Usage
if __name__ == "__main__":
    sol = Solution()
    text1 = "abcde"
    text2 = "ace"
    print(sol.longestCommonSubsequence(text1, text2))  # Expected output: 3 (LCS is "ace")

    text1 = "abc"
    text2 = "abc"
    print(sol.longestCommonSubsequence(text1, text2))  # Expected output: 3 (LCS is "abc")

    text1 = "abc"
    text2 = "def"
    print(sol.longestCommonSubsequence(text1, text2))  # Expected output: 0 (no common subsequence)