# https://leetcode.com/problems/determine-if-two-strings-are-close/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        set1 = set(word1)
        set2 = set(word2)

        same_chars = set1 == set2

        same_freqs = sorted(word1.count(c) for c in set1) == sorted(word2.count(c) for c in set2)

        return same_chars and same_freqs

# Example
sol = Solution()
print(sol.closeStrings("abc", "bca"))  # True
print(sol.closeStrings("abc", "def"))  # False
print(sol.closeStrings("aaabbbbccddeeeeefffff", "aaaaabbcccdddeeeeffff"))  # False