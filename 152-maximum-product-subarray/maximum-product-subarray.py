class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # pre,suf=1,1
        # n=len(nums)
        # prefix=[]
        # suffix=[]
        # prefix.append(0)
        # for i in range(n-1):
        #     pre=pre*nums[i]
        #     prefix.append(pre)
        # suffix.append(0)
        # for i in range(n-1,0,-1):
        #     suf=suf*nums[i]
        #     suffix.append(suf)
        # maxreturn=-9999999999999999999999
        # for i in range(n):
        #     if nums[i]<0:
        #         maxreturn=max(maxreturn,max(suffix[i],prefix[i]))
        # return maxreturn
        n=len(nums)
        pre,suf=0,0
        maxi=-99999999999999999
        for i in range(n):
            if pre==0:
                pre=1
            if suf==0:
                suf=1
            pre=pre*nums[i]
            suf=suf*nums[n-1-i]
            maxi=max(maxi,max(suf,pre))
        return maxi