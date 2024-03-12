class Solution(object):
    def isHappy(self, n):
        
        mem = set()

        while n not in mem:
            mem.add(n)
            n = sum([int(i) ** 2 for i in str(n)])

        return n== 1