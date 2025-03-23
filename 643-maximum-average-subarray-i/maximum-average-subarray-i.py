class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        som=0
        for i in range(k):
            som+=nums[i]
        maxsum=som
        n=len(nums)
        for i in range(k,n):
            som=som-nums[i-k]+nums[i]
            maxsum=max(maxsum,som)
        return float(maxsum)/k

