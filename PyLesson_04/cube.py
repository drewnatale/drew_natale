
def calcSurf(s):
    return ((s*s)*6)

side = int(input("how long are the sides?"))

print("the surface area of a cube whose sides are", side, "in length is", calcSurf(side))
