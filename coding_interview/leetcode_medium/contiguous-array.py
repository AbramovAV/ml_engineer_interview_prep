class Solution:
    from collections import defaultdict
    def findMaxLength(self, nums: List[int]) -> int:
        sums_pos = defaultdict(list)
        prefix_sum = 0
        for idx, num in enumerate(nums):
            if num:
                prefix_sum += 1
            else:
                prefix_sum -= 1
            sums_pos[prefix_sum].append(idx)

        max_len = 0
        if 0 in sums_pos:
            max_len = sums_pos[0][-1] + 1
            del sums_pos[0]

        for prefix_sum in sums_pos:
            min_odd, max_odd = None, 0
            min_even, max_even = None, 0
            for s in sums_pos[prefix_sum]:
                if s%2:
                    if min_odd is None:
                        min_odd = s
                    max_odd = s
                else:
                    if min_even is None:
                        min_even = s
                    max_even = s

            if min_odd is not None:
                max_len = max(max_len, max_odd-min_odd)
            if min_even is not None:
                max_len = max(max_len, max_even-min_even)
        return max_len