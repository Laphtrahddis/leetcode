# [387. First Unique Character in a String](https://leetcode.com/problems/first-unique-character-in-a-string/)

**Difficulty:** Easy · **Topic:** Strings · **Solved:** 2026-11-07 · **Language:** Python3

**Approach:** walk the string left to right. Skip characters already known to repeat (kept in `seen`). For a new character, check whether it appears again in the rest of the string; if not, it's the first unique one. If none qualifies, return -1.

**Complexity:** O(n) time, because only lowercase letters are allowed, so at most 26 distinct characters ever trigger the O(n) search (about 26·n). O(1) extra space, since `seen` holds at most 26 letters.
