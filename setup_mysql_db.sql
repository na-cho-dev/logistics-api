-- Create and Setup a database for HealthPixel Project

CREATE DATABASE IF NOT EXISTS logistics_db;
CREATE USER IF NOT EXISTS 'dev'@'localhost' IDENTIFIED BY 'dev';
GRANT ALL PRIVILEGES ON `logistics_db`.* TO 'dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'dev'@'localhost';
FLUSH PRIVILEGES;
