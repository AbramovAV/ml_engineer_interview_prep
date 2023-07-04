class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        carry_bit = False
        idx = 0
        for a_bit, b_bit in zip(a[::-1], b[::-1]):
            if a_bit == b_bit:
                if carry_bit:
                    res += "1"
                else:
                    res += "0"
                carry_bit = (a_bit == "1")
            else:
                if carry_bit:
                    res += "0"
                    carry_bit = True
                else:
                    res += "1"
                    carry_bit = False
            idx += 1

        for bit in max(a, b, key=len)[-idx-1::-1]:
            if carry_bit:
                if bit == "0":
                    res += "1"
                    carry_bit = False
                else:
                    res += "0"
                    carry_bit = True
            else:
                res += bit
        if carry_bit:
            res += "1"
        return res[::-1]
