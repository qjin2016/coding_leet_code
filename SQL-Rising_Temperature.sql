# 197,
# https://leetcode.com/problems/rising-temperature/#/description
SELECT w2.Id FROM Weather w1, Weather w2 
WHERE datediff(w2.Date, w1.Date) = 1 AND w1.Temperature < w2.Temperature