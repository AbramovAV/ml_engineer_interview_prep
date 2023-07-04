class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        num = mapping[s[-1]]
        for idx in range(len(s)-2, -1, -1):
            if mapping[s[idx]] < mapping[s[idx+1]]:
                num -= mapping[s[idx]]
            else:
                num += mapping[s[idx]]
        return num