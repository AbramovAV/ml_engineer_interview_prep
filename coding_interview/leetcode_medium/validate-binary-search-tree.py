# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root:
            stack = []
            nums = []
            node = root
            while stack or node is not None:
                if node is not None:
                    stack.append(node)
                    node = node.left
                else:
                    node = stack.pop()
                    nums.append(node.val)
                    node = node.right
            for idx in range(1, len(nums)):
                if nums[idx - 1] >= nums[idx]:
                    return False
        return True