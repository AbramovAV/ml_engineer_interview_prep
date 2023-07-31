class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        combinations = []
        for digit in digits:
            max_pos = len(combinations)
            if max_pos:
                for i in range(max_pos):
                    for letter in mapping[digit]:
                        combinations.append(combinations[i] + letter)
                combinations = combinations[max_pos:]
            else:
                combinations = list(mapping[digit])
        return combinations
            