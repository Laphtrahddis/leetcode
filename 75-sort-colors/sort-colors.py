class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        countzero=0
        countone=0
        counttwo=0
        for i in range(n):
            if nums[i]==0:
                countzero+=1
            if nums[i]==1:
                countone+=1
            if nums[i]==2:
                counttwo+=1
        for i in range(countzero):
            nums[i]=0
        for i in range(countzero, countzero + countone):
            nums[i]=1
        for i in range(countzero + countone, countzero + countone + counttwo):
            nums[i]=2