# Problem: https://leetcode.com/problems/reverse-words-in-a-string-iii/


# Solution
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join([i[::-1] for i in s.split()])
