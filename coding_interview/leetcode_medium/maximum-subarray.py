class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        cur_sum = 0
        left_idx = 0
        right_idx = 0
        while right_idx < len(nums):
            if cur_sum < 0 and (nums[right_idx] > cur_sum):
                left_idx = right_idx
                cur_sum = 0
            cur_sum += nums[right_idx]
            if cur_sum > max_sum:
                max_sum = cur_sum
            elif nums[left_idx] < 0 and right_idx > left_idx:
                cur_sum -= nums[left_idx]
                left_idx += 1
                if cur_sum > max_sum:
                    max_sum = cur_sum
            right_idx += 1
        return max_sum