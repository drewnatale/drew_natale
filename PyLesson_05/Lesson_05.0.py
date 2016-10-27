def calcDisc(sub):
    if subtotal >= 2000:
        return subtotal * 0.15
    if subtotal < 2000:
        return 0
def printf(item, price):
    print("{:<10}..........{:<10.2f}".format(item, price))

item1 = (input("what is item 1?"))
price1 = float(input("what is price 1?"))
item2 = (input("what is item 2?"))
price2 = float(input("what is price 2?"))
item3 = (input("what is item 3?"))
price3 = float(input("what is price 3?"))
item4 = (input("what is item 4?"))
price4 = float(input("what is item 4?"))


subtotal = price1+price2+price3+price4
discount = calcDisc(subtotal)
tax = subtotal * 0.08
total= subtotal-discount+tax

printf(item1, price1)
printf(item2, price2)
printf(item3, price3)
printf(item4, price4)


printf("Subtotal: ", subtotal)
printf("discount: ", discount)
printf("tax: ", tax)
printf("total ", total)
print("Thank You")

#if subtotal is >= 2000 return subtotal * 0.15, otherwise return 0
