# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:     
        nodes = []
        if root:
            stack = [(0, root)]
            to_add = []
            cur_level = 0
            while stack:
                level, node = stack.pop(0)
                if level > cur_level:
                    cur_level += 1
                    nodes.append(to_add)
                    to_add = []
                to_add.append(node.val)
                if node.left:
                    stack.append((level+1, node.left))
                if node.right:
                    stack.append((level+1, node.right))
            if to_add:
                nodes.append(to_add)
        return nodes