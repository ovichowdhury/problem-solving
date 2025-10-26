-- https://leetcode.com/problems/classes-with-at-least-5-students/description/?envType=study-plan-v2&envId=top-sql-50
select class from courses
group by class
having count(student) >= 5;