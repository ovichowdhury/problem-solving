public class Solution
{
  public int Compress(char[] chars)
  {
    int read = 0, write = 0;
    while (read < chars.Length)
    {
      char currentChar = chars[read];
      int count = 0;
      while (read < chars.Length && chars[read] == currentChar)
      {
        read++;
        count++;
      }
      chars[write++] = currentChar;
      if (count > 1)
      {
        foreach (char digit in count.ToString())
        {
          chars[write++] = digit;
        }
      }
    }
    return write; // Return the new length of the compressed array
  }
}

var solution = new Solution();
var chars = new char[] { 'a', 'a', 'b', 'b', 'c', 'c', 'c' };
var result = solution.Compress(chars);

Console.WriteLine(result); // Output the result of compression