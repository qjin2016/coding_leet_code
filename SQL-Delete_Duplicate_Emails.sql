# 196,
# https://leetcode.com/problems/delete-duplicate-emails/#/description

DELETE p1
FROM Person p1, Person p2 WHERE p1.Email = p2.Email AND p2.Id > p1.Id;