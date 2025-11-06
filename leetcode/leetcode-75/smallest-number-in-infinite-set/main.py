# https://leetcode.com/problems/smallest-number-in-infinite-set/description/?envType=study-plan-v2&envId=leetcode-75
import heapq

class SmallestInfiniteSet:

    def __init__(self):
        self.current = 1
        self.heap = []
        self.set = set()

    def popSmallest(self) -> int:
        if self.heap:
            smallest = heapq.heappop(self.heap)
            self.set.remove(smallest)
            return smallest
        
        smallest = self.current
        self.current += 1
        return smallest

    def addBack(self, num: int) -> None:
        if num < self.current and num not in self.set:
            heapq.heappush(self.heap, num)
            self.set.add(num)

# Example Usage
if __name__ == "__main__":
    smallestInfiniteSet = SmallestInfiniteSet()
    
    # Test Case 1: Basic operations
    print("Test Case 1:")
    print(f"popSmallest(): {smallestInfiniteSet.popSmallest()}")  # Expected: 1
    print(f"popSmallest(): {smallestInfiniteSet.popSmallest()}")  # Expected: 2
    smallestInfiniteSet.addBack(1)
    print(f"popSmallest(): {smallestInfiniteSet.popSmallest()}")  # Expected: 1
    print(f"popSmallest(): {smallestInfiniteSet.popSmallest()}")  # Expected: 3
    print()