
from typing import List


def insertion_sort(arr: List[int]) -> None:
  for k in range(len(arr)):
    v = arr[k]
    j = k
    while(arr[j - 1] > v and j >= 1):
      arr[j] = arr[j - 1]
      j -= 1
    arr[j] = v
  return arr


print(insertion_sort([1, 8, 6, 45, 10, -1, -1, 100]))