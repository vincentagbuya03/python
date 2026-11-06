nvda_num = int(input("Enter a number: "))



while nvda_num >= 1:
    for i in range(1,nvda_num+1):
        print(i,end="")
    print()
    nvda_num -= 1

