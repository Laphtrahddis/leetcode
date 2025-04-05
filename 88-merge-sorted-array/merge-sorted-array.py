class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i,j=m-1,0
        while i>=0 and j<n:
            if nums1[i]>nums2[j]:
                nums1[i],nums2[j]=nums2[j],nums1[i]
                i-=1
                j+=1
            else:
                break
        nums2.sort()
        #nums1[0:m].sort()
        #print(nums1)
        nums1[:m] = sorted(nums1[:m])

        for i in range(m,m+n):
            nums1[i]=nums2[i-m]

        