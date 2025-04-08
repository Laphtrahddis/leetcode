class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        low,lb=0,-1
        high=len(nums)-1
        while(low<=high):
            mid=(low+high)//2
            if nums[mid]==target:
                lb=mid
                high=mid-1
            elif nums[mid]>target:
                high=mid-1
            else:
                low=mid+1
        if lb==-1:
            return (-1,-1)
        else:
            low,high=0,len(nums)-1
            up=-1
            while(low<=high):
                mid=(low+high)//2
                if nums[mid]==target:
                    up=mid
                    low=mid+1
                elif nums[mid]<target:
                    low=mid+1
                else:
                    high=mid-1
            return (lb,up)

        