def printf(item, price):
    print("{:<6}\t{:.>10.2f}". format(item, price))




item1 = input("What is your first item? ")
price1 = float(input("What is the price? "))

item2 = input("What is your second item? ")
price2 = float(input("what is the price? "))

item3 = input("What is your third item? ")
price3 = float(input("What is the price? "))


subtotal = price1+price2+price3
tax = 0.63
total = subtotal+tax




printf(item1, price1)
printf(item2, price2)
printf(item3, price3)
printf("Subtotal",subtotal)
printf("tax",tax)
printf("total",total)








