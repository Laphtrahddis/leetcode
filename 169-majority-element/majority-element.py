class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr=nums[0]
        count=0
        for index,i in enumerate(nums):
            if i==curr:
                count+=1
            else:
                count-=1
            if count==0:
                curr=nums[index+1]
        return curr
        
            
             
        