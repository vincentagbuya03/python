"""
Book Management System
Demonstrates Object-Oriented Programming (OOP) in Python:
1. Base Class (Parent): Book
2. Child Classes (Subclasses): PhysicalBook, EBook, AudioBook
3. Method Overriding & Polymorphism
4. Management Class: BookManager
"""


# =====================================================================
# 1. PARENT CLASS (Base Class)
# =====================================================================
class Book:
    """
    Base class representing a generic book.
    Contains common attributes and methods shared by all types of books.
    """

    def __init__(self, book_id: str, title: str, author: str):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_available = True

    def borrow(self) -> bool:
        """Marks the book as borrowed if it is available."""
        if self.is_available:
            self.is_available = False
            print(f"Success: '{self.title}' has been borrowed.")
            return True
        else:
            print(f"Unavailable: '{self.title}' is currently checked out.")
            return False

    def return_book(self) -> bool:
        """Returns the book back to the library."""
        if not self.is_available:
            self.is_available = True
            print(f"Success: '{self.title}' has been returned and is now available.")
            return True
        else:
            print(f"Notice: '{self.title}' was already available.")
            return False

    def display_info(self) -> str:
        """Returns a string describing the book's details."""
        status = "Available" if self.is_available else "Borrowed"
        return f"[{self.__class__.__name__}] ID: {self.book_id} | Title: '{self.title}' | Author: {self.author} | Status: {status}"


# =====================================================================
# 2. CHILD CLASSES (Subclasses / Inheritance)
# =====================================================================

class PhysicalBook(Book):
    """
    CHILD CLASS 1: PhysicalBook (Inherits from Book)
    -------------------------------------------------------------------
    WHAT IT DOES:
    - Represents physical printed books kept on actual library shelves.
    - Adds physical attributes:
        * shelf_location: Where the book is physically located (e.g., 'Aisle 3, Shelf B').
        * weight_grams: Weight of the book in grams.
    - Overrides display_info() to show shelf and weight information.
    - Adds unique method: locate_shelf() to help readers locate the physical copy.
    """

    def __init__(self, book_id: str, title: str, author: str, shelf_location: str, weight_grams: float):
        # Call parent constructor to set up book_id, title, and author
        super().__init__(book_id, title, author)
        self.shelf_location = shelf_location
        self.weight_grams = weight_grams

    # Method Overriding: Extend parent display_info with physical book details
    def display_info(self) -> str:
        base_info = super().display_info()
        return f"{base_info} | Shelf: {self.shelf_location} | Weight: {self.weight_grams}g"

    # Child-specific method
    def locate_shelf(self):
        """Specific behavior: Tells the borrower where to find the physical book."""
        print(f"📍 Physical Book '{self.title}' is located at: {self.shelf_location}")


class EBook(Book):
    """
    CHILD CLASS 2: EBook (Inherits from Book)
    -------------------------------------------------------------------
    WHAT IT DOES:
    - Represents a digital book file (PDF, EPUB, MOBI).
    - Adds digital attributes:
        * file_format: Format of the ebook (e.g., 'PDF', 'EPUB').
        * file_size_mb: Size of the digital file in megabytes.
    - Overrides display_info() to show file format and file size.
    - Adds unique method: download() allowing users to download the digital file.
    """

    def __init__(self, book_id: str, title: str, author: str, file_format: str, file_size_mb: float):
        # Call parent constructor
        super().__init__(book_id, title, author)
        self.file_format = file_format
        self.file_size_mb = file_size_mb

    # Method Overriding: Extend parent display_info with ebook details
    def display_info(self) -> str:
        base_info = super().display_info()
        return f"{base_info} | Format: {self.file_format.upper()} | Size: {self.file_size_mb}MB"

    # Child-specific method
    def download(self):
        """Specific behavior: Simulates downloading the digital ebook."""
        print(f"📥 Downloading '{self.title}.{self.file_format.lower()}' ({self.file_size_mb} MB)... Download complete!")


class AudioBook(Book):
    """
    CHILD CLASS 3: AudioBook (Inherits from Book)
    -------------------------------------------------------------------
    WHAT IT DOES:
    - Represents an audio recording of a book.
    - Adds audio attributes:
        * narrator: The person who narrated the book.
        * duration_minutes: Total length of the audio recording in minutes.
    - Overrides display_info() to show narrator and duration.
    - Adds unique method: play_sample() allowing users to listen to an audio preview.
    """

    def __init__(self, book_id: str, title: str, author: str, narrator: str, duration_minutes: int):
        # Call parent constructor
        super().__init__(book_id, title, author)
        self.narrator = narrator
        self.duration_minutes = duration_minutes

    # Method Overriding: Extend parent display_info with audiobook details
    def display_info(self) -> str:
        base_info = super().display_info()
        return f"{base_info} | Narrator: {self.narrator} | Duration: {self.duration_minutes} mins"

    # Child-specific method
    def play_sample(self):
        """Specific behavior: Simulates playing an audio sample."""
        print(f"🎧 Playing 30-second preview of '{self.title}', narrated by {self.narrator}...")


# =====================================================================
# 3. MANAGEMENT CLASS
# =====================================================================
class BookManager:
    """
    Manages a collection of books (PhysicalBook, EBook, AudioBook).
    Handles adding, searching, viewing, borrowing, returning, and triggering
    special child actions using Polymorphism.
    """

    def __init__(self):
        # Dictionary mapping book_id -> Book instance
        self.books: dict[str, Book] = {}

    def add_book(self, book: Book) -> bool:
        """Adds a book object (any child of Book) into the system."""
        if book.book_id in self.books:
            print(f"Error: Book ID '{book.book_id}' already exists!")
            return False
        self.books[book.book_id] = book
        print(f"Added successfully: '{book.title}' as a {book.__class__.__name__}.")
        return True

    def view_books(self):
        """
        Displays all books in the catalog.
        Demonstrates Polymorphism: Each child class automatically executes
        its own version of display_info().
        """
        if not self.books:
            print("The library catalog is currently empty.")
            return

        print("\n================== LIBRARY CATALOG ==================")
        for book in self.books.values():
            print(book.display_info())
        print("=====================================================")

    def search_books(self, query: str):
        """Searches books by ID, Title, or Author."""
        query_lower = query.lower()
        matches = [
            b for b in self.books.values()
            if query_lower in b.book_id.lower()
            or query_lower in b.title.lower()
            or query_lower in b.author.lower()
        ]

        if not matches:
            print(f"No books found matching '{query}'.")
        else:
            print(f"\n--- Found {len(matches)} Match(es) ---")
            for b in matches:
                print(b.display_info())

    def borrow_book(self, book_id: str):
        """Borrows a book given its ID."""
        if book_id in self.books:
            self.books[book_id].borrow()
        else:
            print(f"Book with ID '{book_id}' not found.")

    def return_book(self, book_id: str):
        """Returns a book given its ID."""
        if book_id in self.books:
            self.books[book_id].return_book()
        else:
            print(f"Book with ID '{book_id}' not found.")

    def use_special_feature(self, book_id: str):
        """
        Executes child-specific methods depending on the type of book:
        - PhysicalBook -> locate_shelf()
        - EBook        -> download()
        - AudioBook    -> play_sample()
        """
        if book_id not in self.books:
            print(f"Book with ID '{book_id}' not found.")
            return

        book = self.books[book_id]
        print(f"\nAccessing special feature for '{book.title}':")

        if isinstance(book, PhysicalBook):
            book.locate_shelf()
        elif isinstance(book, EBook):
            book.download()
        elif isinstance(book, AudioBook):
            book.play_sample()
        else:
            print("Generic books do not have specialized features.")


# =====================================================================
# 4. INTERACTIVE MENU & DEMO
# =====================================================================
def load_sample_books(manager: BookManager):
    """Loads sample books of each child type for immediate testing."""
    manager.add_book(PhysicalBook("B001", "Clean Code", "Robert C. Martin", "Aisle 2, Shelf 4", 650.0))
    manager.add_book(EBook("B002", "Automate the Boring Stuff", "Al Sweigart", "pdf", 12.5))
    manager.add_book(AudioBook("B003", "Atomic Habits", "James Clear", "James Clear", 320))


def run_interactive_menu():
    manager = BookManager()
    load_sample_books(manager)

    while True:
        print("\n===== BOOK MANAGEMENT SYSTEM =====")
        print("1.) View All Books")
        print("2.) Add a New Book (Physical / EBook / AudioBook)")
        print("3.) Search Book")
        print("4.) Borrow Book")
        print("5.) Return Book")
        print("6.) Use Book Special Feature (Locate / Download / Sample)")
        print("7.) Exit")

        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            manager.view_books()

        elif choice == "2":
            print("\nSelect Book Type:")
            print("1. Physical Book")
            print("2. E-Book")
            print("3. Audio Book")
            type_choice = input("Enter type (1-3): ").strip()

            book_id = input("Enter Book ID: ").strip()
            title = input("Enter Title: ").strip()
            author = input("Enter Author: ").strip()

            if type_choice == "1":
                shelf = input("Enter Shelf Location (e.g., Aisle 1, Shelf C): ").strip()
                weight = float(input("Enter Weight in grams: ").strip() or "0")
                manager.add_book(PhysicalBook(book_id, title, author, shelf, weight))

            elif type_choice == "2":
                file_format = input("Enter File Format (e.g., PDF, EPUB): ").strip()
                size = float(input("Enter File Size in MB: ").strip() or "0")
                manager.add_book(EBook(book_id, title, author, file_format, size))

            elif type_choice == "3":
                narrator = input("Enter Narrator Name: ").strip()
                duration = int(input("Enter Duration in minutes: ").strip() or "0")
                manager.add_book(AudioBook(book_id, title, author, narrator, duration))

            else:
                print("Invalid book type selected.")

        elif choice == "3":
            query = input("Enter search keyword (ID, title, or author): ").strip()
            manager.search_books(query)

        elif choice == "4":
            book_id = input("Enter Book ID to borrow: ").strip()
            manager.borrow_book(book_id)

        elif choice == "5":
            book_id = input("Enter Book ID to return: ").strip()
            manager.return_book(book_id)

        elif choice == "6":
            book_id = input("Enter Book ID: ").strip()
            manager.use_special_feature(book_id)

        elif choice == "7":
            print("Exiting Book Management System. Goodbye!")
            break

        else:
            print("Invalid option. Please choose between 1 and 7.")


if __name__ == "__main__":
    run_interactive_menu()

