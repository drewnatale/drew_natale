def problem(p,r,n,t):
    return(p*((1+(n/r))**(n*t)))

rate = float(input("What is the interest rate???"))
principal = float(input("what is the principal?"))
number = float(input("what is the number of times the loan is compounded per year?"))
time = float(input("what is the life of the loan?"))

cost = float((problem(principal,rate,number,time))/(12))


print("your cost per month is: ", cost)

def problm(h,l,w):
    return((h*l*w)/12**3)

height=int(input("what is the height?"))
length=int(input("what is the length?"))
width=int(input("what is the width?"))

print("the volume in ft. es: ", problm(height,length,width))


