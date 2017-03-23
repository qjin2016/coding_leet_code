# 262,
# https://leetcode.com/problems/trips-and-users/#/description

SELECT t.Day AS Day, ROUND(SUM(if(t.Status <> 'completed', 1, 0)) / COUNT(*), 2) AS 'Cancellation Rate' FROM


(SELECT Client_Id, Status, Request_at AS Day FROM Trips WHERE Request_at BETWEEN '2013-10-01' AND '2013-10-03') t

INNER JOIN 

(SELECT Users_Id FROM Users WHERE Banned = 'No') u

ON u.Users_Id = t.Client_Id

GROUP BY t.Day

