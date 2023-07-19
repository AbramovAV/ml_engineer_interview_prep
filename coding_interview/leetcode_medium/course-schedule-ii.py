class Solution:
    from collections import deque
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        nodes, order, queue = {n:{"in":0, "out":set()} for n in range(numCourses)}, [], deque()        
        for out_course, in_course in prerequisites:
            nodes[out_course]["in"] += 1
            nodes[in_course]["out"].add(out_course)
        
        for id in nodes:
            if nodes[id]["in"] == 0:
                queue.append(id)

        while queue:
            id = queue.pop()
            for out in nodes[id]["out"]:
                nodes[out]["in"] -= 1
                if not nodes[out]["in"]:
                    queue.append(out)
            order.append(id)
        
        if len(order) < len(nodes):
            return []
        return order