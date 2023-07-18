class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diff = [g-c for g,c in zip(gas, cost)]
        if sum(diff)<0:
            return -1
        starting_idx = 0
        visited = [False for _ in diff]
        cur_gas = 0
        idx = -1
        gas_len = len(gas)
        while True:
            idx = (idx+1)%gas_len
            new_idx = (idx+1)%gas_len
            visited[idx] = True
            cur_gas += diff[idx]
            if cur_gas < 0:
                if visited[new_idx]==True:
                    return -1
                else:
                    starting_idx = new_idx
                    cur_gas = 0
            elif new_idx == starting_idx:
                return starting_idx