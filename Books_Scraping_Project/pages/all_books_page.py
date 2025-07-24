from bs4 import BeautifulSoup

from locators.all_book_page import AllBooksPageLocators    # your imports from your local files come after import of other things(projects that aren't created by you such as BeautifulSoup
from parsers.book_parsers import BookParser


class AllBooksPage:
    def __init__(self, page_content):
        self.soup = BeautifulSoup(page_content, 'html.parser')

    @property
    def books(self):
        return [BookParser(e) for e in self.soup.select(AllBooksPageLocators.BOOKS)]
