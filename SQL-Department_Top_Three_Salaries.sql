# 185,
# https://leetcode.com/problems/department-top-three-salaries/#/description

SELECT D.Name AS Department, E.Name AS Employee, E.Salary AS Salary 
FROM Employee E INNER JOIN Department D ON E.DepartmentId = D.Id 
WHERE (SELECT COUNT(DISTINCT(Salary)) FROM Employee 
       WHERE DepartmentId = E.DepartmentId AND Salary > E.Salary) < 3
ORDER by E.DepartmentId, E.Salary DESC;