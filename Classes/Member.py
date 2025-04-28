from datetime import datetime
from Classes.Book import Book

class Member:
    def __init__(self, name, email):
        self._name = name
        self._email = email
        self._join_date = datetime.now().strftime("%Y-%m-%d")  

    @property
    def name(self):
        return self._name

    @property
    def email(self):
        return self._email

    @property
    def join_date(self):
        return self._join_date

    def borrow_book(self, book: Book):
        if book.is_available():
            book.borrow()
            print(f"{self.name} borrowed '{book.title}'.")
        else:
            print(f"Sorry, '{book.title}' is not available.")

    def return_book(self, book: Book):
        book.return_book()
        print(f"{self.name} returned '{book.title}'.")

    def create(self, db):
        db.cursor.execute('''
        INSERT INTO members (name, email, join_date)
        VALUES (?, ?, ?)''', (self.name, self.email, self.join_date))
        db.connection.commit()