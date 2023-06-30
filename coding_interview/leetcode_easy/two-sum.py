class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices_map = {}
        for idx,num in enumerate(nums):
            if (target - num) in indices_map:
                return indices_map[target-num], idx
            if num not in indices_map:
                indices_map[num] = idx