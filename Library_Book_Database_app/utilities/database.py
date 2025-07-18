books = []


def add_book(name, author):

    books.append({'name': name, 'author': author, 'read': False})


def show_book_list():
    for book in books:
        print_book_list(book)


def print_book_list(book):
    print(f"Name of the Book: {book['name']}")
    print(f"Written by: {book['author']}")
    print(f"Read: {book['read']}")


def delete_book(name):
    for book in books:
        if book["name"] == name:
            books.remove(book)
        elif book["name"] != name:
            print(f"Could not find the specific book called:{name}")


def mark_book_as_read(name):
    for book in books:
        if book["name"] == name:
            book["read"] = True



