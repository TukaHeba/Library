from datetime import datetime, timedelta

class BorrowedBook:
    def __init__(self, member_id, book_id, borrow_date=None, return_date=None):
        self._member_id = member_id
        self._book_id = book_id
        self._borrow_date = borrow_date or datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self._return_date = return_date

    # Getter for member ID
    @property
    def member_id(self):
        return self._member_id

    # Getter for book ID
    @property
    def book_id(self):
        return self._book_id

    # Getter for borrow date
    @property
    def borrow_date(self):
        return self._borrow_date

    # Getter for return date
    @property
    def return_date(self):
        return self._return_date

    # Setter for return date
    @return_date.setter
    def return_date(self, value):
        self._return_date = value

    # Add a new borrowed book record to the database
    def create(self, db):
        db.cursor.execute('''
        INSERT INTO borrowed_books (member_id, book_id, borrow_date, return_date)
        VALUES (?, ?, ?, ?)
        ''', (self.member_id, self.book_id, self.borrow_date, self.return_date))
        db.connection.commit()
    
    # Update return date when the book is returned
    @staticmethod
    def mark_as_returned(db, member_id, book_id):
        return_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        db.cursor.execute('''
        UPDATE borrowed_books
        SET return_date = ?
        WHERE member_id = ? AND book_id = ? AND return_date IS NULL
        ''', (return_date, member_id, book_id))
        db.connection.commit()

    # Retrieve the titles of all books that have not yet been returned
    @staticmethod
    def get_unreturned_books(db):
        db.cursor.execute('''
        SELECT books.title
        FROM borrowed_books AS borrowed
        JOIN books ON borrowed.book_id = books.id
        WHERE borrowed.return_date IS NULL
        ''')
        return db.cursor.fetchall()

    # Retrieve the names of members who borrowed books in the last 30 days
    @staticmethod
    def get_members_borrowed_last_30_days(db):
        thirty_days_ago = (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d %H:%M:%S")
        db.cursor.execute('''
        SELECT DISTINCT members.name
        FROM borrowed_books AS borrowed
        JOIN members ON borrowed.member_id = members.id
        WHERE borrowed.borrow_date >= ?
        ''', (thirty_days_ago,))
        return db.cursor.fetchall()
    
    # Retrieve all borrowing books 
    @staticmethod
    def get_all_borrowed_books(db):
        db.cursor.execute('''
        SELECT books.title, members.name, borrowed.borrow_date, borrowed.return_date
        FROM borrowed_books AS borrowed
        JOIN books ON borrowed.book_id = books.id
        JOIN members ON borrowed.member_id = members.id
        ''')
        return db.cursor.fetchall()