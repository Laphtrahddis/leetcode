# [232. Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/)

**Difficulty:** Easy · **Topic:** Stack & Queue · **Solved:** 2026-11-11 · **Language:** Python3

**Approach:** two stacks with fixed jobs. `push` always goes onto `in_stack`. `pop` and `peek` read from `out_stack`; only when `out_stack` is empty, pour all of `in_stack` into it, which reverses the order so the oldest item is on top.

**Complexity:** amortised O(1) per operation (each item is moved at most once), O(n) space.
