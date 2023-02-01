-- list cities of california
SELECT id, name FROM cities  WHERE state.id=(SELECT id FROM states name='california')ORDER BY id ASC;
