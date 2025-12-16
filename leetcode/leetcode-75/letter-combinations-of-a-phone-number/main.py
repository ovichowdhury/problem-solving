# https://leetcode.com/problems/letter-combinations-of-a-phone-number/?envType=study-plan-v2&envId=leetcode-75

from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        result = []

        def backtract(combination: str):
            if len(combination) == len(digits):
                result.append(combination)
                return

            for d in digits[len(combination):len(combination)+1]:
                for letter in mapping[d]:
                    backtract(combination + letter)

        backtract("")

        return result

       
            

# Example usage:
# sol = Solution()
# print(sol.letterCombinations("23"))  # Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

# Example usage with 1 digits:
# sol = Solution()
# # Output: ["a", "b", "c"]
# print(sol.letterCombinations("2"))

# Example usage with 3 digits:
sol = Solution()
# Output: ["adg", "adh", "adi", "aeg", "aeh", "aei", "afg", "afh", "afi", "bdg", "bdh", "bdi", "beg", "beh", "bei", "bfg", "bfh", "bfi", "cdg", "cdh", "cdi", "ceg", "ceh", "cei", "cfg", "cfh", "cfi"]
print(sol.letterCombinations("234"))

# # Example usage with 4 digits:
# sol = Solution()
# # Output: ["adgj", "adgk", "adgl", "adhj", "adhk", "adhl", "aegj", "aegk", "aegl", "aehj", "aehk", "aehl", "afgj", "afgk", "afgl", "afhj", "afhk", "afhl", "bdgj", "bdgk", "bdgl", "bdhj", "bdhk", "bdhl", "begj", "begk", "begl", "behj", "behk", "behl", "bfgj", "bfgk", "bfgl", "bfhj", "bfhk", "bfhl", "cdgj", "cdgk", "cdgl", "cdhj", "cdhk", "cdhl", "cegj", "cegk", "cegl", "cehj", "cehk", "cehl", "cfgj", "cfgk", "cfgl", "cfhj", "cfhk", "cfhl"]
# print(sol.letterCombinations("2345"))