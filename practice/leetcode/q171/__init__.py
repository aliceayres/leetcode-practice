"""
177. Nth Highest Salary
Write a SQL query to get the nth highest salary from the Employee table.
+----+--------+
| Id | Salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
For example, given the above Employee table, the nth highest salary where
n = 2 is 200. If there is no nth highest salary, then the query should
return null.
+------------------------+
| getNthHighestSalary(2) |
+------------------------+
| 200                    |
+------------------------+


MySQL

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
      select ifnull((select distinct s.Salary from Employee s
        join (select Salary, @row_num:=@row_num + 1 as rank
            from (SELECT DISTINCT Salary
                  FROM Employee ORDER BY Salary DESC) sc,
             (SELECT @row_num:=0) t ) tmp
        on s.Salary = tmp.Salary and tmp.rank = N)
      ,null)
  );
END
"""