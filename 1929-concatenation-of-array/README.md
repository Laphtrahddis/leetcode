# [1929. Concatenation of Array](https://leetcode.com/problems/concatenation-of-array/)

**Difficulty:** Easy · **Topic:** Arrays · **Solved:** 2026-10-30 (Day 1) · **Language:** Python3

**Approach:** loop over 2n positions and take `nums[i % n]`, so the index wraps back to the start for the second copy.

**Complexity:** O(n) time, O(n) space for the output. (One-liner alternative: `return nums + nums`.)
