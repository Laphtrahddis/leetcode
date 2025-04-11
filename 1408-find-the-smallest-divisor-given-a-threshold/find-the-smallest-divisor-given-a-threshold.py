def calculate(nums,mid):
    sum_=0
    for i in nums:
        sum_+=(i+mid-1)//mid
    return sum_

class Solution(object):
    def smallestDivisor(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        low,high=1,max(nums)
        answer=-1
        while(low<=high):
            mid=(low+high)//2
            sum_=calculate(nums,mid)
            if sum_<=threshold:
                answer=mid
                high=mid-1
            else:
                low=mid+1
        return answer

        