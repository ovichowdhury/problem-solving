from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        m = max(candies)
        for i in candies:
            if i + extraCandies >= m:
                result.append(True)
            else:
                result.append(False)
        return result


if __name__ == "__main__":
    sol = Solution()
    print(sol.kidsWithCandies([4,2,1,1,2], 1))
