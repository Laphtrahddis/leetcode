class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # arr=[]
        # pos=1
        # i=0
        # while i<len(nums):
        #     if pos==1 and nums[i]>0:
        #         arr.append(nums[i])
        #         nums.pop(i)
        #         pos=0
        #         i+=1
        #         continue
        #     if pos==0 and nums[i]<0:
        #         arr.append(nums[i])
        #         nums.pop(i)
        #         pos=1
        #         i+=1
        #         continue
        # return arr
        arr=[]
        nums1 = [i for i in nums if i > 0]
        nums2 = [i for i in nums if i < 0]
        for i in range(len(nums1)):
            arr.append(nums1[i])
            arr.append(nums2[i])
        return arr
