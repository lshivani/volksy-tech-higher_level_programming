-- list no of records with same record
SELECT score, COUNT(*) as number FROM second_table GROUP BY socre ORDER BY number DESC;
