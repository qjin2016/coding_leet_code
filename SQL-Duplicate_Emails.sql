# 182,
# https://leetcode.com/problems/duplicate-emails/#/description

# 1
SELECT DISTINCT(P.Email)
FROM Person P
WHERE 1 < (SELECT COUNT(*) FROM Person P2
			WHERE P2.Email = P.Email)

# 2
SELECT Email
FROM Person
Group By Email
HAVING COUNT(*) > 1