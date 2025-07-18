# Run this to access and modify database application

from utilities.database import books, add_book, show_book_list, delete_book, mark_book_as_read

USER_CHOICE = """
-'a' to add a new book
-'l' to  show list of all books
-'r' to mark a book as read
-'d' to delete a book
-'q' to quit

Your choice: """


def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            name = input("Enter your book's name : ")
            author = input(f"Enter the author's name of the book '{name}': ")
            add_book(name, author)

        elif user_input == 'l':
            show_book_list()

        elif user_input == 'd':
            name = input("Enter the book name you want to delete"
                         "(write exactly as given in the list) : ")
            delete_book(name)
            print(f"The {name} book has been deleted.")

        elif user_input == 'r':
            name = input("Write the name of the book you want "
                         "to mark as read(name should be exact as in the list: ")
            mark_book_as_read(name)

            user_input = input(USER_CHOICE)
        else:
            print("Thank you")

        user_input = input(USER_CHOICE)


menu()















