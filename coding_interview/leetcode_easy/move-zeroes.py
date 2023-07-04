class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zero_idx = []
        for i in range(len(nums)):
            if nums[i] != 0:
                non_zero_idx.append(i)
        for idx, j in enumerate(non_zero_idx):
            nums[idx] = nums[j]
        for i in range(len(non_zero_idx), len(nums)):
            nums[i] = 0