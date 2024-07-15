class Solution(object):
    def lengthOfLongestSubstring(self, s):
        l, size  = 0 , 0
        res = ""

        for r in range(len(s)):
           while s[r] in res:
               l+=1
               res = res[1:]
               
           res += s[r]
           size = max(size, r-l+1)

        return size

               
               
        