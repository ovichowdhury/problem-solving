# https://leetcode.com/problems/roman-to-integer/description/

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        total_sum = 0
        for i in range(len(s) - 1, -1, -1):
            num = roman_map[s[i]]
            if i == len(s) - 1:
                total_sum += num
                continue

            prev_num = roman_map[s[i + 1]]

            if num >= prev_num:
                total_sum += num
            else:
                total_sum -= num
        return total_sum


# Example Usage
if __name__ == "__main__":
    sol = Solution()
    examples = ["III", "IV", "IX", "LVIII", "MCMXCIV"]
    # examples = ["III"]
    for roman in examples:
        print(f"{roman} -> {sol.romanToInt(roman)}")        