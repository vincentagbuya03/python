nvda_num = int(input("Enter a number: "))

nvda_num_str = str(abs(nvda_num))
nvda_digits = len(nvda_num_str)

nvda_oddDigits = 0
nvda_evenDigits = 0
nvda_digit_sum = 0

for char in nvda_num_str:
    d = int(char)
    nvda_digit_sum += d
    if d % 2 == 0:
        nvda_evenDigits += 1
    else:
        nvda_oddDigits += 1

print(f"Number of digits: {nvda_digits}")
print(f"Odd digits: {nvda_oddDigits}")
print(f"Even digits: {nvda_evenDigits}")
print(f"Sum of digits: {nvda_digit_sum}")