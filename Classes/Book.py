class Book:
    def __init__(self, title, author, year, copies):
        self._title = title
        self._author = author
        self._year = year
        self._copies = copies

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def year(self):
        return self._year

    @property
    def copies(self):
        return self._copies

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

    def is_available(self):
        return self.copies > 0

    def borrow(self):
        if self.is_available():
            self.copies -= 1
            print(f"You borrowed '{self.title}'.")
        else:
            print(f"Sorry, '{self.title}' is not available.")

    def return_book(self):
        self.copies += 1
        print(f"You returned '{self.title}'.")