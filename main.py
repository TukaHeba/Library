from Classes.LibraryManager import LibraryManager

manager = LibraryManager("books.db")
print("    >>>>> Welcome to the Library' System <<<<<    ")
print("----------------------------------------------------\n")

while True:
    print("1. Add a Book")
    print("2. List Available Books")
    print("3. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        manager.add_book()
    elif choice == "2":
        manager.list_available_books()
    elif choice == "3":
        manager.close()
        print("Exiting the program.")
        break
    else:
        print("Invalid choice, please try again.")