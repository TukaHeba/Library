from Classes.Book import Book
from Classes.Database import Database
from Classes.Member import Member
from Classes.BorrowedBook import BorrowedBook

class LibraryManager:
    def __init__(self, db_name):
        self.db = Database(db_name)
        self.db.initialize_database()  
        self.db.connect()

    # Display available books for borroing in the database
    def list_available_books(self):
        self.db.cursor.execute('SELECT * FROM books WHERE available_copies > 0')
        books = self.db.cursor.fetchall()
        print("\nAvailable Books:")
        for book in books:
            print(f"{book[0]}. {book[1]} by {book[2]}, Published: {book[3]}, Available copies: {book[4]}")

    # Add a new book to the database
    def add_book(self):
        title = input("Enter the book title: ")
        author = input("Enter the book author: ")
        publish_year = int(input("Enter the book's publish year: "))
        available_copies = int(input("Enter the number of available copies: "))

        book = Book(title, author, publish_year, available_copies)
        book.create(self.db)
        print("The book has been added successfully!")

    def close(self):
        self.db.close()

    # Add a new member to the database
    def add_member(self):
        name = input("Enter the member's name: ")
        email = input("Enter the member's email: ")

        member = Member(name, email)
        member.create(self.db)
        print(f"The member '{member.name}' has been added successfully!")

    # Borrow a book from the library
    def borrow_book(self, member: Member, book: Book):
        if book.is_available():
            member.borrow_book(book)
            borrowed_book = BorrowedBook(member_id=member.id, book_id=book.id)
            borrowed_book.create(self.db)
            print(f"{member.name} borrowed '{book.title}'.")

    # Return a book to the library
    def return_book(self, member: Member, book: Book):
        member.return_book(book)
        borrowed_book = BorrowedBook(member_id=member.id, book_id=book.id)
        borrowed_book.update_return_date(self.db)
        print(f"{member.name} returned '{book.title}'.")

    # List borrowed books that have not been returned
    def list_borrowed_books(self):
        BorrowedBook.get_unreturned_books(self.db)

    # List members who borrowed books in the last 30 days
    def list_members_borrowed_books_last30days(self):
        BorrowedBook.get_members_borrowed_last_30_days(self.db)






