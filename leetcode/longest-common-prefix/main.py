# https://leetcode.com/problems/longest-common-prefix/description/

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        max_len = max(map(lambda x: len(x), strs))
        longest_prefix = ""

        for i in range(max_len):
            chars = set()
            for s in strs:
                chars.add(s[i] if i < len(s) else "")
            if len(chars) == 1:
                longest_prefix += chars.pop()
            else:
                break
        return longest_prefix


# Example usage:
sol = Solution()
print(sol.longestCommonPrefix(["flower","flow","flight"]))  # Output: "fl"
print(sol.longestCommonPrefix(["dog","racecar","car"]))     # Output: ""
print(sol.longestCommonPrefix(["interspecies","interstellar","interstate"]))  # Output: "inters"

print(sol.longestCommonPrefix(["cir","car"]))  # Output: "c"