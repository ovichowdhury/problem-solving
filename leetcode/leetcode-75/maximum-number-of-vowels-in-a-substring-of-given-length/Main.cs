// https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/?envType=study-plan-v2&envId=leetcode-75

Solution solution = new Solution();
// Example usage:
Console.WriteLine(solution.MaxVowels("abciiidef", 3)); // Output: 3
Console.WriteLine(solution.MaxVowels("aeiou", 2)); // Output: 2
Console.WriteLine(solution.MaxVowels("leetcode", 3)); // Output: 2
Console.WriteLine(solution.MaxVowelsOptimized("rhythms", 4)); // Output: 0
Console.WriteLine(solution.MaxVowelsOptimized("tryhard", 4)); // Output: 1

public class Solution
{
    // Time Complexity: O(n * k), where n is the length of the string s and k is the length of the substring.
    // Space Complexity: O(1), since we are using a fixed-size hash set for vowels.
    public int MaxVowels(string s, int k)
    {
        int maxVowels = 0;
        HashSet<char> vowels = new HashSet<char> { 'a', 'e', 'i', 'o', 'u' };

        int left = 0, right = k - 1;

        while (right < s.Length)
        {
            int currentVowels = 0;

            // Count vowels in the current window
            for (int i = left; i <= right; i++)
            {
                if (vowels.Contains(s[i]))
                {
                    currentVowels++;
                }
            }

            maxVowels = Math.Max(maxVowels, currentVowels);

            // Move the window to the right
            left++;
            right++;
        }
        return maxVowels;
    }

    public int MaxVowelsOptimized(string s, int k)
    {
        int maxVowels = 0;
        HashSet<char> vowels = new HashSet<char> { 'a', 'e', 'i', 'o', 'u' };

        int currentVowels = 0;

        for (int i = 0; i < k && i < s.Length; i++)
        {
            if (vowels.Contains(s[i]))
            {
                currentVowels++;
            }
        }

        maxVowels = currentVowels;

        for (int i = k; i < s.Length; i++)
        {
            if (vowels.Contains(s[i]))
            {
                currentVowels++;
            }
            if (vowels.Contains(s[i - k]))
            {
                currentVowels--;
            }

            maxVowels = Math.Max(maxVowels, currentVowels);

            if (maxVowels == k) // Early exit if we reach the maximum possible vowels
            {
                break;
            }
        }

        return maxVowels;
    }
}