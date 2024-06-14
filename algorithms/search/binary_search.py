
import math
from typing import List


def binary_search(arr: List[int], value: int, left, right: int) -> int:
  if right >= left:
    mid = math.ceil((right + left) / 2)
    if(arr[mid] == value):
      return mid
    elif(value > arr[mid]):
      return binary_search(arr, value, mid + 1, right)
    else:
      return binary_search(arr, value, left, mid - 1)
  else:
    return -1
  

print(binary_search([1, 2, 3, 4, 5, 10], 3, 0, 5))