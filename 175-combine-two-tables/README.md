# [175. Combine Two Tables](https://leetcode.com/problems/combine-two-tables/)

**Difficulty:** Easy · **Topic:** SQL · **Solved:** 2026-11-18 · **Language:** MySQL

**Approach:** first JOIN. `LEFT JOIN Address ON Person.personId = Address.personId` keeps every person, and people without an address get `null` for city and state.

**Complexity:** one join between the two tables.
