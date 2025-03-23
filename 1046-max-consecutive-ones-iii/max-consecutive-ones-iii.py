class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # i=0
        # j=0
        # count=0
        # maxcount=0
        # n=len(nums)
        # while(j<n):
        #     if nums[j]==1:
        #         count+=1
        #         j+=1
        #     elif nums[j]==0:
        #         if k>0:
        #             count+=1
        #             j+=1
        #             k-=1
        #         else:
        #             if nums[i]==1:
        #                 i+=1
        #                 count-=1
        #                 j+=1
        #             else:
        #                 i+=1
        #                 j+=1
        #                 k+=1
        #     maxcount=max(maxcount,count)
        # return maxcount

        i,j=0,0
        n=len(nums)
        maxcount=0
        while(j<n):
            if nums[j] == 0:
                k-=1 
            while k<0:
                if nums[i]==0:
                    k+=1
                i+=1
            maxcount=max(maxcount,j-i+1)
            j+=1
        return maxcount
            