# Iterator class for iterating over a collection of books
class BookIterator:
    def __init__(self, books):
        self.books = books
        self.index = 0

    # Check if there are more books to iterate over
    def has_next(self):
        return self.index < len(self.books)

    # Return the next book
    def next(self):
        book = self.books[self.index]
        self.index += 1
        return book

# Aggregate interface representing a collection of books
class BookCollection:
    def __init__(self):
        self.books = []

    # Method to add a book to the collection
    def add_book(self, book):
        self.books.append(book)

    # Method to create an iterator for the book collection
    def create_iterator(self):
        return BookIterator(self.books)

# Book class representing individual books
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    # Method to display book information
    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}")

# Usage
book_collection = BookCollection()
book_collection.add_book(Book("Harry Potter", "J.K. Rowling"))
book_collection.add_book(Book("The Hobbit", "J.R.R. Tolkien"))
book_collection.add_book(Book("To Kill a Mockingbird", "Harper Lee"))

iterator = book_collection.create_iterator()

while iterator.has_next():
    book = iterator.next()
    book.display_info()
