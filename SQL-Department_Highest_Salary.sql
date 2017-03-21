# 184,
# https://leetcode.com/problems/department-highest-salary/#/description


# the following code will only preserve one max values 
-- SELECT Department.Name AS Department, newemp.ename AS Employee, newemp.esa AS Salary
-- FROM 
-- (SELECT Employee.Id AS eid, MAX(Employee.Salary) AS esa, Employee.DepartmentId AS edid, Employee.Name as ename
-- 	FROM Employee
-- GROUP BY Employee.DepartmentId ) newemp JOIN Department
-- ON newemp.edid = Department.Id

SELECT dp_max_salary_with_name.Department AS Department, Employee.Name AS Employee, dp_max_salary_with_name.Salary AS Salary
FROM 
(SELECT Department.Name AS Department, dp_max_salary.Salary AS Salary, Department.Id AS DepartmentId FROM
(SELECT DepartmentId, MAX(Salary) AS Salary FROM Employee GROUP BY DepartmentId) dp_max_salary 
JOIN Department ON Department.Id = dp_max_salary.DepartmentId) dp_max_salary_with_name
JOIN Employee ON Employee.DepartmentId = dp_max_salary_with_name.DepartmentId AND Employee.Salary = dp_max_salary_with_name.Salary