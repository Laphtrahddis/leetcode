# [35. Search Insert Position](https://leetcode.com/problems/search-insert-position/)

**Difficulty:** Easy · **Topic:** Binary Search · **Solved:** 2026-11-18 · **Language:** Python3

**Approach:** binary search on the half-open range `[start, end)`. Too small → `start = mid + 1`; too big → `end = mid`. If the target is missing, the loop squeezes `start` onto the first value bigger than the target, which is the insert position.

**Complexity:** O(log n) time, O(1) space.
