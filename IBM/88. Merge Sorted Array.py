# sol1 
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        index = m
        for i in nums2:
            nums1[index] = i
            index +=1
        nums1.sort()
        

# sol 2
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        k = (m + n) - 1
        while m > 0 and n > 0:
            if nums1[m -1 ] > nums2[n - 1]:
                nums1[k] = nums1[m - 1]
                m -= 1
            else:
                nums1[k] = nums2[n - 1]
                n -=1
            k -= 1
        while n > 0:
            nums1[k] = nums2[n -1]
            n, k = n-1, k-1

# sol 3
class Solution(object):
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