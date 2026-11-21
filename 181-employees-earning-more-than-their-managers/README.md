# [181. Employees Earning More Than Their Managers](https://leetcode.com/problems/employees-earning-more-than-their-managers/)

**Difficulty:** Easy · **Topic:** SQL · **Solved:** 2026-11-22 · **Language:** MySQL

**Approach:** correlated subquery with aliases. The outer `Employee e` is the employee being checked; the inner `Employee m` looks up the row whose `id` equals `e.managerId` and returns the manager's salary. Employees with no manager (`managerId` is NULL) get NULL from the subquery, and `salary > NULL` is never true, so they're skipped.

**Complexity:** one subquery lookup per employee (a self-join does the same in one pass).
