class Solution(object):
    def merge(self, intervals):
        intervals.sort()
        answer=[]
        answer.append(intervals[0])
        for i in range(1,len(intervals)):
            if answer[-1][1]>=intervals[i][0]:
                if intervals[i][1]>answer[-1][1]:
                    answer[-1][1]=intervals[i][1]
            else:
                answer.append(intervals[i])
        return answer
        
        
        
        
        
        
        
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # intervals.sort()
        # nums1=[]
        # n=len(intervals)
        # nums2=[]
        # n=len(intervals)
        # for i in range(n):
        #     nums1.append(intervals[i][0])
        #     nums2.append(intervals[i][1])
        # for i in range(1,n):
        #     if i<n and i>0 and nums1[i]<=nums2[i-1]:
        #         if nums2[i]>nums2[i-1]:
        #             nums2.pop(i-1)
        #         else:
        #             nums2.pop(i)
        #         nums1.pop(i)
        #         n=n-1
        # ans=[]
        # for i in range(n):
        #     temp=[nums1[i],nums2[i]]
        #     ans.append(temp)
        # return ans
               

        