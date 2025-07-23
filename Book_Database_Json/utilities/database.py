import json

'''
[
    {
        'ID': 1,
        'name': 'Harry Potter',
        'author': 'JK Rowling'
        'read': True
    }
]
'''

books_file = 'books.json'


def create_book_table():
    with open(books_file, 'w') as file:
        json.dump([], file)


def _save_all_books(books):
    with open(books_file, 'w') as file:
        json.dump(books, file)


def show_book_list():
    with open(books_file, 'r') as file:
        return json.load(file)


def add_book(_id_, name, author):
    books = show_book_list()
    books.append({'ID': _id_, 'name': name, 'author': author, 'read': False})
    print(f"Book: {name} is added to the list of books.")
    _save_all_books(books)


def delete_book(_id_):
    books = show_book_list()
    books = [book for book in books if book['ID'] != _id_]
    _save_all_books(books)


def mark_book_as_read(_id_):
    books = show_book_list()
    for book in books:
        if book['ID'] == _id_:
            book['read'] = True
            print(f"You have completed reading the book: {book['name']}")
    _save_all_books(books)


