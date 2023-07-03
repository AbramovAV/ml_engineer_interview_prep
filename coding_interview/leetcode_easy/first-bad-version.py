# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low = 1
        high = n
        is_bad_idx = 1
        while low <= high:
            mid = (low + high) // 2
            if isBadVersion(mid):
                is_bad_idx = mid
                high = mid - 1
            else:
                low = mid + 1
        return is_bad_idx