# [1046. Last Stone Weight](https://leetcode.com/problems/last-stone-weight/)

**Difficulty:** Easy · **Topic:** Heap · **Solved:** 2026-11-21 · **Language:** Python3

**Approach:** max-heap via `heapq` with negated weights, so the heaviest stone pops first. Smash the two heaviest while more than two remain, pushing back the difference; then handle the final two (or one) stones directly.

**Complexity:** O(n log n) time, O(1) extra space (heap built in place).
