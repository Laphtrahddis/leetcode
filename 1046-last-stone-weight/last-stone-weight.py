class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while(len(stones)>2):
            biggest = -heapq.heappop(stones)
            second_biggest = -heapq.heappop(stones)
            if biggest>second_biggest:
                heapq.heappush(stones, -(biggest - second_biggest))
        if len(stones) == 2:
            biggest = -heapq.heappop(stones)
            second_biggest = -heapq.heappop(stones)
            if biggest == second_biggest:
                return 0
            else:
                return biggest - second_biggest
        if len(stones) == 1:
            return -heapq.heappop(stones)
