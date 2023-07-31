class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        closest_lower_idx = 0
        closest_upper_idx = -1
        for idx, interval in enumerate(intervals):
            if interval[0] <= newInterval[0] or interval[1] <= newInterval[0]:
                closest_lower_idx = idx
            if interval[0] >= newInterval[1] or interval[1] >= newInterval[1]:
                closest_upper_idx = idx
                break
            closest_upper_idx += 1
        if intervals[closest_lower_idx][0] < newInterval[0] and \
            intervals[closest_lower_idx][1] < newInterval[0]:
            closest_lower_idx += 1
        else:
            newInterval[0] = min(intervals[closest_lower_idx][0], newInterval[0])
        
        if intervals[closest_upper_idx][0] <= newInterval[1]:
            newInterval[1] = max(intervals[closest_upper_idx][1], newInterval[1])
            closest_upper_idx += 1
        return intervals[:closest_lower_idx] + [newInterval] + intervals[closest_upper_idx:]