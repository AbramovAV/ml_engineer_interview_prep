class Solution:
    def decodeString(self, s: str) -> str:
        decoded = ""
        idx = 0
        num_brackets = 0
        start_idx = 0
        digit = ""
        while idx < len(s):
            if not digit and s[idx].isalpha():
                decoded += s[idx]
            elif s[idx].isdigit() and not num_brackets:
                digit += s[idx]
            elif s[idx] == "[":
                if not num_brackets:
                    start_idx = idx
                num_brackets += 1
            elif s[idx] == "]":
                num_brackets -= 1
                if not num_brackets:
                    decoded += int(digit) * self.decodeString(s[start_idx+1:idx])
                    digit = ""
            idx += 1
        return decoded