# https://leetcode.com/problems/max-consecutive-ones/?envType=problem-list-v2&envId=dsa-linear-shoal-array-i


from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        current_count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                current_count += 1
                max_count = max(max_count, current_count)
            else:
                current_count = 0

        return max_count


# Example Usage
if __name__ == "__main__":
    solution = Solution()
    nums = [1,1,0,1,1,1]
    result = solution.findMaxConsecutiveOnes(nums)
    print(result)  # Expected output: 3