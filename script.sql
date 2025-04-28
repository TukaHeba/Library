PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(200) NOT NULL UNIQUE,  
    author VARCHAR(100) NOT NULL,
    published_year INTEGER NOT NULL,
    available_copies INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS members (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE,
    join_date DATE DEFAULT CURRENT_DATE
);

CREATE TABLE IF NOT EXISTS borrowed_books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    member_id INTEGER NOT NULL,
    book_id INTEGER NOT NULL,
    borrow_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    return_date TIMESTAMP,
    FOREIGN KEY (member_id) REFERENCES members(id),
    FOREIGN KEY (book_id) REFERENCES books(id)
);

INSERT INTO books (title, author, published_year, available_copies) VALUES
('Pride and Prejudice', 'Jane Austen', 1813, 4),
('The Hobbit', 'J.R.R. Tolkien', 1937, 3),
('The Catcher in the Rye', 'J.D. Salinger', 1951, 2),
('The Alchemist', 'Paulo Coelho', 1988, 5),
('Moby-Dick', 'Herman Melville', 1851, 1),
('War and Peace', 'Leo Tolstoy', 1869, 2);

INSERT INTO members (name, email, join_date) VALUES
('Alice Wonderland', 'alice@example.com', '2025-03-15'),
('Bob Builder', 'bob@example.com', '2025-02-10'),
('Charlie Chaplin', 'charlie@example.com', '2025-01-05'),
('Diana Prince', 'diana@example.com', '2025-04-01'),
('Edward Scissorhands', 'edward@example.com', '2025-04-20');

INSERT INTO borrowed_books (member_id, book_id, borrow_date, return_date) VALUES
(1, 2, '2025-04-10', '2025-04-20'),  
(2, 3, '2025-04-15', NULL),          
(3, 1, '2025-03-30', '2025-04-05'),  
(4, 4, '2025-04-25', NULL),          
(5, 5, '2025-04-26', NULL);          