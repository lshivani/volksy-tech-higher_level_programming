-- create database and user
CREATE DATABASE IF NOT EXISTS hbtn_0d_2 ;
CREATE USER user_0d_2 IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON 'user_0d_2'@'localhost';
