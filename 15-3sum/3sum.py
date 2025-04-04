class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        lst=[]
        n=len(nums)
        for i in range(n):
            if i>0 and nums[i]==nums[i-1]:
                continue
            j=i+1
            k=n-1
            while j<k:
                sum= nums[i]+ nums[j] + nums[k]

                if sum==0:
                    lst.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                    while j<k and nums[j]==nums[j-1]:
                        j+=1
                    while j<k and nums[k]==nums[k+1]:
                        k-=1
                elif sum<0:
                    j+=1
                else:
                    k-=1
        return lst
            
                    
        # n=len(nums)
        # lst=set()
        # for i in range(0,n):
        #     for j in range(i+1,n):
        #         for k in range(j+1,n):
        #             if nums[i]+nums[j]+nums[k]==0:
        #                 temp=[nums[i],nums[j],nums[k]]
        #                 temp.sort()
        #                 triplet=tuple(temp)
        #                 lst.add(triplet)
        # return [list(y) for y in lst]
