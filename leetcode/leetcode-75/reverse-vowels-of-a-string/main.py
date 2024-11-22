# Problem: https://leetcode.com/problems/reverse-vowels-of-a-string/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def reverseVowels(self, st: str) -> str:
        s = list(st)
        vowels = {
            'A': 1,
            'a': 1,
            'E': 1,
            'e': 1,
            'I': 1,
            'i': 1,
            'O': 1,
            'o': 1,
            'U': 1,
            'u': 1
        }
        left = 0
        right = len(s) - 1
        while left < right:
            # print(f"{s[left]} : {s[right]}")
            isLeftVowel = vowels.get(s[left])
            isRightVowel = vowels.get(s[right])
            if isLeftVowel == 1 and isRightVowel == 1:
                t = s[left]
                s[left] = s[right]
                s[right] = t
                left += 1
                right -= 1
            if isLeftVowel == None:
                left += 1
            if isRightVowel == None:
                right -= 1
        return ''.join(s)

s = Solution()
print(s.reverseVowels("leetcode"))      

