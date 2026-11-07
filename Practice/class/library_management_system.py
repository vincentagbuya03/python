class Book:
    def __init__(self, book_id, title, author, genre):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.genre = genre
        self.is_available = True


class User:
    def __init__(self, user_id, name, age, contact):
        self.user_id = user_id
        self.name = name
        self.age = age
        self.contact = contact

    def view_books(self, books):
        print("\n--- Library Books ---")
        for book in books:
            status = "Available" if book.is_available else "Borrowed"
            print(f"ID: {book.book_id} | Title: {book.title} | Author: {book.author} | Genre: {book.genre} | Status: {status}")


class Visitor(User):
    def __init__(self, user_id, name, age, contact, pass_id):
        super().__init__(user_id, name, age, contact)
        self.pass_id = pass_id

    def display_info(self):
        print(f"Visitor ID: {self.user_id} | Name: {self.name} | Age: {self.age} | Contact: {self.contact} | Pass ID: {self.pass_id}")

    def borrow_book(self, book):
        print(f"{self.name} is only a visitor with Pass ID {self.pass_id}. Visitors cannot borrow books!")



class Borrower(User):
    def __init__(self, user_id, name, age, contact):
        super().__init__(user_id, name, age, contact)
        self.max_books = 5
        self.borrowed_books = []

    def display_info(self):
        print(f"Member ID: {self.user_id} | Name: {self.name} | Age: {self.age} | Contact: {self.contact} | Borrowed: {len(self.borrowed_books)}/{self.max_books}")

    def borrow_book(self, book):
        if len(self.borrowed_books) >= self.max_books:
            print(f"Sorry {self.name}, you reached the maximum limit of {self.max_books} books!")
        elif not book.is_available:
            print(f"Sorry, '{book.title}' is already borrowed.")
        else:
            book.is_available = False
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed '{book.title}' successfully ({len(self.borrowed_books)}/{self.max_books} books borrowed).")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.is_available = True
            self.borrowed_books.remove(book)
            print(f"{self.name} returned '{book.title}' successfully.")
        else:
            print(f"{self.name} does not have this book.")

    def view_borrowed_books(self):
        if not self.borrowed_books:
            print(f"{self.name} has no borrowed books.")
        else:
            print(f"\n{self.name}'s Borrowed Books ({len(self.borrowed_books)}/{self.max_books}):")
            for book in self.borrowed_books:
                print(f"- [{book.book_id}] {book.title} ({book.genre}) by {book.author}")


class Librarian(User):
    def __init__(self, user_id, name, age, contact, employee_id):
        super().__init__(user_id, name, age, contact)
        self.employee_id = employee_id

    def display_info(self):
        print(f"Staff User ID: {self.user_id} | Name: {self.name} | Age: {self.age} | Contact: {self.contact} | Employee ID: {self.employee_id}")

    def add_book(self, books, book):
        books.append(book)
        print(f"Librarian {self.name} added '{book.title}' to the library.")

    def remove_book(self, books, book_id):
        for book in books:
            if book.book_id == book_id:
                books.remove(book)
                print(f"Librarian {self.name} removed '{book.title}' from the library.")
                return
        print("Book not found.")


books = [
    Book("101", "Python Basics", "John Smith", "Programming"),
    Book("102", "Learn Coding", "Jane Doe", "Education"),
    Book("103", "Data Science", "Alan Turing", "Technology"),
    Book("104", "Clean Code", "Robert Martin", "Programming"),
    Book("105", "Atomic Habits", "James Clear", "Self-Help"),
    Book("106", "The Hobbit", "J.R.R. Tolkien", "Fantasy")
]

visitor = Visitor("U01", "Charlie", 20, "09123456789", "PASS-99")
borrower = Borrower("U02", "Vincent", 21, "09987654321")
librarian = Librarian("U03", "Alice", 30, "09112223344", "EMP-501")


def find_book(book_id):
    for book in books:
        if book.book_id == book_id:
            return book
    return None


if __name__ == "__main__":
    while True:
        print("\n--- Library System ---")
        print("1. View all books (Anyone)")
        print("2. View user profiles")
        print("3. Visitor: Try to borrow a book")
        print("4. Borrower: Borrow a book (Max 5)")
        print("5. Borrower: Return a book")
        print("6. Borrower: View borrowed books")
        print("7. Librarian: Add a book")
        print("8. Librarian: Remove a book")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            borrower.view_books(books)

        elif choice == "2":
            print("\n--- User Profiles ---")
            visitor.display_info()
            borrower.display_info()
            librarian.display_info()

        elif choice == "3":
            book_id = input("Enter book ID to borrow: ")
            book = find_book(book_id)
            if book:
                visitor.borrow_book(book)
            else:
                print("Book not found.")

        elif choice == "4":
            book_id = input("Enter book ID to borrow: ")
            book = find_book(book_id)
            if book:
                borrower.borrow_book(book)
            else:
                print("Book not found.")

        elif choice == "5":
            book_id = input("Enter book ID to return: ")
            book = find_book(book_id)
            if book:
                borrower.return_book(book)
            else:
                print("Book not found.")

        elif choice == "6":
            borrower.view_borrowed_books()

        elif choice == "7":
            new_id = input("Enter book ID: ")
            new_title = input("Enter book title: ")
            new_author = input("Enter book author: ")
            new_genre = input("Enter book genre: ")
            new_book = Book(new_id, new_title, new_author, new_genre)
            librarian.add_book(books, new_book)

        elif choice == "8":
            del_id = input("Enter book ID to remove: ")
            librarian.remove_book(books, del_id)

        elif choice == "9":
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please try again.")
