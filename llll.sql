-- 1. Find all books with titles that start with 'The'
SELECT *
FROM Books
WHERE Title LIKE 'The%';

-- 2. List all distinct genres available in the bookstore
SELECT DISTINCT Genre
FROM Books;

-- 3. Find books by authors whose names contain 'Smith'
SELECT *
FROM Books
WHERE Author LIKE '%Smith%';

-- 4. Get all books published after 2015, sorted by price (lowest to highest)
SELECT *
FROM Books
WHERE PublishedYear > 2015
ORDER BY Price ASC;

-- 5. Find all books in the 'Science Fiction' genre that cost more than 500
SELECT *
FROM Books
WHERE Genre = 'Science Fiction' AND Price > 500;

-- 6. List distinct authors who have written books in the 'Fantasy' genre
SELECT DISTINCT Author
FROM Books
WHERE Genre = 'Fantasy';

-- 7. Get books with titles ending in 'Adventure', sorted by published year (newest first)
SELECT *
FROM Books
WHERE Title LIKE '%Adventure'
ORDER BY PublishedYear DESC;

-- 8. Find all books priced between 300 and 700, sorted alphabetically by title
SELECT *
FROM Books
WHERE Price BETWEEN 300 AND 700
ORDER BY Title ASC;

