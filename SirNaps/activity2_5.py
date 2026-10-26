nvda_name= input("Enter customer name: ")
nvda_previous = float(input("Enter previous reading : "))
nvda_current = float(input("Enter current reading : "))
nvda_rate = float(input("Enter kWh rate : "))


nvda_consumption = nvda_current - nvda_previous
nvda_total = nvda_consumption * nvda_rate

lineone = "-"
line = "="
print(line*20)
print("Electricity Bill")
print(line*20)
print(f"Customer: {nvda_name}")
print(f"Consumption : {nvda_consumption}")
print(f"Rate per kWh : {nvda_rate:.2f}")
print(f"Total bill : {nvda_total:.2f}")