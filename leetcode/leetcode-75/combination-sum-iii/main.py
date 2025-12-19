# https://leetcode.com/problems/combination-sum-iii/description/?envType=study-plan-v2&envId=leetcode-75

from typing import List

# combinations(1, [])
#  ├─ combinations(2, [1])
#  │   ├─ combinations(3, [1,2])
#  │   │   ├─ combinations(4, [1,2,3])
#  │   │   └─ combinations(4, [1,2])
#  │   └─ combinations(3, [1])
#  │       ├─ combinations(4, [1,3])
#  │       └─ combinations(4, [1])
#  └─ combinations(2, [])
#      ├─ combinations(3, [2])
#      └─ combinations(3, [])


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        
        def backtract(num: int, combination: List[int], cur_sum: int):
            if len(combination) == k and cur_sum == n:
                result.append(combination)
                return
            
            if num > 9:
                return
            
            # include the num
            backtract(num + 1, combination + [num], cur_sum + num)

            # exclude the num
            backtract(num + 1, combination, cur_sum)
        
        backtract(1, [], 0)

        return result



            

# Example usage:
sol = Solution()
print(sol.combinationSum3(3, 7))  # Output: [[1, 2, 4]]
print(sol.combinationSum3(3, 9))  # Output: [[1, 2, 6], [1, 3, 5], [2, 3, 4]]

# 
# Testcase demonstrating the edge case from the prompt:
# k = 9, n = 45
# The expected single combination is [1,2,3,4,5,6,7,8,9]
# Current implementation may return [] due to the order of base-case checks.
k = 9
n = 45
actual = sol.combinationSum3(k, n)
expected = [list(range(1, 10))]

print("Testcase: k=", k, "n=", n)
print("Actual:", actual)
print("Expected:", expected)
print("Match:", actual == expected)