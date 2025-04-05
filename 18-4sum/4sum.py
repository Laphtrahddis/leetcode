class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        n=len(nums)
        st=set()
        for i in range(n-3):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,n-2):
                k,l=j+1,n-1
                while(k<l):
                    sum_=nums[i]+nums[j]+nums[k]+nums[l]
                    if sum_==target:
                        st.add((nums[i], nums[j], nums[k], nums[l]))
                        k += 1      
                        l -= 1
                    elif sum_<target:
                        k+=1
                    else:
                        l-=1
        return list(st)

        