# [443. String Compression](https://leetcode.com/problems/string-compression/)

**Difficulty:** Medium · **Topic:** Two Pointers · **Solved:** 2026-11-07 · **Language:** Python3

**Approach:** two pointers on the same list. `i` reads one group of equal letters at a time (the inner loop finds where the group ends, `jumpTo`); `written` writes the letter, then each digit of the group length if it is more than 1, at the front of the list. Writing never overtakes reading, so nothing is overwritten too early. Return `written` as the new length.

**Complexity:** O(n) time (each character is read once by the inner loop), O(1) extra space.

**Lesson:** a Python `for` loop resets `i` every round, so a manual jump needs a `while` loop.
