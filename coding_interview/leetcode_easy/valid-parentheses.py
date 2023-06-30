class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        stack = []
        bracket_mapping = {
            "(": ")",
            "[": "]",
            "{": "}"
        }
        for bracket in s:
            if bracket in bracket_mapping:
                stack.append(bracket)
            elif not stack:
                return False
            else:
                if bracket_mapping[stack.pop()] != bracket:
                    return False
        if stack:
            return False
        return True