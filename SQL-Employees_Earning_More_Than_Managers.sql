# 181,
# https://leetcode.com/problems/employees-earning-more-than-their-managers/#/description

# 1,
SELECT Name AS Employee
FROM Employee e
WHERE e.ManagerId IS NOT NULL AND e.Salary > (SELECT e2.Salary FROM Employee e2 WHERE e2.Id = e.ManagerId)

# 2,
SELECT e.Name AS Employee 
FROM Employee e LEFT JOIN Employee e2 
ON e.ManagerId = e2.Id
WHERE e.Salary > e2.Salary