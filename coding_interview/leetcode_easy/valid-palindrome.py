class Solution:
    def isPalindrome(self, s: str) -> bool:
        alnumstr = ""
        for char in s:
            if char.isalnum():
                alnumstr += char.lower()
        alnumstr_len = len(alnumstr)
        if alnumstr_len < 2 or \
            (alnumstr[:alnumstr_len//2] == alnumstr[-(alnumstr_len//2):][::-1]):
            return True
        return False