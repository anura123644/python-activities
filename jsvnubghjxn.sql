SELECT department, COUNT(*) AS num_employees, AVG(salary) AS avg_salary
FROM employees
WHERE salary > 30000
GROUP BY department
HAVING AVG(salary) > 40000
ORDER BY avg_salary DESC;

