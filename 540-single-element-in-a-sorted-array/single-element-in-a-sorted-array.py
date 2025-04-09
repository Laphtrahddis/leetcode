class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return nums[0]
        n=len(nums)
        if nums[0]!=nums[1]:
            return nums[0]
        if nums[n-1]!=nums[n-2]:
            return nums[n-1]
        low,high=0,len(nums)-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]!=nums[mid-1] and nums[mid]!=nums[mid+1]:
                return nums[mid]
            elif (nums[mid]==nums[mid+1] and mid%2==1) or (nums[mid]==nums[mid-1] and mid%2==0):
                high=mid-1
            else:
                low=mid+1
        return -1

        