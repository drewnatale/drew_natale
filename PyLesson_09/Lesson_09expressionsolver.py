expression = input("enter mathematical expression")
equation = expression.split(" ") 

i = 0
while i < len (equation):
    if i < len (equation) and equation [i] = "*" or equation [i] = "/":
        if equation [i] = "*":
            equation[i] = int(equation[i] - 1) * (equation[i] + 1)
        else:
            if equation [i] = "/":
            equation[i] = int(equation[i] - 1) / (equation[i] + 1)

        remove equation @ i-1
        remove equation @ i
       add 1 to i
            

i = 0

while i <len (equation):
    if i < len (equation) and equation [i] = "+" or equation [i] = "-":
        if equation [i] = "+":
            equation[i] = int(equation[i] - 1) + (equation[i] + 1)

        else:
            if equation [i] ="-"
            equation [i] = int(equation[i]-1)-(equation[i] +1)

        remove equation @ i-1
        remove equation @ i
      add 1 to i 

            
            
    


 

    
    




