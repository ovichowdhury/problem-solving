# https://leetcode.com/problems/decode-string/?envType=study-plan-v2&envId=leetcode-75

# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for char in s:
            if char != "]":
                stack.append(char)
            else:
                chars = ""
                item = stack.pop()
                while item != "[":
                    chars = item + chars
                    item = stack.pop()

                num = stack.pop()
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num

                chars = int(num) * chars

                for c in chars:
                    stack.append(c)


        return "".join(stack)

# Example usage
s = "3[a2[c]]"
solution = Solution()
print(solution.decodeString(s))  # Output: "accaccacc"

s = "2[abc]3[cd]ef"
print(solution.decodeString(s))  # Output: "abcabccdcdcdef"

s = "100[leetcode]"
print(solution.decodeString(s))  # Output: "leetcode" repeated 100 times