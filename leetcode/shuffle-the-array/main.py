# https://leetcode.com/problems/shuffle-the-array/description/?envType=problem-list-v2&envId=dsa-linear-shoal-array-i

from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        shift_bits = 10  # Since nums[i] <= 1000, we can use 10 bits to store each number
        mask = (1 << shift_bits) - 1  # Mask to extract the last 10 bits

        # print(bin(mask))  # Debug: print the binary representation of the mask

        for i in range(n):
            nums[i] = nums[i] | nums[i + n] << shift_bits
        
        print(nums)
        

# Example Usage
if __name__ == "__main__":
    solution = Solution()
    nums = [2,5,1,3,4,7]
    n = 3
    result = solution.shuffle(nums, n)
    print(result)  # Expected output: [2,3,5,4,1,7]
