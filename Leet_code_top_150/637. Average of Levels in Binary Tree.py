# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        s = defaultdict(float)
        t = defaultdict(int)

        def dfs(node, h):
            if not node: return

            dfs(node.left, h+1)
            dfs(node.right, h+1)
            s[h] += node.val
            t[h] += 1

        dfs(root, 0)

        output = []
        for i in range(len(s)):
            output.append(s[i]/t[i])

        return output
