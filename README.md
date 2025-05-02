# Library System

A simple command-line based Library System that allows users to manage books, members, borrow and return books. Also display various reports on the current state of the library.

## Features

- Add books to the library
- Add members to the library
- Borrow books (members can borrow available books)
- Return books (members can return borrowed books)
- Display all available books in the library
- Display all borrowed books and their return status
- Display all members who borrowed books in the last 30 days
- Display all Unreturned Books

## Requirements

- Python 3.x
- SQLite

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/TukaHeba/Library.git
2. Navigate to the project directory:
   ```bash
   cd Library
3. Run the main.py file:
   ```bash
   python3 main.py
4. Follow the on-screen instructions.

## File Structure

```bash
project/
│
├── classes/            # Directory containing all class files
│   ├── Book.py         # Class for managing book operations 
│   ├── Database.py     # Class for managing database operations 
│   ├── Member.py       # Class for managing member operations 
│   ├── BorrowedBook.py # Class for managing borrowed book records
│   └── LibraryManager.py # Main class for handling library logic and database interactions
├── main.py             # Main entry point of the program. Runs the system logic
├── script.sql          # SQL script to set up the database and add dummy data
└── README.md           # Project documentation