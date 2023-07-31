class Solution:
    from collections import defaultdict
    def longestConsecutive(self, nums: List[int]) -> int:
        counter = dict.fromkeys(nums, 0)
        for num in counter:
            if num+1 in counter:
                counter[num+1] += 1

        start_points = []
        for num in counter:
            if counter[num] == 0:
                start_points.append(num)

        max_seq = 0
        for start_point in start_points:
            point = start_point
            cur_seq = 0
            while point in counter:
                cur_seq += 1
                point += 1
            max_seq = max(max_seq, cur_seq)
        return max_seq