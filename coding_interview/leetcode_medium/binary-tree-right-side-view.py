# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        from collections import deque
        vals = []
        if root:
            stack = deque([(1, root)])
            while stack:
                level, root = stack.pop()
                if level > len(vals):
                    vals.append(root.val)
                if root.left:
                    stack.append((level+1, root.left))
                if root.right:
                    stack.append((level+1, root.right))
        return vals