class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        totalSum = 0
        for index,num in enumerate(nums):
            nums[index] = nums[index] + totalSum
            totalSum = nums[index]
        return nums
