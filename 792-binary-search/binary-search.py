class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def binary_search(nums,target,low,high):
            if low>high:
                return -1
            mid=(low+high)/2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                return binary_search(nums,target,low,mid-1)
            else:
                return binary_search(nums,target,mid+1,high)

        low=0
        high=len(nums)-1
        return binary_search(nums,target,low,high)

        