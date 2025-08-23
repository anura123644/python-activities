-- 1. Select all students
SELECT * FROM students;

-- 2. Get distinct departments
SELECT DISTINCT department FROM students;

-- 3. List students ordered by marks (highest first)
SELECT name, marks FROM students
ORDER BY marks DESC;

-- 4. Count how many students are in each department
SELECT department, COUNT(*) AS student_count
FROM students
GROUP BY department;

-- 5. Find average marks per department
SELECT department, AVG(marks) AS avg_marks
FROM students
GROUP BY department;

-- 6. Find the highest marks in each department
SELECT department, MAX(marks) AS highest_marks
FROM students
GROUP BY department;

-- 7. Find the total marks scored by each department
SELECT department, SUM(marks) AS total_marks
FROM students
GROUP BY department;

-- 8. Combine GROUP BY with ORDER BY to rank departments by average marks
SELECT department, AVG(marks) AS avg_marks
FROM students
GROUP BY department
ORDER BY avg_marks DESC;

-- 9. Count how many students scored above 80
SELECT COUNT(*) AS high_scorers
FROM students
WHERE marks > 80;

-- 10. Find departments with more than 5 students
SELECT department, COUNT(*) AS student_count
FROM students
GROUP BY department
HAVING COUNT(*) > 5;

