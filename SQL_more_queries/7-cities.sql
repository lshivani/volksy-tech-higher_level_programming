--creates database table cities
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities(id INT NOT NULL AUTO_GENERATED,state_id INT NOT NULL,name VARCHAR(256) NOT NULL,PRIMARY KEY(id),FOREIGN KEY(state_id) REFERENCES state(state_id));