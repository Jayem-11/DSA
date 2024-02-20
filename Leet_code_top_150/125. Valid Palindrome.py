import re
class Solution(object):
    def isPalindrome(self, s):
        s = re.sub(r'\W|_', '', s.lower())
        l = 0
        r = len(s)-1

        while l <= r:
            if s[l] != s[r]:
                return False

            l += 1
            r -= 1
        return True
        


        