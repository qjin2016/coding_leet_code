# 178,
# https://leetcode.com/problems/rank-scores/#/description

SELECT S1.Score AS Score, (SELECT COUNT(DISTINCT(S2.score)) + 1 FROM Scores S2

WHERE S2.score > S1.score) AS Rank

FROM Scores S1

ORDER BY Score DESC