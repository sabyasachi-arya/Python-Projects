from utilities import database
from utilities.database import add_book, show_book_list, delete_book, mark_book_as_read

USER_CHOICE = """
Self Book Database by Python, By Sabyasachi Bhattacharjee,
-Enter 'a/A' to add a new book
-Enter 'l/L' to  show list of all books
-Enter 'r/R' to mark a book as read
-Enter 'd/D' to delete a book
-Enter 'q/Q' to quit

Your choice: """


def menu():
    database.create_book_table()
    user_input = input(USER_CHOICE).lower()
    while user_input != 'q':
        if user_input == 'a':
            _id_ = int(input("Enter an identification(ID) number of your book(Please input numbers): "))
            name = input("Enter your book's name : ").upper()
            author = input(f"Enter the author's name of the book '{name}': ").title()
            add_book(_id_, name, author)

        elif user_input == 'l':
            books = database.show_book_list()
            for book in books:
                read = 'Yes' if book['read'] is True else 'No'
                print(f"ID No.: {book['ID']}, Book: {book['name']} by {book['author']}, read: {read}")

        elif user_input == 'd':
            _id_ = int(input("Enter the book ID you want to delete : "))
            delete_book(_id_)
            print(f"The book ID: {_id_} has been deleted.")

        elif user_input == 'r':
            _id_ = int(input("Write the ID number of the book you want to mark as read: "))
            mark_book_as_read(_id_)

        else:
            print("Thank you!")

        user_input = input(USER_CHOICE)


menu()
