class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sets = [[]]
        for i in range(len(nums)):
            new_sets = []
            for subset in sets:
                new_sets.append(subset + [nums[i]])
            sets.extend(new_sets)
        return sets