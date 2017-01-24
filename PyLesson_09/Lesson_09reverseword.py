myList = ["cat", "dog", "fish", "rabbit", "bird"]

print("in order")

output=""
for i in myList:
    output += i + " "
print(output)

print("\nReversed...")

def reverse():
    for i in range(len(myList)-1, -1, -1):
        print(myList[i])
        

reverse()

