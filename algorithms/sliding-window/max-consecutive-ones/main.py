# max consecutive ones

def find_max_consecutive_ones(nums):
  max_count = 0
  left = 0
  for right in range(len(nums)):
    if nums[right] != 1:
        left = right + 1
    max_count = max(max_count, right - left + 1)
  return max_count

# Example usage:
if __name__ == "__main__":
    nums = [1, 1, 0, 1, 1, 1]
    print(find_max_consecutive_ones(nums))  # Output should be 3
    nums = [0, 0, 0, 0]
    print(find_max_consecutive_ones(nums))  # Output should be 0
    nums = [1, 1, 1, 1]
    print(find_max_consecutive_ones(nums))  # Output should be 4

    nums = [1, 0, 1, 1, 0, 1]
    print(find_max_consecutive_ones(nums))  # Output should be 2
    nums = [0, 1, 1, 0, 1, 1, 1]
    print(find_max_consecutive_ones(nums))  # Output should be 3
    nums = [1, 0, 0, 1, 1, 1, 0, 1]
    print(find_max_consecutive_ones(nums))  # Output should be 3
    nums = [1, 1, 0, 1, 0, 1, 1, 1, 0, 1]
    print(find_max_consecutive_ones(nums))  # Output should be 3
    nums = [0, 1, 0, 1, 0, 1, 0, 1]
    print(find_max_consecutive_ones(nums))  # Output should be 1

    nums = []
    print(find_max_consecutive_ones(nums))  # Output should be 0
    nums = [1]
    print(find_max_consecutive_ones(nums))  # Output should be 1
    