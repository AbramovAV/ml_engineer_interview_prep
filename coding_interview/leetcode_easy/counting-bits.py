class Solution:
    def countBits(self, n: int) -> List[int]:
        num_bits = [0]
        if n >= 1:
            num_bits.append(1)
            add_one = False
            idx = 1
        while len(num_bits) <= n:
            if add_one:
                num_bits.append(num_bits[idx]+1)
                idx += 1
            else:
                num_bits.append(num_bits[idx])
            add_one = not add_one
        return num_bits