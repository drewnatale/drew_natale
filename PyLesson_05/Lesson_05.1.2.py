w=float(input("what is your weight?"))
h=float(input("what is your weight?"))

bmi= (703*w)/h**2

print("bmi: ",bmi)


if bmi<18.5:
    print("condition ia underweight")
if 18.5<bmi<24.9:
    print("condition are normal")
if 25<bmi<29.9:
     print("condition overweight")
if 29.9<bmi<34.9:
    print("condition obese")
if 35<bmi<39.9:
    print("condition very obese")
if bmi>39.9:
    print("condition morbidly obese")


