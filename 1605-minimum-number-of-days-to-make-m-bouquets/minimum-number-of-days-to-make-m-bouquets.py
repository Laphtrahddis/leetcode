class Solution(object):
    # #m is the number of bouqets and k is the number of adjacent flowers we need to use.
    def calculate(self,bloomDay,mid,m,k):
        count,answer=0,0
        for j in bloomDay:
            if j<=mid:
                count+=1
            else:
                count=0
            if count==k:
                answer+=1
                count=0
        if answer>=m:
            return 1
        else:
            return 0

    def minDays(self, bloomDay, m, k):
        low,high=min(bloomDay),max(bloomDay)
        answer=-1
        while low<=high:
            mid=(low+high)//2
            nom=self.calculate(bloomDay,mid,m,k)
            if nom==1:
                answer=mid
                high=mid-1
            else:
                low=mid+1
        return answer
                      
        
        
        
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        # #m is the number of bouqets and k is the number of adjacent flowers we need to use.
        # for i in range(max(bloomDay)+1):
        #     count=0
        #     answer=0
        #     for j in bloomDay:
        #         if j<=i:
        #             count+=1
        #         else:
        #             count=0
        #             print("reset ho rha hai", i)
        #         if count==k:
        #             answer+=1
        #             count=0
        #     if answer>=m:
        #         return i
        # return -1

        