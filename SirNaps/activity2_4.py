nvda_product = input("Enter product name: ")
nvda_price = float(input("Enter Price : "))
nvda_quantity = int(input("Enter Quantity : "))
nvda_subtotal = nvda_price * nvda_quantity
nvda_discount = nvda_subtotal * 0.01
nvda_total = nvda_subtotal - nvda_discount

lineone = "-"
line = "="
print(line*20)
print("Sales Receipt")
print(line*20)
print(f"Product: {nvda_product}")
print(f"Price: {nvda_price}")
print(f"Quantity: {nvda_quantity}")
print(lineone*20)
print(f"Subtotal : {nvda_subtotal}")
print(f"Discount : {nvda_discount}")
print(f"Total : {nvda_total}")