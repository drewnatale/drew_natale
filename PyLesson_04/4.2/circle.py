def calcArea(r):
    global circle
    return((r*r)*3.14)


circle = 0
radius = int(input("what is the radius?"))

print("the area of a circle with a radius of", radius, "is", calcArea(radius))


