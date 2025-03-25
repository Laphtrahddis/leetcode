class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: listt[int]
        :type nums2: listt[int]
        :rtype: listt[listt[int]]
        """
        nums1set,nums2set=set(nums1),set(nums2)
        set1,set2=set(),set()
        for i in nums1set:
            if i not in nums2set:
                set1.add(i)
        for i in nums2set:
            if i not in nums1set:
                set2.add(i)
        return [list(set1),list(set2)]
        