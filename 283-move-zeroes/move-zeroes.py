class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        written = 0
        while i < len(nums):
            num = nums[i]
            if num > 0:
                nums[written] = num
                written+=1
            elif num<0:
                nums[written] = num
                written+=1
            i+=1
        j = written 
        while j < len(nums):
            nums[j] = 0
            j+=1
        return nums
