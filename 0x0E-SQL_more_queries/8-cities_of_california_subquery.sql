-- list cities from Cali
SELECT c.id,c.name FROM cities c, states s WHERE c.state_id = s.id AND s.name = 'California';
