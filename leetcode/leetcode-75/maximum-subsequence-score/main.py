# https://leetcode.com/problems/maximum-subsequence-score/?envType=study-plan-v2&envId=leetcode-75

from typing import List
from itertools import combinations
import heapq

# Time Complexity: O(n!/k!(n-k)!) * k
# Space Complexity: O(k)
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        indices = [i for i in range(len(nums1))]
        comb = combinations(indices, k)
        max_score = 0
        for c in comb:
            sum_nums1 = sum(nums1[i] for i in c)
            min_nums2 = min(nums2[i] for i in c)
            score = sum_nums1 * min_nums2
            max_score = max(max_score, score)
        return max_score

class Solution2:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = sorted(zip(nums2, nums1), reverse=True)
        sum_nums1 = 0
        max_score = 0
        heap = []
        for n2, n1 in pairs:
            heapq.heappush(heap, n1)
            sum_nums1 += n1

            if len(heap) > k:
                sum_nums1 -= heapq.heappop(heap)
            
            if len(heap) == k:
                score = sum_nums1 * n2
                max_score = max(max_score, score)

        return max_score



# Example usage:
sol = Solution2()
result = sol.maxScore([1,3,3,2], [2,1,3,4], 3)
print(result)  # Expected output: 12