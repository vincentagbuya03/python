import os
import csv

field_names = ["id", "name", "age", "date", "time", "reason"]


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def read_appointments():
    """Reads all appointments from appointments.csv safely, supporting both files with and without headers."""
    if not os.path.exists("appointments.csv") or os.path.getsize("appointments.csv") == 0:
        return []

    appointments = []
    with open("appointments.csv", "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        header = None
        for row in reader:
            if not row or not any(cell.strip() for cell in row):
                continue
            first = row[0].strip().lower()
            if first in ("id", "appointment id"):
                header = [h.strip().lower() for h in row]
                continue

            if header:
                row_dict = dict(zip(header, row))
                appointments.append({
                    "id": row_dict.get("id", "").strip(),
                    "name": (row_dict.get("name") or row_dict.get("patient name", "")).strip(),
                    "age": row_dict.get("age", "").strip(),
                    "date": row_dict.get("date", "").strip(),
                    "time": row_dict.get("time", "").strip(),
                    "reason": row_dict.get("reason", "").strip()
                })
            else:
                appointments.append({
                    "id": row[0].strip() if len(row) > 0 else "",
                    "name": row[1].strip() if len(row) > 1 else "",
                    "age": row[2].strip() if len(row) > 2 else "",
                    "date": row[3].strip() if len(row) > 3 else "",
                    "time": row[4].strip() if len(row) > 4 else "",
                    "reason": row[5].strip() if len(row) > 5 else ""
                })
    return appointments


def get_next_appointment_id():
    """Computes the next appointment ID (e.g. P001 -> P002) based on existing records."""
    appointments = read_appointments()
    ids = []
    for appt in appointments:
        val = appt.get("id", "")
        digits = "".join(filter(str.isdigit, val))
        if digits:
            ids.append(int(digits))
    if ids:
        return f"P{max(ids) + 1:03d}"
    return "P001"


def register_appointment():
    clear_console()
    print("=" * 100)
    appointment_id = get_next_appointment_id()

    print(f"Generated Appointment ID : {appointment_id}")
    name = input("Enter patient name : ")
    try:
        age = int(input("Enter patient age : "))
    except ValueError:
        print("Invalid age!")
        print("=" * 100)
        return
    date = input("Enter appointment date : ")
    time = input("Enter appointment time : ")
    reason = input("Enter reason for appointment : ")

    file_exists = os.path.exists("appointments.csv") and os.path.getsize("appointments.csv") > 0
    with open("appointments.csv", "a", newline="", encoding="utf-8") as file:
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
    appointments = read_appointments()
    if not appointments:
        print("No appointments found.")
    else:
        for appt in appointments:
            print(f"{appt['id']}, {appt['name']}, {appt['age']}, {appt['date']}, {appt['time']}, {appt['reason']}")
    print("=" * 100)


def search_appointment():
    clear_console()
    print("=" * 100)
    name = input("Enter patient name : ")
    found = False
    appointments = read_appointments()
    search_term = name.strip().lower()
    for appt in appointments:
        if search_term in appt["name"].lower() or search_term == appt["id"].strip().lower():
            print(f"{appt['id']}, {appt['name']}, {appt['age']}, {appt['date']}, {appt['time']}, {appt['reason']}")
            found = True
    if not found:
        print("No appointment found.")
    print("=" * 100)


def count_appointment_by_date():
    clear_console()
    print("=" * 100)
    date = input("Enter date : ")
    count = 0
    appointments = read_appointments()
    search_date = date.lower().replace(" ", "")
    for appt in appointments:
        if search_date in appt["date"].lower().replace(" ", ""):
            count += 1
    print(f"Number of appointments on {date} : {count}")
    print("=" * 100)

    print("=" * 100)