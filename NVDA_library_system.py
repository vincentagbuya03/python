
nvda_books = [
    {"id": "B-001", 
     "title": "Introduction to Python", 
     "author": "Sir Naps",
     "category": "Programming", 
     "copies": 5
     },
    {"id": "B-002", 
     "title": "Web Development Basics", 
     "author": "Sir Paul",
     "category": "Web Development", 
     "copies": 3
     },
    {"id": "B-003", 
     "title": "Database Fundamentals", 
     "author": "Sir Cmark",
     "category": "Database", 
     "copies": 0
     },
    {"id": "B-004", 
     "title": "Mobile App Development", 
     "author": "Sir Naps",
     "category": "Mobile Development", 
     "copies": 4
     },
    {"id": "B-005", 
     "title": "Computer Networking", 
     "author": "Sir Tops",
     "category": "Networking", 
     "copies": 2
     },
]

while True:
    print("\n" + "=" * 34)
    print("LIBRARY BOOK MANAGEMENT SYSTEM")
    print("=" * 34 + "\n")
    print("[1] Display All Book Records")
    print("[2] Add New Book")
    print("[3] Update Available Copies")
    print("[4] Search Book")
    print("[5] Display Available Books")
    print("[6] Display Unavailable Books")
    print("[7] Generate Inventory Statistics")
    print("[8] Display Unique Categories")
    print("[9] Display Sorted Copies")
    print("[10] Exit")

    nvda_raw = input("Enter your choice: ").strip()
    try:
        nvda_choice = int(nvda_raw)
    except ValueError:
        print("Invalid choice. Please enter a number from 1 to 10.")
        continue

    if nvda_choice == 1:
        print("\n===== ALL BOOK RECORDS =====")
        nvda_statuses = ["Available" if nvda_b["copies"] > 0 else "Unavailable" for nvda_b in nvda_books]
        print(f"{'ID':<8}{'Title':<26}{'Author':<14}{'Category':<20}{'Copies':<8}Status")
        for nvda_book, nvda_status in zip(nvda_books, nvda_statuses):
            print(f"{nvda_book['id']:<8}{nvda_book['title'].upper():<26}{nvda_book['author']:<14}"
                  f"{nvda_book['category']:<20}{nvda_book['copies']:<8}{nvda_status}")
        nvda_titles = [nvda_b["title"] for nvda_b in nvda_books]
        nvda_upper_titles = [nvda_b["title"].upper() for nvda_b in nvda_books]


    elif nvda_choice == 2:
        print("\n===== ADD NEW BOOK =====")
        nvda_numbers = [int(nvda_b["id"].split("-")[1]) for nvda_b in nvda_books]
        nvda_new_id = f"B-{(max(nvda_numbers) + 1 if nvda_numbers else 1):03d}"
        print(f"Auto-generated Book ID: {nvda_new_id}")
        nvda_title = input("Title: ").strip()
        nvda_author = input("Author: ").strip()
        nvda_category = input("Category: ").strip()
        if not nvda_title or not nvda_author or not nvda_category:
            print("Error: Title, author and category cannot be empty.")
            continue
        nvda_duplicate = [nvda_b for nvda_b in nvda_books if nvda_b["id"] == nvda_new_id]
        if nvda_duplicate:
            print("Error: Book ID already exists.")
            continue
        while True:
            nvda_copies = int(input("Copies: ").strip())
            if nvda_copies < 0:
                print("Copies cannot be negative.")
                continue
            break
        nvda_books.append({"id": nvda_new_id, "title": nvda_title.upper(), "author": nvda_author,
                      "category": nvda_category, "copies": nvda_copies})
        print(f"Success: '{nvda_title.upper()}' added with ID {nvda_new_id}.")

    elif nvda_choice == 3:
        print("\n===== UPDATE AVAILABLE COPIES =====")
        nvda_book_id = input("Enter Book ID: ").strip()
        nvda_found = None
        for nvda_b in nvda_books:
            if nvda_b["id"].lower() == nvda_book_id.lower():
                nvda_found = nvda_b
                break
        if nvda_found is None:
            print("Error: Book ID not found.")
            continue
        print(f"Title: {nvda_found.get('title').upper()}")
        while True:
            nvda_copies = int(input("New number of copies: ").strip())
            if nvda_copies < 0:
                print("Copies cannot be negative.")
                continue
            break
        nvda_found["copies"] = nvda_copies
        print("Updated record:")
        for nvda_key, nvda_value in nvda_found.items():
            if nvda_key == "title":
                print(f"  {nvda_key}: {str(nvda_value).upper()}")
            else:
                print(f"  {nvda_key}: {nvda_value}")

    elif nvda_choice == 4:
        print("\n===== SEARCH BOOK =====")
        nvda_book_id = input("Enter Book ID: ").strip()
        nvda_found = None
        for nvda_b in nvda_books:
            if nvda_b["id"].lower() == nvda_book_id.lower():
                nvda_found = nvda_b
                break
        if nvda_found is None:
            print("Book ID not found.")
        else:
            if nvda_found["copies"] >= 1:
                nvda_status = "Available"
            else:
                nvda_status = "Unavailable"
            print(f"Book ID: {nvda_found['id']}")
            print(f"Title: {nvda_found['title'].upper()}")
            print(f"Author: {nvda_found['author']}")
            print(f"Category: {nvda_found['category']}")
            print(f"Available Copies: {nvda_found['copies']}")
            print(f"Availability Status: {nvda_status}")

    elif nvda_choice == 5:
        print("\n===== AVAILABLE BOOKS =====")
        nvda_available_titles = [nvda_b["title"].upper() for nvda_b in nvda_books if nvda_b["copies"] > 0]
        for nvda_t in nvda_available_titles:
            print(f"- {nvda_t}")
        if not nvda_available_titles:
            print("None.")

    elif nvda_choice == 6:
        print("\n===== UNAVAILABLE BOOKS =====")
        nvda_unavailable_titles = [nvda_b["title"].upper() for nvda_b in nvda_books if nvda_b["copies"] == 0]
        for nvda_t in nvda_unavailable_titles:
            print(f"- {nvda_t}")
        if not nvda_unavailable_titles:
            print("None.")

    elif nvda_choice == 7:
        nvda_copies = [nvda_b["copies"] for nvda_b in nvda_books]
        if not nvda_copies:
            print("No records.")
        else:
            nvda_available_count = len([nvda_c for nvda_c in nvda_copies if nvda_c > 0])
            print("\n===== INVENTORY STATISTICS =====\n")
            print(f"Total Books: {len(nvda_books)}")
            print(f"Total Available Copies: {sum(nvda_copies)}")
            print(f"Average Copies: {sum(nvda_copies) / len(nvda_copies):.2f}")
            print(f"Highest Copies: {max(nvda_copies)}")
            print(f"Lowest Copies: {min(nvda_copies)}")
            print(f"\nAvailable Books: {nvda_available_count}")
            print(f"Unavailable Books: {len(nvda_copies) - nvda_available_count}")

    elif nvda_choice == 8:
        print("\n===== UNIQUE CATEGORIES =====\n")
        nvda_categories = {nvda_b["category"] for nvda_b in nvda_books}
        for nvda_c in sorted(nvda_categories):
            print(nvda_c)
    elif nvda_choice == 9:
        nvda_copies = [nvda_b["copies"] for nvda_b in nvda_books]
        print("\n===== SORTED COPIES =====")
        print("All copies:", nvda_copies)
        print("Ascending: ", sorted(nvda_copies))
        print("Descending:", sorted(nvda_copies, reverse=True))

        nvda_asc = sorted(nvda_books, key=lambda nvda_b: nvda_b["copies"])
        print("\n--- Titles Sorted by Copies (Ascending) ---")
        for nvda_b in nvda_asc:
            print(f"- {nvda_b['title'].upper()} (Copies: {nvda_b['copies']})")

        nvda_desc = sorted(nvda_books, key=lambda nvda_b: nvda_b["copies"], reverse=True)
        print("\n--- Titles Sorted by Copies (Descending) ---")
        for nvda_b in nvda_desc:
            print(f"- {nvda_b['title'].upper()} (Copies: {nvda_b['copies']})")



    elif nvda_choice == 10:
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please select from 1 to 10.")
