# 176,
# https://leetcode.com/problems/second-highest-salary/#/description

# create table to test code
create table Employee (ID VARCHAR(20), Salary VARCHAR(20));

INSERT INTO Employee (ID, Salary) VALUES (1, 100);
INSERT INTO Employee (ID, Salary) VALUES (2, 200);
INSERT INTO Employee (ID, Salary) VALUES (3, 300);

DELETE FROM Employee WHERE ID = 2;
DELETE FROM Employee WHERE ID = 3;


# 1,
SELECT 
(SELECT Main.Salary FROM Employee Main
WHERE 2 = (
            SELECT COUNT(*) FROM Employee Aux
            WHERE Main.Salary >= Aux.Salary
)
) SecondHighestSalary; 

# 2,
SELECT
	(
		SELECT Salary FROM Employee
		Order By Salary DESC LIMIT 1, 1
		)
SecondHighestSalary;

# NOTE, query language might different depending on the version, vendor, MySQL/SQL server, etc.