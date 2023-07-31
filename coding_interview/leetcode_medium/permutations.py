class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        for idx in range(len(nums)):
            other = self.permute(nums[:idx]+nums[idx+1:])
            if not other:
                permutations.append([nums[idx]])
            else:
                permutations.extend(
                    [
                        [nums[idx]]+p for p in other
                    ]
                )
        return permutations