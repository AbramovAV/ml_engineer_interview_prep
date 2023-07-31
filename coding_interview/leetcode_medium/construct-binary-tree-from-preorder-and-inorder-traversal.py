# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if preorder:
            node = TreeNode(val=preorder[0])
            if inorder:
                inIndex = inorder.index(preorder[0])

                node.left = self.buildTree(preorder[1:1+inIndex], inorder[:inIndex])
                node.right = self.buildTree(preorder[1+inIndex:], inorder[inIndex+1:])
            return node
        return None