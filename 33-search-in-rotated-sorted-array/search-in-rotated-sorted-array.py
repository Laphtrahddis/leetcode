class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        split=-1
        n=len(nums)
        if len(nums)==1:
            if nums[0]==target:
                return 0
            else: 
                return -1
        for i in range(len(nums)-1):
            if nums[i+1]<nums[i]:
                split=i
        if split!=-1:
            nums=nums[split+1:n]+nums[0:split+1]
        #print(nums)
        found=-1
        low=0
        high=n-1
        while(low<=high):
            mid=(low+high)//2
            if nums[mid]==target:
                found=mid
                break
            elif nums[mid]<target:
                low=mid+1
            else:
                high=mid-1
        if found==-1:
            return found
        elif split==-1:
            print("debug")
            return found
        else:
            return (found+split+1)%n
        