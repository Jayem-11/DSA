# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res, count = None, 1

        def dfs(node):
            if not node: return 

            dfs(node.left)
            nonlocal res, count
            if count == k:
                res = node.val 
            count += 1
            dfs(node.right)
        dfs(root)

        return res