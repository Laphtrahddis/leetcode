# [226. Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/)

**Difficulty:** Easy · **Topic:** Trees · **Solved:** 2026-11-18 · **Language:** Python3

**Approach:** recursion. Base case: an empty node returns `None`. Otherwise swap the left and right children (`a, b = b, a`), invert each subtree, and return the node.

**Complexity:** O(n) time (each node once), O(h) space for the call stack, where h is the tree height.
