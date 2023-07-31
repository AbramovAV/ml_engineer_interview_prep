class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diff = [g-c for g,c in zip(gas, cost)]
        starting_idx = 0
        cur_gas = 0
        sum = 0
        for i in range(len(diff)):
            cur_gas += diff[i]
            sum += diff[i]
            if cur_gas < 0:
                cur_gas = 0
                starting_idx = i + 1
        if sum < 0:
            return -1
        return starting_idx