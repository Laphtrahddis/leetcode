# [167. Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)

**Difficulty:** Medium · **Topic:** Two Pointers · **Solved:** 2026-11-07 · **Language:** Python3

**Approach:** because the array is sorted, start one pointer at each end. Sum too small: move the left pointer right (bigger number). Too big: move the right pointer left. Equal: return the 1-based indexes.

**Complexity:** O(n) time, O(1) extra space (vs O(n) space for the hash-map Two Sum).
