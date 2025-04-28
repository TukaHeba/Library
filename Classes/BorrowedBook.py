from datetime import datetime, timedelta

class BorrowedBook:
    def __init__(self, member_id, book_id, borrow_date=None, return_date=None):
        self._member_id = member_id
        self._book_id = book_id
        self._borrow_date = borrow_date or datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self._return_date = return_date

    @property
    def member_id(self):
        return self._member_id

    @property
    def book_id(self):
        return self._book_id

    @property
    def borrow_date(self):
        return self._borrow_date

    @property
    def return_date(self):
        return self._return_date

    @return_date.setter
    def return_date(self, value):
        self._return_date = value

    # Add a new borrowed book entry to the database
    def create(self, db):
        db.cursor.execute('''
        INSERT INTO borrowed_books (member_id, book_id, borrow_date, return_date)
        VALUES (?, ?, ?, ?)
        ''', (self.member_id, self.book_id, self.borrow_date, self.return_date))
        db.connection.commit()

    # Update return date when the book is returned
    def update_return_date(self, db):
        self.return_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Set current time as return date
        db.cursor.execute('''
        UPDATE borrowed_books
        SET return_date = ?
        WHERE member_id = ? AND book_id = ? AND return_date IS NULL
        ''', (self.return_date, self.member_id, self.book_id))
        db.connection.commit()
        print(f"Book returned successfully. Return date: {self.return_date}")

    # get the names of books that have not been returned yet
    @staticmethod
    def get_unreturned_books(db):
        db.cursor.execute('''
        SELECT books.title
        FROM borrowed_books AS borrowed
        JOIN books ON borrowed.book_id = books.id
        WHERE borrowed.return_date IS NULL
        ''')
        unreturned_books = db.cursor.fetchall()
        print("\nBooks that have not been returned yet:")
        for book in unreturned_books:
            print(f"'{book[0]}'")

  # get the names of members who borrowed books in the last 30 days
    @staticmethod
    def get_members_borrowed_last_30_days(db):
        thirty_days_ago = (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d")
        db.cursor.execute('''
        SELECT DISTINCT members.name
        FROM borrowed_books AS borrowed
        JOIN members ON borrowed.member_id = members.id
        WHERE borrowed.borrow_date >= ?
        ''', (thirty_days_ago,))
        members = db.cursor.fetchall()
        print("\nMembers who borrowed books in the last 30 days:")
        for member in members:
            print(f"{member[0]}")