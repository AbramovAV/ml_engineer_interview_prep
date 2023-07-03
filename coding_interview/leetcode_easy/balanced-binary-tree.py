# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None or \
            root.left is None and root.right is None:
            return True
        elif root.left is None:
            return (root.right.right is None and root.right.left is None)
        elif root.right is None:
            return (root.left.right is None and root.left.left is None)
        else:
           if abs(self.getHeight(root.left) - self.getHeight(root.right)) > 1:
               return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def getHeight(self, root:TreeNode, cur_height:int=1) -> int:
        if root.left is None and root.right is None:
            return cur_height
        else:
            left_height = right_height = cur_height + 1
            if root.left is not None:
                left_height = self.getHeight(root.left, left_height)
            if root.right is not None:
                right_height = self.getHeight(root.right, right_height)
            return max(left_height, right_height)