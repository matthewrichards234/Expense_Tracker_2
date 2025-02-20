CREATE DATABASE `Finance_Tracker_Database`;
USE `Finance_Tracker_Database`;

CREATE TABLE User (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    age INT NOT NULL,
    date_of_birth DATE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone_number VARCHAR(15) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL
);

CREATE TABLE Category (
    category_id INT PRIMARY KEY AUTO_INCREMENT,
    category_name VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE Transaction (
    transaction_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    date_time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    category_id INT NOT NULL,
    total_amount DECIMAL(10, 2) NOT NULL,
    payment_method ENUM('Cash', 'Credit', 'Debit', 'Other') NOT NULL,
    FOREIGN KEY (user_id) REFERENCES User(user_id),
    FOREIGN KEY (category_id) REFERENCES Category(category_id)
);

INSERT INTO User (user_id, first_name, last_name, date_of_birth, email, phone_number, password_hash)
VALUES
(1, 'Leslie', 'Knope', '1949-09-25', 'leslie.knope@example.com', '123-456-7890', 'password1'),
(2, 'Ron', 'Swanson', '1960-05-06', 'ron.swanson@example.com', '987-654-3210', 'password2'),
(3, 'April', 'Ludgate', '1989-03-20', 'april.ludgate@example.com', '555-123-4567', 'password3'),
(4, 'Andy', 'Dwyer', '1984-09-11', 'andy.dwyer@example.com', '444-567-8901', 'password4'),
(5, 'Ben', 'Wyatt', '1975-12-12', 'ben.wyatt@example.com', '222-333-4444', 'password5'),
(6, 'Chris', 'Traeger', '1967-10-27', 'chris.traeger@example.com', '333-222-1111', 'password6'),
(7, 'Ann', 'Perkins', '1977-06-22', 'ann.perkins@example.com', '777-888-9999', 'password7'),
(8, 'Tom', 'Haverford', '1985-04-30', 'tom.haverford@example.com', '666-555-4444', 'password8'),
(9, 'Donna', 'Meagle', '1970-02-14', 'donna.meagle@example.com', '999-000-1111', 'password9'),
(10, 'Jerry', 'Gergich', '1955-07-15', 'jerry.gergich@example.com', '888-777-6666', 'password10');

