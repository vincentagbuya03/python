
nvda_vehicle_type = input("Enter vehicle type (Motorcycle Car Van): ").strip().lower()
nvda_hours_input = input("Enter number of hours parked: ")
nvda_hours = float(nvda_hours_input)
nvda_classification = ""
nvda_fee = 0

if nvda_hours <= 0:
    print("Invalid parking duration.")
else:
    if nvda_vehicle_type == "motorcycle":
        if nvda_hours <= 3:
            nvda_classification = "Short Stay"
            nvda_fee = 10
        else:
            nvda_classification = "Extended Stay"
            nvda_fee = 20
        print(f"Classification: {nvda_classification}")
        print(f"Fee: {nvda_fee}")
    else:
        if nvda_vehicle_type == "car":
            if nvda_hours <= 3:
                nvda_classification = "Short Stay"
                nvda_fee = 20
            else:
                nvda_classification = "Extended Stay"
                nvda_fee = 40
            print(f"Classification: {nvda_classification}")
            print(f"Fee: {nvda_fee}")
        else:
            if nvda_vehicle_type == "van":
                if nvda_hours <= 3:
                    nvda_classification = "Short Stay"
                    nvda_fee = 20
                else:
                    nvda_classification = "Extended Stay"
                    nvda_fee = 40
                print(f"Classification: {nvda_classification}")
                print(f"Fee: {nvda_fee}")
            else:
                print("Invalid vehicle type.")