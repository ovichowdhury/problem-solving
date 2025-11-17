# https://leetcode.com/problems/total-cost-to-hire-k-workers/description/?envType=study-plan-v2&envId=leetcode-75

import heapq
from typing import List


class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        tuple_queue = []
        total_cost = 0
        hired = 0
        
        while hired < k:
            n = len(costs)
            if n < candidates:
                for i in range(n):
                    heapq.heappush(tuple_queue, (costs[i], i))
                cost, index = heapq.heappop(tuple_queue)
                total_cost += cost
                del costs[index]
                hired += 1
                tuple_queue = []
                continue

            last_start = n - candidates

            for i in range(candidates):
                heapq.heappush(tuple_queue,(costs[i], i))
            for j in range(last_start, n):
                heapq.heappush(tuple_queue, (costs[j], j))

            cost, index = heapq.heappop(tuple_queue)
            total_cost += cost
            del costs[index]
            hired += 1
            tuple_queue = []

        return total_cost


class Solution2:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        leftq = []
        rightq = []

        l = 0
        r = len(costs) - 1

        for i in range(candidates):
            if l <= r:
                heapq.heappush(leftq, costs[l])
                l += 1
        
        for i in range(candidates):
            if l <= r:
                heapq.heappush(rightq, costs[r])
                r -= 1
        
        total_cost = 0

        for _ in range(k):
            if rightq == [] or (leftq and leftq[0] <= rightq[0]):
                total_cost += heapq.heappop(leftq)

                if l <= r:
                    heapq.heappush(leftq, costs[l])
                    l += 1
            
            else:
                total_cost += heapq.heappop(rightq)

                if l <= r:
                    heapq.heappush(rightq, costs[r])
                    r -= 1
        
        return total_cost

        


# Example usage 
sol = Solution2()
print(sol.totalCost([17,12,10,2,7,2,11,20,8], 3, 4))  # Expected Output: 11
print(sol.totalCost([1,2,4,1], 3, 3))  # Expected Output: 4

