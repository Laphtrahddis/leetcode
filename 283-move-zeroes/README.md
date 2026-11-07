# [283. Move Zeroes](https://leetcode.com/problems/move-zeroes/)

**Difficulty:** Easy · **Topic:** Two Pointers · **Solved:** 2026-11-07 · **Language:** Python3

**Approach:** read pointer `i` scans the list; write pointer `written` copies every non-zero number forward, keeping their order. Then fill everything from `written` to the end with zeros. Same read/write-pointer trick as String Compression.

**Complexity:** O(n) time, O(1) extra space.
