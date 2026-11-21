# [182. Duplicate Emails](https://leetcode.com/problems/duplicate-emails/)

**Difficulty:** Easy · **Topic:** SQL · **Solved:** 2026-11-22 · **Language:** MySQL

**Approach:** `GROUP BY email` makes one group per email, and `HAVING COUNT(email) > 1` keeps only the groups with more than one row. `COUNT` can't go in `WHERE`, because `WHERE` checks one row at a time, before any grouping. (`DISTINCT` is optional here, since `GROUP BY` already returns each email once.)

**Complexity:** one pass to group the rows.
