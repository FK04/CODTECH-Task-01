use library_db;
CREATE TABLE IF NOT EXISTS temp_books (
    bid INT,
    title VARCHAR(255),
    author VARCHAR(255),
    category VARCHAR(100),
    status VARCHAR(50)
);

SET GLOBAL wait_timeout = 600;
SET GLOBAL interactive_timeout = 600;
OPTIMIZE TABLE books_data;


select * from books_data;

ALTER TABLE books_data ADD COLUMN due_date DATE;

ALTER TABLE books_data MODIFY COLUMN bid INT AUTO_INCREMENT PRIMARY KEY;

