-- Create database
CREATE DATABASE IF NOT EXISTS db3;

-- Use the database
USE db3;

-- Create students table
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    age INT NOT NULL,
    grade VARCHAR(50) NOT NULL
);

-- Sample data for testing
INSERT INTO students (student_id, name, age, grade) VALUES
(1, 'John Doe', 20, 'A'),
(2, 'Jane Smith', 22, 'B'),
(3, 'Sam Brown', 19, 'C'),
(4, 'Lucy Green', 21, 'B'),
(5, 'Michael White', 23, 'A');
