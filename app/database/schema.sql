CREATE TABLE Users(
    email VARCHAR(32) NOT NULL UNIQUE,
    first_name VARCHAR(32) NOT NULL,
    surname VARCHAR(32) NOT NULL,
    password VARCHAR(255) NOT NULL,
    PRIMARY KEY (email)
);

CREATE TABLE Temp_users(
    email VARCHAR(32) NOT NULL UNIQUE,
    first_name VARCHAR(32) NOT NULL,
    surname VARCHAR(32) NOT NULL,
    password VARCHAR(255) NOT NULL,

    user_verified BOOLEAN DEFAULT FALSE,
    manager_verified BOOLEAN DEFAULT FALSE,

    PRIMARY KEY (email)
);

CREATE TABLE Products(
    id VARCHAR(32) NOT NULL,
    name VARCHAR(32) NOT NULL,
    order_qty INT NOT NULL,
    cossh VARCHAR(2083),

    PRIMARY KEY (id)
);

CREATE TABLE Sites(
    name VARCHAR(32) NOT NULL UNIQUE,
    address VARCHAR(256) NOT NULL,
    PRIMARY KEY (name)
);

CREATE TABLE Stock(
    id INT NOT NULL AUTO_INCREMENT,
    product_id VARCHAR(32) NOT NULL,
    site_id VARCHAR(32) NOT NULL,
    stock_healthy BOOLEAN DEFAULT True,
        -- NULL = ordered
        -- false = low
        -- true = healthy
    order_date DATE DEFAULT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (product_id) REFERENCES Products(id) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (site_id) REFERENCES Sites(name) ON UPDATE CASCADE ON DELETE CASCADE
);
