class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = nums[0]
        cur_product = 1
        first_negative = 1
        for num in nums:
            cur_product *= num
            max_product = max(max_product, cur_product)
            if cur_product==0:
                cur_product = 1
                first_negative = 1
                continue

            if cur_product < 0:
                if first_negative==1:
                    first_negative = cur_product
                    continue
                max_product = max(max_product, int(cur_product/first_negative))
            
        return max_product