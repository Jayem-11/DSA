# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev, res = None, True

        def inorder(node):
            if not node: return
            inorder(node.left)
            nonlocal prev, res
            if prev:
                if prev.val >= node.val:
                    res = False
            prev = node
            inorder(node.right)

        inorder(root)
        return res