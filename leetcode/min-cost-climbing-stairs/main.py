""" problem: https://leetcode.com/problems/min-cost-climbing-stairs """

from typing import List


# pylint: disable=invalid-name
def minCostClimbingStairs(cost: List[int]) -> int:
    """ Top level method """
    memo = {}
    def min_cost_climbing_stairs(index: int, cost: List[int]) -> int:
        """Find the min cost"""
        if index >= len(cost):
            return 0
        if index == len(cost) - 1:
            return cost[index]
        if memo.get(index):
            return memo.get(index)
        t1 = min_cost_climbing_stairs(index + 1, cost)
        t2 = min_cost_climbing_stairs(index + 2, cost)
        memo[index + 1] = t1
        memo[index + 2] = t2
        m = min(t1, t2)
        return cost[index] + m
    return min(min_cost_climbing_stairs(0, cost), min_cost_climbing_stairs(1, cost))


print(minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))
