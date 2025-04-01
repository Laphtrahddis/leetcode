class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        preSum,cnt=0,0
        dic={}
        dic[0]=1
        for i in nums:
            preSum+=i
            remove=preSum-k
            if remove in dic:
                cnt+=dic[remove]
            if preSum in dic:
                dic[preSum]+=1
            else:
                dic[preSum]=1
        return cnt

        
        