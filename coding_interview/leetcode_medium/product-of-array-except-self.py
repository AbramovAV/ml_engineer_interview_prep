class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        to_return = [1] * len(nums)
        pre = 1
        post = 1
        for i in range(len(nums)):
            to_return[i] = to_return[i] * pre
            pre *= nums[i]
            to_return[-i-1] *= post
            post *= nums[-i-1]
        return to_return