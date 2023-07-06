"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node:
            queue = [node]
            new_nodes = {}
            while queue:
                node = queue.pop(0)
                if node.val not in new_nodes:
                    new_nodes[node.val] = Node(val=node.val, neighbors=node.neighbors)
                    queue.extend([n for n in node.neighbors])
            for idx, node in new_nodes.items():
                node.neighbors = [
                    new_nodes[n.val] for n in node.neighbors
                ]
            return new_nodes[1]