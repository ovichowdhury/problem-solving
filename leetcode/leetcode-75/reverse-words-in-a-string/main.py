# Problem: https://leetcode.com/problems/reverse-words-in-a-string/?envType=study-plan-v2&envId=leetcode-75

import re

class Solution:
    def reverseWords(self, s: str) -> str:
        mystr = s.strip()
        mystr = re.sub("\s\s+", " ", mystr)
        mystr_list = mystr.split()
        mystr_list = mystr_list[::-1]
        return " ".join(mystr_list)

s = Solution()
print(s.reverseWords("a good   example"))  