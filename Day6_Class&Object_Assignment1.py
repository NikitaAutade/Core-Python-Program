class Library:
    # Class attributes
    total_books = 0
    all_books = []
    
    def __init__(self, name):
        # Instance attributes
        self.name = name
        self.borrowed_books = []
    
    def borrow_book(self, book):
        """Method to borrow a book from the library."""
        if book in Library.all_books:
            self.borrowed_books.append(book)
            Library.all_books.remove(book)
            Library.total_books -= 1
            print(f"{self.name} borrowed '{book}'.")
        else:
            print("Book not available.")
    
    def return_book(self, book):
        """Method to return a book to the library."""
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            Library.all_books.append(book)
            Library.total_books += 1
            print(f"{self.name} returned '{book}'.")
        else:
            print("This book was not borrowed by you.")
    
    @classmethod
    def view_library_books(cls):
        """Class method to view available books in the library."""
        print(f"Total books in library: {cls.total_books}")
        print("Available books:", cls.all_books)

# Example usage
Library.all_books = ["Python ", "Java", "C++", "AI"]
Library.total_books = len(Library.all_books)

# Creating a library member
member1 = Library("Alice")
member1.borrow_book("Python ")
Library.view_library_books()
member1.return_book("Python")
Library.view_library_books()
