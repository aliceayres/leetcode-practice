"""
175. Combine Two Tables
Table: Person
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| PersonId    | int     |
| FirstName   | varchar |
| LastName    | varchar |
+-------------+---------+
PersonId is the primary key column for this table.
Table: Address
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| AddressId   | int     |
| PersonId    | int     |
| City        | varchar |
| State       | varchar |
+-------------+---------+
AddressId is the primary key column for this table.

Write a SQL query for a report that provides the following information for each
person in the Person table, regardless if there is an address for each of those
people:
FirstName, LastName, City, State

MySQL
# Write your MySQL query statement below

select pr.FirstName,pr.LastName,ad.City,ad.State
from Person pr
left join Address ad on pr.PersonId = ad.PersonId
"""