class Solution(object):
    def splitArray(self, nums, k):
        def canSplit(mid):
            count, total = 1, 0
            for num in nums:
                total += num
                if total > mid:
                    count += 1
                    total = num
            return count <= k

        low, high = max(nums), sum(nums)
        answer = -1
        while low <= high:
            mid = (low + high) // 2
            if canSplit(mid):
                answer = mid
                high = mid - 1
            else:
                low = mid + 1
        return answer
