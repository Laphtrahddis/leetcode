class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: listt[int]
        :type nums2: listt[int]
        :rtype: listt[listt[int]]
        """
        listt=[[],[]]
        for i in nums1:
            if i not in nums2 and i not in listt[0]:
                listt[0].append(i)
        for i in nums2:
            if i not in nums1 and i not in listt[1]:
                listt[1].append(i)
        return listt
        