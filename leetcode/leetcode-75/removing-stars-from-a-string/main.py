# https://leetcode.com/problems/removing-stars-from-a-string/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for char in s:
            if char == '*':
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(char)
        return ''.join(stack)


# Example usage
s = "leet**cod*e"
solution = Solution()
print(solution.removeStars(s))  # Output: "lecoe"

s = "erase*****"
print(solution.removeStars(s))  # Output: ""