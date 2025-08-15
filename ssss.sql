

CREATE TABLE Authors (
    AuthorID INT PRIMARY KEY,
    Name VARCHAR(100),
    Country VARCHAR(50)
);

CREATE TABLE Books (
    BookID INT PRIMARY KEY,
    Title VARCHAR(200),
    Genre VARCHAR(50),
    Price DECIMAL(5,2),
    Stock INT,
    AuthorID INT,
    FOREIGN KEY (AuthorID) REFERENCES Authors(AuthorID)
);

CREATE TABLE Sales (
    SaleID INT PRIMARY KEY,
    BookID INT,
    Quantity INT,
    SaleDate DATE,
    FOREIGN KEY (BookID) REFERENCES Books(BookID)
);


INSERT INTO Authors VALUES
(1, 'Harper Lee', 'USA'),
(2, 'Paulo Coelho', 'Brazil'),
(3, 'Arundhati Roy', 'India');

INSERT INTO Books VALUES
(1, 'To Kill a Mockingbird', 'Fiction', 12.99, 5, 1),
(2, 'The Alchemist', 'Fiction', 10.50, 12, 2),
(3, 'The God of Small Things', 'Fiction', 15.00, 3, 3),
(4, 'Brida', 'Romance', 9.75, 8, 2);

INSERT INTO Sales VALUES
(1, 1, 2, '2025-08-01'),
(2, 2, 5, '2025-08-01'),
(3, 3, 1, '2025-08-02'),
(4, 1, 1, '2025-08-03');



-- 1. List all books sorted by price (high to low)
SELECT Title, Price
FROM Books
ORDER BY Price DESC;

-- 2. Find all Fiction books in stock
SELECT Title, Stock
FROM Books
WHERE Genre = 'Fiction' AND Stock > 0;

-- 3. Total revenue per book
SELECT b.Title, SUM(s.Quantity * b.Price) AS Revenue
FROM Sales s
JOIN Books b ON s.BookID = b.BookID
GROUP BY b.Title;

-- 4. Authors with more than 1 book
SELECT a.Name, COUNT(b.BookID) AS BookCount
FROM Authors a
JOIN Books b ON a.AuthorID = b.AuthorID
GROUP BY a.Name
HAVING COUNT(b.BookID) > 1;

-- 5. Books with low stock (less than 5)
SELECT Title, Stock
FROM Books
WHERE Stock < 5;

-- 6. Sales made after August 1, 2025
SELECT *
FROM Sales
WHERE SaleDate > '2025-08-01';

