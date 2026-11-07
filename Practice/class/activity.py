class Book:
    def __init__(self, book_id, title, author, genre):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.genre = genre


    def display_books(self):
        print("")
        print(f"Book ID : {self.book_id}")
        print(f"Title : {self.title}")
        print(f"Authoer: {self.author}")
        print(f"Genre : {self.genre}")


class User:
    def __init__(self, user_id, name, age, contact):
        self.user_id = user_id
        self.name = name
        self.age = age
        self.contact = contact

    def display_user(self):
        print("")
        print(f"User ID : {self.user_id}")
        print(f"Name : {self.name}")
        print(f"Age: {self.age}")
        print(f"Contact : {self.contact}")

class Patron(User):
    def __init__(self, user_id, name, age, contact):
        super().__init__(user_id, name, age, contact)
        self.max_books = 5
        self.borrowed_books = ["Attack on titan"]

    def display_info(self):
        print(f"Member ID: {self.user_id} | Name: {self.name} | Age: {self.age} | Contact: {self.contact} | Borrowed: {len(self.borrowed_books)}/{self.max_books}")

    

class Librarian(User):
    def __init__(self, user_id, name, age, contact, employee_id):
        super().__init__(user_id, name, age, contact)
        self.employee_id = employee_id

while True:
    print("\n--- Library System ---")
    print("1. Users")
    print("2. Books")
    print("3. Visitor")
    print("4. Borrower")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        user1 = User("23-sc-4114", "Vincent Agbuya", 21 , "09122354762")
        user1.display_user()

    elif choice == "2":
        print("\n--- Books ---")
        book1 = Book("book_0001", "ELECTIVE 4", "Napoleon Hermoso", "Programming")
        book1.display_books()

    elif choice == "3":
        print("\n--- Borrower ---")
        borrower1 = Patron("Borrower-0001", "Chelsea" , 21 , "09122354762")
        borrower1.display_info()

    elif choice == "4":
        print("Exiting program...")
        break
    else:
        print("Error program...")
        