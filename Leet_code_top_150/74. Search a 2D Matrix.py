class Solution(object):
    def searchMatrix(self, matrix, target):
        if not matrix or target is None:
            return False
        rows, cols = len(matrix), len(matrix[0])
        l, r = 0, rows*cols - 1
        
        while l <= r:
            m = (l + r)/2
            num = matrix[m/cols][m%cols]

            if num == target:
                return True

            elif num < target:
                l = m +1

            else:
                r = m-1
        return False

        

        