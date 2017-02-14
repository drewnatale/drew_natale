import random;

player = random.randint(1,6)
computer = random.randint(1,6)

print("you rolled a" , player)

print("computer rolled a" , computer)

def rollDice():
    winner = ""
    if player > computer:
        winner = "player"
    if computer > player:
        winner = "computer"
        
    print ("the winner is" , winner)
rollDice()

    
    

