<<<<<<< HEAD
math =input("whats the grade for the class?")
science =input("whats the garde for this class?")
english =input("whats the grade for this class?")
history =input("whats the grade for this class?")
art =input("whats the grade for this class?")
language =input("whats the grade for this class?")
pe =input("whats the grade for this class?")


def calcPoints(grade):
    if grade=="a":
        return 4.0
    if grade=="b":
        return 3.0
    if grade=="c":
        return 2.0
    if grade=="d":
        return 1.0
    if grade=="f":
        return 0

gPoints=(calcPoints(math)+calcPoints(science)+calcPoints(english)+calcPoints(history)+calcPoints(art)+calcPoints(language)+calcPoints(pe))/7
print("your GPA is  ",gPoints)
=======
math =input("whats the grade for the class?")
science =input("whats the garde for this class?")
english =input("whats the grade for this class?")
history =input("whats the grade for this class?")
art =input("whats the grade for this class?")
language =input("whats the grade for this class?")
pe =input("whats the grade for this class?")


def calcPoints(grade):
    if grade=="a":
        return 4.0
    if grade=="b":
        return 3.0
    if grade=="c":
        return 2.0
    if grade=="d":
        return 1.0
    if grade=="f":
        return 0

gPoints=(calcPoints(math)+calcPoints(science)+calcPoints(english)+calcPoints(history)+calcPoints(art)+calcPoints(language)+calcPoints(pe))/7
print("your GPA is  ",gPoints)
>>>>>>> origin/master
