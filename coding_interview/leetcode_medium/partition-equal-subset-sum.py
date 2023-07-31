class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2:
            return False
        
        total_sum //= 2
        dp = [True] + [False] * total_sum

        for num in nums:
            for j in range(total_sum, num-1, -1):
                dp[j] = dp[j] or dp[j-num]

        return dp[total_sum]