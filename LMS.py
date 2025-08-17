
class Book:
    def __init__(self,title,author,isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True
    
    def __str__(self):
        status =  "Available" if self.available else "Borrowed"
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) - {status}"
    
class Borrower:
    def __init__(self,name):
        self.name = name
        self.borrowed_books = []
        
    def borrow(self,book):
        if book.available:
            book.available = False
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed '{book.title}'")
            
        else:
            print(f"sorrym'{book.title}' is already borrowed.")
        
    def return_book(self,book):
        if book in self.borrowed_books:
            book.available = True
            self.borrowed_books.remove(book)
            print(f"{self.name} returned '{book.title}'")
        else:
            print(f"{self.name} does not have '{book.title}'.")
            
class Library:
    def __init__(self):
        self.books = []
        self.borrow_log = []
        
    def add_book(self,book):
        self.books.append(book)
        print(f"Added '{book.title}' to the library.")
        
    def display_books(self):
        print("\n available books in library:")
        for book in self.books:
            print(book)
            
    def borrow_book(self, borrower,isbn):
        for book in self.books:
            if book.isbn == isbn:
                borrower.borrow(book)
                if not book.available:
                    self.borrow_log.append((borrower.name,book.title))
                return
        print("book not found!.")
        
    def return_book(self,borrower,isbn):
        for book in self.books:
            if book.isbn == isbn:
                borrower.return_book(book)
                return 
        print("book not found!")
        
    def show_borrow_log(self):
        print("\n Borrow log:")
        for entry in self.borrow_log:
            print(f"{entry[0]} borrowed '{entry[1]}'")

library = Library()        
# Adding books
book1 = Book("1984", "George Orwell", "001")
book2 = Book("The Hobbit", "J.R.R. Tolkien", "002")
book3 = Book("Python Basics", "John Doe", "003")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
# Borrower
alice = Borrower("Alice")
bob = Borrower("Bob")
# Actions
library.display_books()
library.borrow_book(alice, "001")
library.borrow_book(bob, "001")  # Already borrowed
library.return_book(alice, "001")
library.borrow_book(bob, "001")

library.display_books()
library.show_borrow_log()