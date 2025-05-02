class Book:
    def __init__(self, title, author, year, copies):
        self._title = title
        self._author = author
        self._year = year
        self._copies = copies

    # Getter for title
    @property
    def title(self):
        return self._title

    # Getter for author
    @property
    def author(self):
        return self._author

    # Getter for publication year
    @property
    def year(self):
        return self._year

    # Getter for available copies
    @property
    def copies(self):
        return self._copies

    # Setter for available copies with basic validation
    @copies.setter
    def copies(self, value):
        if value < 0:
            print("Copies cannot be negative!")
        else:
            self._copies = value
            
    # Add new book to the database
    def create(self, db):
        db.cursor.execute('''
        INSERT INTO books (title, author, published_year, available_copies)
        VALUES (?, ?, ?, ?)''', (self.title, self.author, self.year, self.copies))
        db.connection.commit()

    # Check if a specific book ID has any available copies
    @staticmethod
    def is_available(db, book_id):
        db.cursor.execute("SELECT available_copies FROM books WHERE id = ?", (book_id,))
        result = db.cursor.fetchone()
        return result and result[0] > 0

    # Retrieve all available books from the database and return them as Book objects
    @classmethod
    def get_available_books(cls, db):
        db.cursor.execute('SELECT title, author, published_year, available_copies FROM books WHERE available_copies > 0')
        results = db.cursor.fetchall()
        return [cls(title, author, year, copies) for title, author, year, copies in results]

    # Decrease available copies by 1 for a specific book ID (when borrowed)
    @staticmethod
    def borrow(db, book_id):
        db.cursor.execute('UPDATE books SET available_copies = available_copies - 1 WHERE id = ?', (book_id,))
        db.connection.commit()

    # Increase available copies by 1 for a specific book ID (when returned)
    @staticmethod
    def return_book(db, book_id):
        db.cursor.execute('UPDATE books SET available_copies = available_copies + 1 WHERE id = ?', (book_id,))
        db.connection.commit()