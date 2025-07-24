from code_behind_ import books


def print_best_books():
    best_books = sorted(books, key=lambda x: x.rating * -1)[:10]   # multiply by -1 to make descending order & [:10] to print top 10 or just till 10
    for book in best_books:
        print(book)


def print_cheapest_books():
    cheapest_books = sorted(books, key=lambda x: x.price)[:10]   # multiply by -1 to make descending order & [:10] to print top 10 or just till 10
    for book in cheapest_books:            # shift+f6 to change name of same variables altogether
        print(book)


def print_best_and_cheapest_books():
    best_and_cheapest_books = sorted(books, key=lambda x: (x.rating * -1, x.price))[:10]  # sort by multiple things like ratings and price together , bcoz rating is written first so first sorting will be done by ratings and then will be sorted by price
    for book in best_and_cheapest_books:      # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ first sorting criteria is rating after then is pricing
        print(book)


print('____________________TOP 10 BOOKS BY RATING__________________________')
print_best_books()
print('____________________TOP 10 CHEAPEST BOOKS__________________________')
print_cheapest_books()
print('____________________TOP 10 BEST & CHEAPEST BOOKS__________________________')
print_best_and_cheapest_books()
