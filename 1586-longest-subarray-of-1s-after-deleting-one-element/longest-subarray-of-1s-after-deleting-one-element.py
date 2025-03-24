class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i,j=0,0
        maxlen=0
        flag=0
        n=len(nums)
        for j in range(n):
            if nums[j]==0:
                flag+=1
            while flag>1:
                if nums[i]==0:
                    flag-=1
                    i+=1
                else:
                    i+=1
            maxlen=max(maxlen,j-i)

        return maxlen

            
            
