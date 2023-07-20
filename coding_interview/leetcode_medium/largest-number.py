class Solution:
    from functools import cmp_to_key
    def largestNumber(self, nums: List[int]) -> str:
        def cmp_func(x,y):
            left = x+y
            right = y+x
            if left<right:
                return 1
            elif left > right:
                return -1
            else:
                return 0
        nums = [str(num) for num in nums]
        nums.sort(key=cmp_to_key(cmp_func))
        if all([x=="0" for x in nums]):
            return "0"
        else:
            return "".join(nums)