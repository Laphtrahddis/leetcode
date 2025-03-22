class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        xor1=0
        xor2=0    #Neutral element for * is 1, +- is 1, and for xor is also 0
        n=len(nums)
        for i in range(n):
            xor1=xor1^nums[i]
        for i in range(n+1):
            xor2=xor2^i
        return xor1^xor2
        