"""
180. Consecutive Numbers
Write a SQL query to find all numbers that appear at least three times consecutively.
+----+-----+
| Id | Num |
+----+-----+
| 1  |  1  |
| 2  |  1  |
| 3  |  1  |
| 4  |  2  |
| 5  |  1  |
| 6  |  2  |
| 7  |  2  |
+----+-----+
For example, given the above Logs table, 1 is the only number that appears consecutively
for at least three times.
+-----------------+
| ConsecutiveNums |
+-----------------+
| 1               |
+-----------------+

MySQL
# Write your MySQL query statement below
select distinct(t.Num) as ConsecutiveNums
from Logs t
join Logs lf on t.id = lf.id +1
join Logs rt on t.id = rt.id -1
where t.num = lf.num and t.num = rt.num
"""