# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# iterative solution
class Solution(object):
    def searchBST(self, root, val):
        temp = root
        while temp:
            if temp.val == val:
                return temp
            elif temp.val < val :
                temp = temp.right
            else:
                temp= temp.left
        return None

#recursive solution        
def recursive(self, root, val):
        def rec(root):
            if root:
                if root.val == val: return root
                elif root.val < val: return rec(root.right)
                return rec(root.left)
        
        return rec(root)