class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        increasing=0
        n=len(nums)
        if nums[0]>=nums[len(nums)-1]:
            increasing=0
        else:
            increasing=1
        if increasing==1:
            for i in range(n-1):
                if nums[i]>nums[i+1]:
                    return False
                else:
                    continue
            return True
        if increasing==0:
            for i in range(n-1):
                if nums[i]<nums[i+1]:
                    return False
                else:
                    continue
            return True

        

        