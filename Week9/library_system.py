#create book class with title, author, ISBN attributes
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    #Add method to display book info
    def info(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"


#Create library class collection of books
class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    #Implement methods to add, remove, list books
    def add_book(self, book):
        self.books.append(book)
        print(f"Added Book: {book.info()}")

    def remove_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                print(f"Removed Book: {book.info()}")
                return
        print("Book not found with title '{title}'")

    def list_books(self):
        print(f"\nBooks in {self.name}:")
        if not self.books:
            print("No books found.")
        for i, book in enumerate(self.books, 1):
            print(f"{i}. {book.info()}")

    #Add search method to find books by title
    def search_book(self, search_title):
        found = [b for b in self.books if search_title.lower() in b.title.lower()]
        if found:
            print(f"Found {len(found)} book(s) matching '{search_title}'")
            for b in found:
                print(f"- {b.info()}")

        else:
            print(f"No book found with title '{search_title}'")


#Testing Checklist
library = Library("Staatsbibliothek")
book1 = Book("And Then There Were None", "Agatha Christie", "978-0062073488" )
book2 = Book("The Shining", "Stephen King", "978-0307743657")
book3 = Book("Along Came a Spider", "James Patterson", "978-0446364270")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

library.list_books()
library.search_book("And Then There")
library.remove_book("The Shining")
library.list_books()
