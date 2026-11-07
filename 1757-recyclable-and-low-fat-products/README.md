# [1757. Recyclable and Low Fat Products](https://leetcode.com/problems/recyclable-and-low-fat-products/)

**Difficulty:** Easy · **Topic:** SQL · **Solved:** 2026-11-07 · **Language:** MySQL

**Approach:** both `enum('Y','N')` columns must be `'Y'`, so filter with `WHERE ... AND ...` and return `product_id`.

**Complexity:** one full scan of the table, O(n) rows.
