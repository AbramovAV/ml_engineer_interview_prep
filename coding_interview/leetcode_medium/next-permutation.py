class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums_len = len(nums)
        k = None
        l = None

        for i in range(nums_len-1, 0, -1):
            if nums[i-1] < nums[i]:
                k = i-1
                break

        if k is None:
            nums[:] = nums[::-1]
        else:
            for i in range(nums_len-1, k, -1):
                if nums[k] < nums[i]:
                    l = i
                    break
            nums[k], nums[l] = nums[l], nums[k]
            nums[k+1:] = nums[:k:-1]