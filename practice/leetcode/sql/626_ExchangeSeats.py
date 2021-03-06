"""
626. Exchange Seats
Mary is a teacher in a middle school and she has a table seat storing
students' names and their corresponding seat ids.
The column id is continuous increment.
Mary wants to change seats for the adjacent students.
Can you write a SQL query to output the result for Mary?
+---------+---------+
|    id   | student |
+---------+---------+
|    1    | Abbot   |
|    2    | Doris   |
|    3    | Emerson |
|    4    | Green   |
|    5    | Jeames  |
+---------+---------+
For the sample input, the output is:
+---------+---------+
|    id   | student |
+---------+---------+
|    1    | Doris   |
|    2    | Abbot   |
|    3    | Green   |
|    4    | Emerson |
|    5    | Jeames  |
+---------+---------+
Note:
If the number of students is odd, there is no need to change the last
one's seat.

MySQL
# Write your MySQL query statement below

select t.id id,if(t.id%2=0,ttt.student,ifnull(tt.student,t.student)) student
from seat t
left join seat tt on tt.id = t.id+1 and t.id%2 = 1
left join seat ttt on ttt.id = t.id-1 and t.id%2 = 0
order by t.id asc
"""