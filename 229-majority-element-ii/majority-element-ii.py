class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        dict={}
        lst=[]
        for i in nums:
            if i not in dict:
                dict[i]=1
            else:
                dict[i]+=1
            if dict[i]==(n//3)+1:
                    lst.append(i)
        return lst