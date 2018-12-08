-- To import your schemas into your database, run:
-- `cd app && cat schema.sql | yasha -v config.yaml
--                           | mysql -u <username> -p <database>`
-- from the project directory
-- where <username> is your MySQL username and <database> is the MySQL
-- database of interest.


-- Create Database.
DROP DATABASE IF EXISTS {{ MYSQL_DATABASE }};
CREATE DATABASE {{ MYSQL_DATABASE }};
use {{ MYSQL_DATABASE }};

-- Setup db user.
FLUSH PRIVILEGES;
DROP USER IF EXISTS {{ MYSQL_USERNAME }};
CREATE USER {{ MYSQL_USERNAME }} 
    IDENTIFIED WITH mysql_native_password BY '{{ MYSQL_PASSWORD }}';
GRANT ALL ON {{ MYSQL_DATABASE }}.* TO {{ MYSQL_USERNAME }};
FLUSH PRIVILEGES;

-- Setup tables.
CREATE TABLE Users (
    email VARCHAR(32) NOT NULL UNIQUE,

    first_name VARCHAR(32) NOT NULL,
    surname VARCHAR(32) NOT NULL,

    verified BIT(1),
        -- NULL unverified
        -- +1 user verified
        -- +1 manager verified

    password VARCHAR(255) NOT NULL,

    PRIMARY KEY (email)
);

CREATE TABLE Products (
    id INT NOT NULL,
    name INT NOT NULL,

    PRIMARY KEY (id)
);

CREATE TABLE Sites (
    id INT NOT NULL AUTO_INCREMENT,
    name INT NOT NULL,
    address VARCHAR(256) NOT NULL,

    PRIMARY KEY (id)
);

CREATE TABLE Stock (
    id INT NOT NULL AUTO_INCREMENT,
    product_id INT NOT NULL,
    site_id INT NOT NULL,
    stock_healthy BOOLEAN,
        -- NULL = ordered
        -- false = low
        -- true = healthy

    PRIMARY KEY (id),
    FOREIGN KEY (product_id) REFERENCES Products(id),
    FOREIGN KEY (site_id) REFERENCES Stock(id)
);
