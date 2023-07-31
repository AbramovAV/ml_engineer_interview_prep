class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0
        ptr = 0
        num = 0
        sign = 1
        while ptr < len(s)-1 and s[ptr] == " ":
            ptr += 1
        
        if s[ptr] == "-":
            sign = -1
            ptr += 1
        elif s[ptr] == "+":
            ptr += 1

        while ptr < len(s) and s[ptr].isdigit():
            num = num*10 + (ord(s[ptr]) - 48)
            ptr += 1

        if num * sign < -2**31:
            return -2**31
        elif num * sign > 2**31 - 1:
            return 2**31 - 1
        else:
            return num * sign