-- list all cities cntained in database
SELECT cities.id,cities.name,states.name FROM cities INNER JOIN states ON cities.states.id=states.id;
