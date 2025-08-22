--  Create the Employees table
CREATE TABLE Employees (
    EmpID INT,
    Name VARCHAR(50),
    Department VARCHAR(50),
    Salary INT
);

--  Insert sample data
INSERT INTO Employees (EmpID, Name, Department, Salary) VALUES
(101, 'Alice', 'HR', 50000),
(102, 'Bob', 'IT', 60000),
(103, 'Charlie', 'Finance', 55000),
(104, 'Diana', 'IT', 70000),
(105, 'Ethan', 'HR', 48000);

--  1. Select all records
SELECT * FROM Employees;

--  2. Select names and salaries
SELECT Name, Salary FROM Employees;

--  3. Find employees in the IT department
SELECT * FROM Employees
WHERE Department = 'IT';

--  4. Find employees with salary greater than 55000
SELECT * FROM Employees
WHERE Salary > 55000;

--  5. Find the highest salary
SELECT MAX(Salary) AS HighestSalary FROM Employees;

--  6. Find the lowest salary
SELECT MIN(Salary) AS LowestSalary FROM Employees;

--  7. Find the name of the employee with the highest salary
SELECT Name FROM Employees
WHERE Salary = (SELECT MAX(Salary) FROM Employees);

