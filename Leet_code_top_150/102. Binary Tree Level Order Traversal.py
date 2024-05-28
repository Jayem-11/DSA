# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        queue = deque([root])
        out = []
        while queue:
            qlen = len(queue)
            level = []
            for i in range(qlen):
                root = queue.popleft()
                if root:
                    level.append(root.val)
                    queue.append(root.left)
                    queue.append(root.right)
            if level:
                out.append(level)
        return out




        