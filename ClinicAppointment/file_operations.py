import csv



def register_appointment():

    appointment_id = "P001"
    try:
        with open("appointments.csv", "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            rows = [row for row in reader if row]
            if rows:
                ids = []
                for row in rows:
                    digits = "".join(filter(str.isdigit, row[0]))
                    if digits:
                        ids.append(int(digits))
                if ids:
                    appointment_id = f"P{max(ids) + 1:03d}"
                else:
                    appointment_id = "P001"
    except (FileNotFoundError, ValueError):
        appointment_id = "P001"

    print(f"Generated Appointment ID : {appointment_id}")
    name = input("Enter patient name : ")
    try:
        age = int(input("Enter patient age : "))
    except ValueError:
        print("Invalid age!")
        return
    date = input("Enter appointment date : ")
    time = input("Enter appointment time : ")
    reason = input("Enter reason for appointment : ")

    with open("appointments.csv", "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([appointment_id, name, age, date, time, reason])
    print(f"Appointment registered successfully (ID: {appointment_id})")


def view_appointment():
    try:
        with open("appointments.csv", "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            for row in reader:
                if row:
                    print(", ".join(row))
    except FileNotFoundError:
        print("No appointments found.")


def search_appointment():
    name = input("Enter patient name : ")
    found = False
    try:
        with open("appointments.csv", "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            for row in reader:
                if not row:
                    continue
                # Search by patient name (row[1]) or by ID (row[0])
                search_term = name.strip().lower()
                if len(row) >= 6:
                    match = (search_term in row[1].lower()) or (search_term == row[0].strip().lower())
                else:
                    match = (search_term in row[0].lower())

                if match:
                    print(", ".join(row))
                    found = True
        if not found:
            print("No appointment found.")
    except FileNotFoundError:
        print("No appointments found.")


def count_appointment_by_date():
    date = input("Enter date : ")
    count = 0
    try:
        with open("appointments.csv", "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            for row in reader:
                date_val = row[3] if len(row) >= 6 else (row[2] if len(row) >= 3 else "")
                if date.lower().replace(" ", "") in date_val.lower().replace(" ", ""):
                    count += 1
        print(f"Number of appointments on {date} : {count}")
    except FileNotFoundError:
        print(f"Number of appointments on {date} : 0")
