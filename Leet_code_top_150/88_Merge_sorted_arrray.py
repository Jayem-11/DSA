class Solution:
    def merge(self, nums1, m, nums2, n):
        
        a, b, index = m-1, n-1, m + n - 1

        while b >= 0:
            if a>=0 and nums1[a] > nums2[b]:
                nums1[index] = nums1[a]
                a-=1
            else:
                nums1[index] = nums2[b]
                b-=1

            index-=1
        """
        Do not return anything, modify nums1 in-place instead.
        """
        