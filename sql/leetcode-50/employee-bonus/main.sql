-- https://leetcode.com/problems/employee-bonus/?envType=study-plan-v2&envId=top-sql-50
select name, bonus 
from employee left join bonus
on employee.empId = bonus.empId
where bonus < 1000 or bonus is null;
