class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #n=len(nums)
        dict={}
        for i in nums:
            if i not in dict:
                dict[i]=1
            else:
                dict[i]+=1
        lst=[]
        for key,value in dict.items():
            if value>len(nums)//3:
                lst.append(key)
        return lst
        