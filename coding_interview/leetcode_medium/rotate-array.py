class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k % len(nums) != 0:
            k %= len(nums)

            first_half = len(nums)-k
            for i in range(1, first_half//2+1):
                nums[i-1], nums[first_half-i] = nums[first_half-i], nums[i-1]

            for i in range(1, k//2+1):
                nums[i-1+first_half], nums[len(nums)-i] = nums[len(nums)-i], nums[i-1+first_half]

            for i in range(1, len(nums)//2+1):
                nums[i-1], nums[len(nums)-i] = nums[len(nums)-i], nums[i-1]