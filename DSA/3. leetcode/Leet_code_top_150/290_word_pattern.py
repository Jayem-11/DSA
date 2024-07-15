class Solution(object):
    def wordPattern(self, pattern, s):
        words = s.split(" ")
        if len(pattern) != len(words):
            return False

        mapst, mapts = {},{}
        for c1, c2 in zip(pattern, words):
            if ((c1 in mapst and mapst[c1] != c2) or ( c2 in mapts and mapts[c2] != c1)) :
                return False
            mapst[c1] = c2
            mapts[c2] = c1
        return True 
        
        