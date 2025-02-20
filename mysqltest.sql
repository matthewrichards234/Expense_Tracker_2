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
    category_name VARCHAR(50) NOT NULL UNIQUE
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
('Leslie', 'Knope', '1949-09-25', 'leslie.knope@example.com', '123-456-7890', 'password1'),
('Ron', 'Swanson', '1960-05-06', 'ron.swanson@example.com', '987-654-3210', 'password2'),
('April', 'Ludgate', '1989-03-20', 'april.ludgate@example.com', '555-123-4567', 'password3'),
('Andy', 'Dwyer', '1984-09-11', 'andy.dwyer@example.com', '444-567-8901', 'password4'),
('Ben', 'Wyatt', '1975-12-12', 'ben.wyatt@example.com', '222-333-4444', 'password5'),
('Chris', 'Traeger', '1967-10-27', 'chris.traeger@example.com', '333-222-1111', 'password6'),
('Ann', 'Perkins', '1977-06-22', 'ann.perkins@example.com', '777-888-9999', 'password7'),
('Tom', 'Haverford', '1985-04-30', 'tom.haverford@example.com', '666-555-4444', 'password8'),
('Donna', 'Meagle', '1970-02-14', 'donna.meagle@example.com', '999-000-1111', 'password9'),
('Jerry', 'Gergich', '1955-07-15', 'jerry.gergich@example.com', '888-777-6666', 'password10');


INSERT INTO Category (category_name)
VALUES
('Grocery'),
('Pets'),
('Electronics'),
('Clothing'),
('Furniture'),
('Sports'),
('Books'),
('Beauty'),
('Toys'),
('Automotive');


INSERT INTO Transaction (user_id, date_time, category_id, total_amount, payment_method)
VALUES
(1, '2024-07-01 10:30:00', 1, 50.75, 'Credit'),
(2, '2024-07-02 14:15:00', 2, 20.00, 'Debit'),
(3, '2024-07-03 18:45:00', 3, 199.99, 'Cash'),
(4, '2024-07-04 09:00:00', 4, 75.50, 'Other'),
(5, '2024-07-05 16:30:00', 5, 300.00, 'Credit'),
(6, '2024-07-06 12:10:00', 6, 45.25, 'Debit'),
(7, '2024-07-07 20:20:00', 7, 15.99, 'Cash'),
(8, '2024-07-08 08:05:00', 8, 89.49, 'Other'),
(9, '2024-07-09 17:55:00', 9, 120.00, 'Credit'),
(10, '2024-07-10 11:40:00', 10, 60.30, 'Debit');
