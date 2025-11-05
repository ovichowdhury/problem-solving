# https://leetcode.com/problems/kth-largest-element-in-an-array/?envType=study-plan-v2&envId=leetcode-75

from typing import List
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        return heapq.heappop(heap)


# Example Usage
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1: Basic example
    print("Test Case 1:")
    nums1 = [3, 2, 1, 5, 6, 4]
    k1 = 2
    result1 = solution.findKthLargest(nums1, k1)
    print(f"nums = {nums1}, k = {k1}")
    print(f"2nd largest element: {result1}")
    print(f"Expected: 5\n")
    
    # Test Case 2: Array with duplicates
    print("Test Case 2:")
    nums2 = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k2 = 4
    result2 = solution.findKthLargest(nums2, k2)
    print(f"nums = {nums2}, k = {k2}")
    print(f"4th largest element: {result2}")
    print(f"Expected: 4\n")
    
    # Test Case 3: Single element
    print("Test Case 3:")
    nums3 = [1]
    k3 = 1
    result3 = solution.findKthLargest(nums3, k3)
    print(f"nums = {nums3}, k = {k3}")
    print(f"1st largest element: {result3}")
    print(f"Expected: 1\n")
    
    # Test Case 4: All same elements
    print("Test Case 4:")
    nums4 = [7, 7, 7, 7, 7]
    k4 = 3
    result4 = solution.findKthLargest(nums4, k4)
    print(f"nums = {nums4}, k = {k4}")
    print(f"3rd largest element: {result4}")
    print(f"Expected: 7\n")
    
    # Test Case 5: Large array
    print("Test Case 5:")
    nums5 = [7, 10, 4, 3, 20, 15]
    k5 = 3
    result5 = solution.findKthLargest(nums5, k5)
    print(f"nums = {nums5}, k = {k5}")
    print(f"3rd largest element: {result5}")
    print(f"Expected: 10\n")
    
    
