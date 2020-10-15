# Write your MySQL query statement below
select max(Salary) SecondHighestSalary
from Employee
where Salary < (select max(Salary) from Employee);

select
    ifnull(
        (select distinct Salary
        from Employee 
        order by Salary desc
        limit 1,1),
    null) as SecondHighestSalary;