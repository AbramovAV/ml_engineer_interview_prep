class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []
        candidates.sort()
        for idx in range(-1, -len(candidates)-1, -1):
            if (target - candidates[idx]) > 0:
                if (target - candidates[idx]) >= candidates[idx]:
                    other = self.combinationSum(candidates[:idx] + [candidates[idx]], target - candidates[idx])
                else:
                    other = self.combinationSum(candidates[:idx], target - candidates[idx])
                if other:
                    combinations.extend([c + [candidates[idx]] for c in other])
            elif target == candidates[idx]:
                combinations.append([candidates[idx]])
        return combinations