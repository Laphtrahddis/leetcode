class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left,right=0,len(nums)-1
        count=0
        nums.sort()
        while left<right:
            som=nums[left]+nums[right]
            if(som==k):
                count+=1
                left+=1
                right-=1
            elif(som<k):
                left+=1
            else:
                right-=1
        return count
        