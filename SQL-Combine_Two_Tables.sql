# 175,
# https://leetcode.com/problems/combine-two-tables/#/description
# Table A contains information about name and ID;
# Table B contains address info
# combine two tables

SELECT FirstName, LastName, City, State 
FROM Person P LEFT JOIN Address A 
ON P.PersonId = A.PersonId