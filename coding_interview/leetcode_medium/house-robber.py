class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        else:
            nums = [0,0,0] + nums
            for i in range(3, len(nums)):
                nums[i] += max(nums[i-3], nums[i-2])
            return max(nums[-1], nums[-2])