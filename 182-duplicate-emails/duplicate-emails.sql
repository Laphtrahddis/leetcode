# Write your MySQL query statement below
select DISTINCT(email) from Person GROUP BY email HAVING COUNT(email) > 1
