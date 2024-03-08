class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        
        for i in t:
            if i not in s:
                return False
            s = s.replace(i , "", 1)

        return True
        