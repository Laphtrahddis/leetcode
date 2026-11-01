# [217. Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)

**Difficulty:** Easy · **Topic:** Arrays & Hashing · **Solved:** 2026-11-01 · **Language:** Python3

**Approach:** count each number in a dictionary while scanning; the moment a number is already there, return True. If the loop finishes, there are no duplicates.

**Complexity:** O(n) time, O(n) space for the dictionary.
