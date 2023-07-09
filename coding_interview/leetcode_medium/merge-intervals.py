class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []
        intervals.sort()
        low = intervals[0][0]
        high = intervals[0][1]
        for interval in intervals[1:]:
            if interval[0] > high:
                merged.append([low, high])
                low = interval[0]
            high = max(high, interval[1])
        merged.append([low, high])
        return merged