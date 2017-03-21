# 177,
# https://leetcode.com/problems/nth-highest-salary/#/description

# to have function in mysql:
# 1st, type: delimiter $$
# 2nd, type function
# 3rd, end with $$

# to use function in mysql:
# 1st, type: delimiter ;
# 2nd, type function and parameter

CREATE FUNCTION getNthHighestSalary(N INT) 
RETURNS INT
BEGIN
RETURN (
		SELECT MAX(Main.Salary) FROM Employee Main
		WHERE (N-1) = (
					SELECT COUNT(DISTINCT(Aux.salary)) FROM Employee Aux
					WHERE Main.Salary < Aux.Salary)
);
END

CREATE FUNCTION getNthHighestSalary(N INT) 
RETURNS INT
BEGIN
RETURN (
		SELECT MIN(Main.Salary) FROM Employee Main
		WHERE N = (
					SELECT COUNT(DISTINCT(Aux.salary)) FROM Employee Aux
					WHERE Main.Salary > Aux.Salary)
);
END

