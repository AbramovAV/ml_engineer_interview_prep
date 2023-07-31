# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root:
            if root.val == p.val or root.val == q.val:
                return root
            left_res = self.lowestCommonAncestor(root.left, p, q)
            right_res = self.lowestCommonAncestor(root.right, p, q)
            if left_res is not None and right_res is not None:
                return root
            elif left_res is not None and right_res is None:
                return left_res
            elif left_res is None and right_res is not None:
                return right_res
            else:
                return None