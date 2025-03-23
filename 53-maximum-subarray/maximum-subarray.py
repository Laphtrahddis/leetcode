class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxsum=nums[0]
        j=0
        n=len(nums)
        currsum=0
        while(j<n):
            if currsum<0:
                currsum=0
            currsum+=nums[j]
            maxsum=max(maxsum,currsum)
            j+=1
        return maxsum    