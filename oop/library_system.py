# library_system.py

# Base class for Book
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"'{self.title}' by {self.author}"

# Derived class for EBook
class EBook(Book):
    def __init__(self, title, author, file_size):
        # Call the base class constructor
        super().__init__(title, author)
        # Additional attribute specific to EBook
        self.file_size = file_size

    def __str__(self):
        return f"{super().__str__()} (EBook - {self.file_size}MB)"

# Derived class for PrintBook
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        # Call the base class constructor
        super().__init__(title, author)
        # Additional attribute specific to PrintBook
        self.page_count = page_count

    def __str__(self):
        return f"{super().__str__()} (PrintBook - {self.page_count} pages)"

# Library class to demonstrate composition
class Library:
    def __init__(self):
        self.books = []  # This will hold instances of Book, EBook, and PrintBook

    def add_book(self, book):
        # Add a book (Book, EBook, or PrintBook) to the library
        self.books.append(book)

    def list_books(self):
        # Print details of all the books in the library
        if not self.books:
            print("No books in the library.")
        else:
            print("Books in the library:")
            for book in self.books:
                print(book)



