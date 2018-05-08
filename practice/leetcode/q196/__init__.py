"""
196. Delete Duplicate Emails
Write a SQL query to delete all duplicate email entries in a table named Person,
keeping only unique emails based on its smallest Id.
+----+------------------+
| Id | Email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
| 3  | john@example.com |
+----+------------------+
Id is the primary key column for this table.
For example, after running your query, the above Person table should have the
following rows:
+----+------------------+
| Id | Email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
+----+------------------+

MySQL
# Write your MySQL query statement below
delete from Person where Id not in
(select tt.id from (select min(t.id) as id
from Person t group by t.Email) tt )

# ① You can't specify target table 'Person' for update in FROM clause
# ② min(id)
"""