class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        from collections import deque
        monotonic_stack = deque()
        days = [0] * len(temperatures)

        for idx, temp in enumerate(temperatures):
            if len(monotonic_stack)==0 or monotonic_stack[-1][1] >= temp:
                monotonic_stack.append((idx, temp))
            else:
                while monotonic_stack and monotonic_stack[-1][1] < temp:
                    old_idx, old_temp = monotonic_stack.pop()
                    days[old_idx] = idx - old_idx
                monotonic_stack.append((idx, temp))
        return days