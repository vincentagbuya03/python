nvda_customer_name = input("Enter customer name: ")
nvda_order_amount = float(input("Enter total order amount (in Php): "))
nvda_delivery_distance = float(input("Enter delivery distance in kilometers: "))
nvda_membership_input = input("Customer membership status (Yes/No): ").strip().lower()

nvda_is_member = nvda_membership_input == "yes" or nvda_membership_input == "y"

nvda_premium_minimum = 3000
nvda_standard_max_distance = 20

nvda_shipping_classification = ""

if nvda_order_amount <= 0:
    nvda_shipping_classification = "Invalid Order"
elif nvda_is_member and nvda_order_amount >= nvda_premium_minimum:
    nvda_shipping_classification = "Premium Delivery"
elif nvda_delivery_distance <= nvda_standard_max_distance:
    nvda_shipping_classification = "Standard Delivery"
else:
    nvda_shipping_classification = "Extended Delivery"

print(f"Customer: {nvda_customer_name}")
print(f"Shipping Classification: {nvda_shipping_classification}")
