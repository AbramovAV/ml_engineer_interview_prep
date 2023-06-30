class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        if target < nums[0] or target > nums[-1]:
            return -1
        while low <= high:
            idx = (high+low)//2
            mid = nums[idx]
            if mid < target:
                low = idx + 1
            elif mid > target:
                high = idx - 1
            else:
                return idx
        return -1