from datetime import datetime, timedelta
from Classes.Database import Database
from Classes.Book import Book
from Classes.Member import Member
from Classes.BorrowedBook import BorrowedBook

class LibraryManager:
    def __init__(self, db_name):
        self.db = Database(db_name)
        self.db.initialize_database()  
        self.db.connect()

    # Display available books for borrowing in the database
    def list_available_books(self):
        books = Book.get_available_books(self.db)
        print("\n------ Available Books ------")
        for book in books:
            print(f"Title: {book.title} | Author: {book.author} | Published at: {book.year} | Available copies: {book.copies}")

    # Add a new book to the database
    def add_book(self):
        title = input("Enter the book title: ")
        author = input("Enter the book author: ")
        publish_year = int(input("Enter the book's publish year: "))
        available_copies = int(input("Enter the number of available copies: "))

        book = Book(title, author, publish_year, available_copies)
        book.create(self.db)
        print("The book has been added successfully!")

    # Close the connection to the database
    def close(self):
        self.db.close()

    # Add a new member to the database
    def add_member(self):
        name = input("Enter the member's name: ")
        email = input("Enter the member's email: ")

        member = Member(name, email)
        member.create(self.db)
        print(f"The member '{member.name}' has been added successfully!")
 
    # Borrow a book if both the member exists and the book is available
    def borrow_a_book(self):
        member_id = int(input("Enter Member ID: "))
        book_id = int(input("Enter Book ID: "))

        if not Member.exists(self.db, member_id):
            print("Member not found.")
            return

        if not Book.is_available(self.db, book_id):
            print("Book not available.")
            return

        Book.borrow(self.db, book_id)

        borrowed = BorrowedBook(member_id, book_id)
        borrowed.create(self.db)
        print("Book borrowed successfully.")

    # Return a book operation
    def return_a_book(self):
        member_id = int(input("Enter Member ID: "))
        book_id = int(input("Enter Book ID: "))
        BorrowedBook.mark_as_returned(self.db, member_id, book_id)
        Book.return_book(self.db, book_id)
        print("Book returned successfully.")

    # Display all books that have not been returned yet
    def list_unreturned_books(self):
        results = BorrowedBook.get_unreturned_books(self.db)
        print("\n --- Unreturned Books ---")
        for title in results:
            print(f"'{title[0]}' is still not returned")

    # Display members who borrowed books within the last 30 days
    def list_members_borrowed_books_last30days(self):
        members = BorrowedBook.get_members_borrowed_last_30_days(self.db)        
        print("\n --- Members who borrowed books in the last 30 days ---")
        for name in members:
            print(f"{name[0]}")

    # Display all borrowed books with return status
    def list_borrowed_books(self):
        records = BorrowedBook.get_all_borrowed_books(self.db)
        print("\n --- All Borrowed Books ---")
        for title, member, borrow_date, return_date in records:
            status = return_date if return_date else "Not Returned"
            print(f"'{title}' borrowed by {member} on {borrow_date} - {status}")