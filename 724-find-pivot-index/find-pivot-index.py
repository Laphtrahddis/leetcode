class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        presums=[]
        presums.append(0)
        lsum=0
        for i in range(1,len(nums)):
            lsum+=nums[i-1]
            presums.append(lsum)
        postsums = [0] * len(nums)
        psum=0
        for i in range(len(nums)-2,-1,-1):
            psum+=nums[i+1]
            postsums[i]=psum
        for i in range(len(nums)):
            if postsums[i]==presums[i]:
                return i
        return -1




        
        