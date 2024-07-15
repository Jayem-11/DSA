class Solution(object):
    def strStr(self, haystack, needle):
        for i in range(len(haystack)):
            if needle == haystack[i : i + (len(needle) )]:
                return i
        return -1