# https://leetcode.com/problems/n-th-tribonacci-number/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def tribonacci(self, n: int) -> int:
        t0 = 0
        t1 = 1
        t2 = 1

        if n == 0:
            return t0
        if n <= 2:
            return t2
        
        for _ in range(3 ,n + 1):
            temp = t0 + t1 + t2
            t0 = t1
            t1 = t2
            t2 = temp
        return t2


# Example usage:
sol = Solution()
print(sol.tribonacci(4))  # Output: 4

# # Another example:
print(sol.tribonacci(25))  # Output: 1389537

# Another example:
print(sol.tribonacci(0))  # Output: 0
print(sol.tribonacci(1))  # Output: 1
print(sol.tribonacci(2))  # Output: 1