class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        ans = []
        for i in range(len(nums)*2):
            ans.append(nums[i%len(nums)])
        return ans
