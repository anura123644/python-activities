-- Total salary of all employees
SELECT SUM(salary) AS total_salary
FROM employees;

-- Count the number of employees
SELECT COUNT(*) AS total_employees
FROM employees;

-- Average salary of employees
SELECT AVG(salary) AS average_salary
FROM employees;

-- Lowest salary among employees
SELECT MIN(salary) AS lowest_salary
FROM employees;

-- Highest salary among employees
SELECT MAX(salary) AS highest_salary
FROM employees;

