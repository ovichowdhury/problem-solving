# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
import math

def guess(num: int) -> int:
    pass


class Solution:
    def guessNumber(self, n: int) -> int:
        def search(start: int, end: int) -> int:
            pivot = math.ceil((start + end) / 2)
            res = guess(pivot)
            if res == -1:
                return search(start, pivot)
            elif res == 1:
                return search(pivot, end)
            else:
                return pivot
        return search(0, n)
        