-- MySQL setup test - prepares a MySQL server for test the project
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
GRANT ALL PRIVILEGES ON hbnb_test .* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
