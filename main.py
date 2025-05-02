from Classes.LibraryManager import LibraryManager

manager = LibraryManager("books.db")
print("  >>>>> Welcome to the Library' System <<<<<")

while True:
    print("-------------------------------------------------")
    print("1. Add a Book")
    print("2. List Available Books")
    print("3. Add Member")
    print("4. Borrow a Book")
    print("5. Return a Book")
    print("6. List Unreturned Books")
    print("7. List Members Who Borrowed in Last 30 Days")
    print("8. list Borrowed Books ")
    print("9. Exit")
    print("-------------------------------------------------")
    choice = input("Choose an option: ")

    if choice == "1":
        manager.add_book()
    elif choice == "2":
        manager.list_available_books()
    elif choice == "3":
        manager.add_member()
    elif choice == "4":
        manager.borrow_a_book()
    elif choice == "5":
        manager.return_a_book()
    elif choice == "6":
        manager.list_unreturned_books()
    elif choice == "7":
        manager.list_members_borrowed_books_last30days()
    elif choice == "8":
        manager.list_borrowed_books()
    elif choice == "9":
        manager.close()
        print("Exiting the program.")
        break
    else:
        print("Invalid choice, please try again.")