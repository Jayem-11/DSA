
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        res = []
        q = deque([root])
        count = 0
        while q:
            qlen = len(q)
            level = []

            for i in range(qlen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.right)
                    q.append(node.left)

            if level:
                if count % 2 == 0:
                    res.append(level[::-1])
                else:
                    res.append(level)

            count += 1

        return res
        

