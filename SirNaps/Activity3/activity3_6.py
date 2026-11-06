

nvda_user_type = input("Enter user type (Student/Faculty/Staff/Visitor): ").strip().lower()
nvda_laboratory_status = input("Enter laboratory status (Open/Closed): ").strip().lower()
nvda_valid_id = input("Valid identification status (Yes/No): ").strip().lower()
nvda_time_input = input("Enter time of access (0-23 hour): ").strip()
nvda_access_time = float(nvda_time_input)
nvda_open_hour = 8
nvda_close_hour = 17
nvda_within_schedule = nvda_access_time >= nvda_open_hour and nvda_access_time <= nvda_close_hour

if nvda_laboratory_status == "open":
    if nvda_user_type == "student":
        if nvda_valid_id == "yes" and nvda_within_schedule == True:
            print("Access granted.")
        else:
            print("Access denied. Valid Identification Required or Access Time is Outside Schedule.")
    elif nvda_user_type == "faculty" or nvda_user_type == "staff":
        if nvda_valid_id == "yes" and nvda_laboratory_status == "open":
            print("Access granted. Welcome to the laboratory.")
        else:
            print("Access denied. ")
    elif nvda_user_type == "visitor":
        print("Access denied. Valid Identification Required")
    else:
        print("Invalid user type.")
else:
    if nvda_laboratory_status == "closed":
        print("Access denied. Laboratory is closed.")
    else:
        print("Invalid laboratory status.")
