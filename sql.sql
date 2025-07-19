SELECT *
FROM Customers
WHERE Country IN ('India', 'USA')             -- IN operator
  AND Name LIKE 'A%'                          -- LIKE operator
  AND Age BETWEEN 25 AND 40                   -- BETWEEN operator
  AND Email IS NOT NULL                       -- IS NOT NULL operator
  AND City IS NULL                            -- IS NULL operator
  AND (Gender = 'Female' OR Gender = 'Male'); -- AND/OR operators

