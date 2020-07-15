-- all cities
SELECT c.id, c.name, s.name FROM cities c, states s where s.id = c.state_id ORDER BY c.id ASC;
