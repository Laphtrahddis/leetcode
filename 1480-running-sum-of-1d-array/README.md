# [1480. Running Sum of 1d Array](https://leetcode.com/problems/running-sum-of-1d-array/)

**Difficulty:** Easy · **Topic:** Prefix sum · **Solved:** 2026-10-27 (prep setup day) · **Language:** Python3

**Approach:** keep a running total and overwrite each element with itself plus the total so far.

**Complexity:** O(n) time, O(1) extra space (updates `nums` in place).
