-- creating the hbnb_dv_db database
-- creating the hbnb_dev user
-- adding privileges to the user
CREATE DATABASE IF NOT EXISTS hbnb_dv_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dv_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';