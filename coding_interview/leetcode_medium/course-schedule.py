class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import deque
        nodes, order, queue = {}, [], deque()
        
        for n in range(numCourses):
            nodes[n] = {"in":0, "out":set()}
        
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
            return False

        return True