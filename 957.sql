-- Create a table named Students
CREATE TABLE Students (
    ID INTEGER,
    Name TEXT,
    Age INTEGER
);

-- Insert sample records into Students table
INSERT INTO Students (ID, Name, Age) VALUES
(1, 'Asha', 20),
(2, 'Ravi', 22),
(3, 'Meena', 21),
(4, 'Raj', 23);

-- Select all records from Students table
SELECT * FROM Students;

-- Select records where Age is greater than 21
SELECT * FROM Students
WHERE Age > 21;

