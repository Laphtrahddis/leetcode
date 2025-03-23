class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """   
        max_sum = float('-inf') #max sum found so far
        curr_sum = 0
        for i in nums:
            curr_sum = curr_sum + i
            if curr_sum > max_sum:
                max_sum = curr_sum
            if curr_sum < 0:
                curr_sum = 0
        return max_sum