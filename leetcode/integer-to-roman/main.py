# https://leetcode.com/problems/integer-to-roman/description/?envType=problem-list-v2&envId=math

class Solution:
    def intToRoman(self, num: int) -> str:
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]
        syms = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]
        
        roman = ""

        for i in range(len(val)):
            while num >= val[i]:
                roman += syms[i]
                num -= val[i]
        return roman
    
    


# Example usage:
if __name__ == "__main__":
    solution = Solution()
    print(solution.intToRoman(3))    # Output: "III"
    print(solution.intToRoman(4))    # Output: "IV"
    print(solution.intToRoman(9))    # Output: "IX"
    print(solution.intToRoman(58))   # Output: "LVIII"
    print(solution.intToRoman(1994)) # Output: "MCMXCIV"
    print(solution.intToRoman(44))   # Output: "XLIV"