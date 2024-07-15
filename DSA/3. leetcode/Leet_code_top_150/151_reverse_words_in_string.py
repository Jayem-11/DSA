class Solution(object):
    def reverseWords(self, s):

        words = s.split()
        res = ""
        for i in range(len(words)-1,-1,-1):
            if i == 0:
                 res += words[i]
                 return res
            res += words[i] + " "
        return res

        