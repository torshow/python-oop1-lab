#!/usr/bin/env python3


# Book represents a book carried by the bookstore.

class Book:
    def __init__(self, title, page_count):

        self.title = title
        self.page_count = page_count

# Return the current page count.
    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, page_count):
        if not isinstance(page_count, int):
            print("page_count must be an integer")
        else:
            self._page_count = page_count

# Simulate turning a page in the book.

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")