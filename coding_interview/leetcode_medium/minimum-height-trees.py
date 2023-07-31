class Solution:
    from collections import deque, defaultdict
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n-1 == 0:
            return [0]
        root_nodes = defaultdict(list)
        self.graph = deque([set() for _ in range(n)])
        for edge in edges:
            self.graph[edge[0]].add(edge[1])
            self.graph[edge[1]].add(edge[0])

        leaves = [i for i in range(n) if len(self.graph[i])==1]

        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                other = self.graph[leaf].pop()
                self.graph[other].remove(leaf)
                if len(self.graph[other]) == 1:
                    new_leaves.append(other)
            leaves = new_leaves
        return leaves