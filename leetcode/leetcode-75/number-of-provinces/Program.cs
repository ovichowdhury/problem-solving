// https://leetcode.com/problems/number-of-provinces/?envType=study-plan-v2&envId=leetcode-75

// Example Usage (using a jagged array)
var solution = new Solution();
int[][] isConnected = new int[][]
{
    new int[] { 1, 1, 0 },
    new int[] { 1, 1, 0 },
    new int[] { 0, 0, 1 }
};
var result = solution.FindCircleNum(isConnected);
Console.WriteLine(result); // Output: 2

// Solution using jagged array (int[][])
public class Solution
{
  public int FindCircleNum(int[][] isConnected)
  {
    int n = isConnected.Length;
    int[] visited = new int[n];
    int numOfProvinces = 0;
    for (int i = 0; i < n; i++)
    {
      if (visited[i] == 0)
      {
        DFS(isConnected, i, visited);
        numOfProvinces++;
      }
    }
    return numOfProvinces;
  }

  private void DFS(int[][] isConnected, int start, int[] visited)
  {
    visited[start] = 1;
    int cols = isConnected[start].Length;
    for (int n = 0; n < cols; n++)
    {
      if (isConnected[start][n] == 1 && visited[n] == 0)
      {
        DFS(isConnected, n, visited);
      }
    }
  }
}
