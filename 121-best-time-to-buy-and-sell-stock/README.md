# [121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

**Difficulty:** Easy · **Topic:** Sliding Window · **Solved:** 2026-11-08 · **Language:** Python3

**Approach:** one pass left to right. Keep the cheapest price seen so far (the best day to have bought), and on each day check the profit of selling today (`price - cheapest`). Keep the biggest profit.

**Complexity:** O(n) time, O(1) space.
