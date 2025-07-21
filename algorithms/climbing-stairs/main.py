# Problem: Climbing Stairs
# You are climbing a staircase. It takes n steps to reach the top. Each time you can either climb 1 step or 2 steps.
#
# How many distinct ways can you climb to the top?

def climb_stairs(n: int) -> int:
  if n <= 1:
    return 1
  dp = [0] * (n + 1)
  dp[0] = 1
  dp[1] = 1
  for i in range(2, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]
  return dp[n]

# Example usage:
if __name__ == "__main__":
  n = 5  # Example input
  print(f"Number of distinct ways to climb {n} stairs: {climb_stairs(n)}")
