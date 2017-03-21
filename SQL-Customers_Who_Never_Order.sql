# 183,
# https://leetcode.com/problems/customers-who-never-order/#/description


# 1
SELECT Name AS Customers FROM
Customers
WHERE Id NOT IN (SELECT CustomerId FROM Orders)


# 2
SELECT Customers.Name AS Customers 
FROM (Customers LEFT JOIN Orders ON Customers.Id = Orders.CustomerId) WHERE Orders.CustomerId IS NULL

