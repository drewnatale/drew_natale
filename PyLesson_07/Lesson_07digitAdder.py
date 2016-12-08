number = int(input("what is the number?"))
num = number
sum = 0
             
while num > 0:
      sum += num % 10
      num = int(num / 10)


print("the sum of the digits in" , number, "is" , sum)
