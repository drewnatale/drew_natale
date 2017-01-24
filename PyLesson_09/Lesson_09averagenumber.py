from random import *
numbers = []
for i in range (0, 10):
    numbers.append(randint(0, 100))

print("Numbers...")
output = ""
for number in numbers:
    output += str(number) + " "
print(output + "\n")

def average():
    average = 0
    for number in numbers:
        average += number
    return average/len(numbers)


print("The average of the above numbers is", average())

    





















