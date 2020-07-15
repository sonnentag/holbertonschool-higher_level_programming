-- create database, user, and grant select on new db to new user
-- create database, user, and grant select on new db to new user
CREATE DATABASE IF NOT EXISTS 'hbtn_0d_2';
DROP USER IF EXISTS 'user_0d_2'@'localhost';
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON 'hbtn_0d_2'.* TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;
