# [11. Container With Most Water](https://leetcode.com/problems/container-with-most-water/)

**Difficulty:** Medium · **Topic:** Two Pointers · **Solved:** 2026-11-07 · **Language:** Python3

**Approach:** start with the widest container (pointers at both ends). Area = shorter line × width; keep the max. Then move the pointer at the shorter line inward: moving the taller one can never help, because the width shrinks and the height is still capped by the shorter line.

**Complexity:** O(n) time, O(1) extra space.
