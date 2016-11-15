def calcSurf(s):
    global cube
    return ((s*s)*6)

circle = 0
side = int(input("how long are the sides?"))

print("the surface area of a cube whose sides are", side, "in length is", calcSurf(side))
