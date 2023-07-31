class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        max_lens = {}
        for idx in range(len(nums)-1, -1, -1):
            max_next = max(
                (max_lens.get(x,0) if x > nums[idx] else 0 for x in nums[idx+1:]),
                default=0)
            max_lens[nums[idx]] = 1 + max_next
        return max(max_lens.values())