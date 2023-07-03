# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        longest_path = 0
        if root:
            if root.left:
                longest_path += self.getHeight(root.left)
            if root.right:
                longest_path += self.getHeight(root.right)
            longest_path = max(
                longest_path,
                self.diameterOfBinaryTree(root.right),
                self.diameterOfBinaryTree(root.left))
        return longest_path

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