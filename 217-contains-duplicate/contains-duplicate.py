class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        dictionary = {}
        for num in nums:
            if not dictionary.get(num):
                dictionary[num] = 1
            else:
                dictionary[num] = dictionary[num] + 1
                return True
        return False
