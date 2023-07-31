# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        from collections import deque
        pathes = []
        if root:
            stack = deque()
            cur_path = deque()
            cur_sum = 0
            stack.append((0, root))
            while stack:
                level, node = stack.pop()
                if len(cur_path)>0 and cur_path[-1][0] >= level:
                    while cur_path[-1][0] >= level:
                        _, old_val = cur_path.pop()
                        cur_sum -= old_val
                cur_path.append((level, node.val))
                cur_sum += node.val

                if node.left is None and node.right is None:
                    if cur_sum == targetSum:
                        pathes.append([p[1] for p in cur_path])
                if node.right is not None:
                    stack.append((level+1, node.right))
                if node.left is not None:
                    stack.append((level+1, node.left))

        return pathes