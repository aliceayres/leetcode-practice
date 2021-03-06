"""
601. Human Traffic of Stadium
X city built a new stadium, each day many people visit it and the stats are saved
as these columns: id, date, people
Please write a query to display the records which have 3 or more consecutive rows
and the amount of people more than 100(inclusive).
For example, the table stadium:
+------+------------+-----------+
| id   | date       | people    |
+------+------------+-----------+
| 1    | 2017-01-01 | 10        |
| 2    | 2017-01-02 | 109       |
| 3    | 2017-01-03 | 150       |
| 4    | 2017-01-04 | 99        |
| 5    | 2017-01-05 | 145       |
| 6    | 2017-01-06 | 1455      |
| 7    | 2017-01-07 | 199       |
| 8    | 2017-01-08 | 188       |
+------+------------+-----------+
For the sample data above, the output is:
+------+------------+-----------+
| id   | date       | people    |
+------+------------+-----------+
| 5    | 2017-01-05 | 145       |
| 6    | 2017-01-06 | 1455      |
| 7    | 2017-01-07 | 199       |
| 8    | 2017-01-08 | 188       |
+------+------------+-----------+
Note:
Each day only have one row record, and the dates are increasing with id increasing.

MySQL
# Write your MySQL query statement below

select tt.id,tt.date,tt.people
from stadium tt
where tt.id in
(select distinct t.id
from stadium t
join stadium lf on lf.id = t.id-1
join stadium rt on rt.id = t.id+1
where t.people >= 100 and lf.people>= 100
and rt.people >= 100)
or tt.id in (select distinct lf.id
from stadium t
join stadium lf on lf.id = t.id-1
join stadium rt on rt.id = t.id+1
where t.people >= 100 and lf.people>= 100
and rt.people >= 100)
or tt.id in (select distinct rt.id
from stadium t
join stadium lf on lf.id = t.id-1
join stadium rt on rt.id = t.id+1
where t.people >= 100 and lf.people>= 100
and rt.people >= 100)
order by tt.id asc
"""