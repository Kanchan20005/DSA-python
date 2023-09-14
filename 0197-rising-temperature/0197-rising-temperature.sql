# Write your MySQL query statement below
SELECT A.id
FROM Weather A, Weather B
WHERE 
DATEDIFF(A.recordDate, B.recordDate) =1
and A.temperature> B.temperature