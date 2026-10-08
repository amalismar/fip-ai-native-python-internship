#Total for a Receipt

item1 = float(input("Enter the price of item 1: "))
item2 = float(input("Enter the price of item 2: "))
item3 = float(input("Enter the price of item 3: "))

total = item1 + item2 + item3

print(f"The total for the receipt is: ${total:.2f}") # 2f puts the number in 2 decimal places