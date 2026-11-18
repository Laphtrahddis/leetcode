# [100. Same Tree](https://leetcode.com/problems/same-tree/)

**Difficulty:** Easy · **Topic:** Trees · **Solved:** 2026-11-18 · **Language:** Python3

**Approach:** recursion with three base cases: both nodes empty → same; only one empty → different; values differ → different. Otherwise both left subtrees and both right subtrees must be the same.

**Complexity:** O(n) time, O(h) space for the call stack.
