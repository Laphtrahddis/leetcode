# [125. Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)

**Difficulty:** Easy · **Topic:** Two Pointers · **Solved:** 2026-11-07 · **Language:** Python3

**Approach:** build a new list with only letters and digits (never pop from a list while looping over it), lowercase it, and compare it with its reverse.

**Complexity:** O(n) time, O(n) extra space for the cleaned list and its reverse. (Follow-up: two pointers from both ends, skipping non-alphanumerics, gets O(1) space.)
