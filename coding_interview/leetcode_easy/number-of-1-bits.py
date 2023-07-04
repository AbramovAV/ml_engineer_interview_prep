class Solution:
    def hammingWeight(self, n: int) -> int:
        weights = [
            int("01" * 16, base=2),
            int("0011" * 8, base=2),
            int("00001111" * 4, base=2),
            int(("0" * 8 + "1" * 8) * 2, base=2),
            int("0" * 16 + "1"*16, base=2),
        ]
        for shift, weight in zip([1,2,4,8,16], weights):
            n = (n & weight) + ((n >> shift) & weight)
        return n