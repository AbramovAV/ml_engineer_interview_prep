class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1/x
            n *= -1
        elif n == 0:
            return 1
        res = x
        powers = []
        while n > 1:
            powers.append(n)
            n //= 2
        cur_pow = 1
        for power in powers[::-1]:
            res *= res
            cur_pow *= 2
            if power - cur_pow == 1:
                res *= x
                cur_pow += 1
        return res