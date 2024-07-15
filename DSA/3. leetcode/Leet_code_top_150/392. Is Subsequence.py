class Solution(object):

    def isSubsequence(self, s, t):
        if len(s) > len(t):return False
        if len(s) == 0:return True
        l = 0
        for r in range(len(t)):
            if l <= len(s) - 1:
                if s[l] == t[r]:
                    l += 1
        return l == len(s)
           