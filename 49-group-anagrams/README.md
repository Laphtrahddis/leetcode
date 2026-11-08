# [49. Group Anagrams](https://leetcode.com/problems/group-anagrams/)

**Difficulty:** Medium · **Topic:** Arrays & Hashing · **Solved:** 2026-11-08 · **Language:** Python3

**Approach:** anagrams have the same letters, so sorting a word's letters gives the same key for all of them (`"eat"`, `"tea"` -> `"aet"`). Use that sorted string as a dictionary key and collect the words in a list under it, then return all the lists.

**Complexity:** O(n · k log k) time for n words of length up to k (sorting each word), O(n · k) space for the dictionary.
