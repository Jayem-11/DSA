# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Recursive solution
class Solution(object):
    def isSymmetric(self, root):
        def dfs(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False

            return (left.val == right.val and dfs(left.left, right.right) and dfs(left.right, right.left))
        return dfs(root.left, root.right)
        
# Iterative solution

class Solution(object):
    def isSymmetric(self, root):
        if not root:
            return True

        stack = [(root.left, root.right)]

        while stack:
            l, r = stack.pop()
            if not l and not r:
                continue
            if not l or not r or (l.val != r.val):
                return False
            stack.append((l.left, r.right))
            stack.append((l.right, r.left))
        return True
            