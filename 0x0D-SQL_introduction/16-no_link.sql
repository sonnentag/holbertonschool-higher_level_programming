-- say my name (return list of scores who have name info included)
SELECT score,name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
