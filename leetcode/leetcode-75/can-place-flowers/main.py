# pylint: skip-file
from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        empty_space = 0
        for i, f in enumerate(flowerbed):
            if i == 0:
                if f == 0 and len(flowerbed) == 1:
                    empty_space += 1
                    continue
                if f == 0 and flowerbed[i + 1] == 0:
                    flowerbed[i] = 1
                    empty_space += 1
                continue
            if i == len(flowerbed) - 1:
                if f == 0 and flowerbed[i - 1] == 0:
                    flowerbed[i] = 1
                    empty_space += 1
                continue
            if f == 0 and flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                empty_space += 1
        if n <= empty_space:
            return True
        else:
            return False
      

sol = Solution()
print(sol.canPlaceFlowers([0], 1))