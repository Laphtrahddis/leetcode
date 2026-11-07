# [595. Big Countries](https://leetcode.com/problems/big-countries/)

**Difficulty:** Easy · **Topic:** SQL · **Solved:** 2026-11-07 · **Language:** MySQL

**Approach:** first SQL query. `SELECT` the three columns asked for, `FROM` the World table, and keep only rows `WHERE` the area is at least 3,000,000 km² `OR` the population is at least 25,000,000.

**Complexity:** one full scan of the table, O(n) rows.
