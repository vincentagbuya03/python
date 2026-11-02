import os
import csv

field_names = ["id", "name", "age", "date", "time", "reason"]


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def register_appointment():
    clear_console()
    print("=" * 100)
    appointment_id = "P001"
    try:
        with open("appointments.csv", "a", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            ids = []
            for row in reader:
                val = row.get("id") or row.get("Appointment ID") or ""
                digits = "".join(filter(str.isdigit, val))
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

    file_exists = os.path.exists("appointments.csv") and os.path.getsize("appointments.csv") > 0
    with open("appointments.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=field_names)
        if not file_exists:
            writer.writeheader()
        writer.writerow({
            "id": appointment_id,
            "name": name,
            "age": age,
            "date": date,
            "time": time,
            "reason": reason
        })
    print(f"Appointment registered successfully (ID: {appointment_id})")
    print("=" * 100)


def view_appointment():
    clear_console()
    print("=" * 100)
    try:
        with open("appointments.csv", "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            rows = list(reader)
            if not rows:
                print("No appointments found.")
            else:
                for row in rows:
                    id_val = row.get("id") or row.get("Appointment ID") or ""
                    name_val = row.get("name") or row.get("Patient Name") or ""
                    age_val = row.get("age") or row.get("Age") or ""
                    date_val = row.get("date") or row.get("Date") or ""
                    time_val = row.get("time") or row.get("Time") or ""
                    reason_val = row.get("reason") or row.get("Reason") or ""
                    print(f"{id_val}, {name_val}, {age_val}, {date_val}, {time_val}, {reason_val}")
    except FileNotFoundError:
        print("No appointments found.")
    print("=" * 100)


def search_appointment():
    clear_console()
    print("=" * 100)
    name = input("Enter patient name : ")
    found = False
    try:
        with open("appointments.csv", "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            search_term = name.strip().lower()
            for row in reader:
                id_val = row.get("id") or row.get("Appointment ID") or ""
                name_val = row.get("name") or row.get("Patient Name") or ""
                age_val = row.get("age") or row.get("Age") or ""
                date_val = row.get("date") or row.get("Date") or ""
                time_val = row.get("time") or row.get("Time") or ""
                reason_val = row.get("reason") or row.get("Reason") or ""

                # Search by patient name or by ID
                if search_term in name_val.lower() or search_term == id_val.strip().lower():
                    print(f"{id_val}, {name_val}, {age_val}, {date_val}, {time_val}, {reason_val}")
                    found = True
        if not found:
            print("No appointment found.")
    except FileNotFoundError:
        print("No appointments found.")
    print("=" * 100)


def count_appointment_by_date():
    clear_console()
    print("=" * 100)
    date = input("Enter date : ")
    count = 0
    try:
        with open("appointments.csv", "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            search_date = date.lower().replace(" ", "")
            for row in reader:
                date_val = row.get("date") or row.get("Date") or ""
                if search_date in date_val.lower().replace(" ", ""):
                    count += 1
        print(f"Number of appointments on {date} : {count}")
    except FileNotFoundError:
        print(f"Number of appointments on {date} : 0")
    print("=" * 100)