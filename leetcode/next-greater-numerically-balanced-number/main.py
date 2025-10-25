# https://leetcode.com/problems/next-greater-numerically-balanced-number/description/

class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        if n == 0:
            return 1
        for i in range(n + 1, 10 ** (n + 1)):
            if self.isBalanced(i):
                return i

    def isBalanced(self, x: int) -> bool:
        ht = {}
        while x > 0:
            digit = x % 10
            if digit in ht:
                ht[digit] += 1
            else:
                ht[digit] = 1
            x = x // 10

        for key, value in ht.items():
            if key != value:
                return False
        return True


# Example usage
sol = Solution()
print(sol.nextBeautifulNumber(1))    # expected 22
print(sol.nextBeautifulNumber(1000)) # expected 1333
print(sol.nextBeautifulNumber(3000)) # expected 3133