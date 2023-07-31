class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        from collections import Counter
        triplets = set()
        nums = Counter(nums)
        for first in nums:
            for second in nums:
                if -first-second in nums:
                    unique = Counter([first, second, -first-second])
                    if all(nums[n]>=unique[n] for n in unique):
                        triplets.add(tuple(sorted([first, second, -first-second])))
        return list(triplets)