class Solution(object):
    def rangeBitwiseAnd(self, left, right):
        i = 0
        while left != right:
            left >>=1
            right >>=1
            i += 1
        return right << i

        