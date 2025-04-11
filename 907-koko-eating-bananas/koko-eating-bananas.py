class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        def calculate(piles,mid):
            sumtime=0
            for i in piles:
                sumtime+=(i+mid-1)//mid
            return sumtime
        low=1
        answer=1
        high=max(piles)
        while(low<=high):
            mid=(low+high)//2
            nom=calculate(piles,mid)
            if nom<=h:
                answer=mid
                high=mid-1
            elif nom>h:
                low=mid+1
        return answer

        