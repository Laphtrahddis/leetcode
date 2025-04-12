def shippable(weights,mid,days):
    countdays=0
    som=0
    for i in weights:
        som+=i
        if som>mid:
            countdays+=1
            som=i
    if som>0:
        countdays+=1
    if countdays>days:
        return False
    else:
        return True
class Solution(object):
    def shipWithinDays(self, weights, days):
        #weights.sort()
        low=max(weights)
        high=sum(weights)
        answer=-1
        while(low<=high):
            mid=(low+high)//2
            value=shippable(weights,mid,days)
            if value==True:
                answer=mid
                high=mid-1
            else:
                low=mid+1
        return answer
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        
        