from typing import List

def bubble_sort(arr: List[int]) -> None:
  for i in range(len(arr) - 1, -1, -1):
    for j in range(i):
      if arr[j] > arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]
  return arr
    


print(bubble_sort([1, 8, 6, 45, 10, -1, -1, 100]))