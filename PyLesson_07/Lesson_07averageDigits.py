number = int(input("enter a number"))
digits = 0
average = 0

def avDigits():
    global average, digits
    num = number 
    while num > 0:#exits when all the digits are gone from num
        digits += 1 #count the digits
        average += num % 10 #adding the last digit to average
        num = int(num / 10) #taking the last digit away from num
    average /= digits #calculate the average

avDigits()
print("the sum of the digits in" , number, "is" , average) 

