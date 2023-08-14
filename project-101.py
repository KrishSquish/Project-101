import random 

def rollDie():
    dieRoll = random.randint(1,6)
    print("[-----]")
    if dieRoll == 1:
        print("[     ]\n[  0  ]\n[     ]")
    elif dieRoll == 2:
        print("[0    ]\n[     ]\n[    0]")
    elif dieRoll == 3:
        print("[0    ]\n[  0  ]\n[    0]")
    elif dieRoll == 4:
        print("[0   0]\n[     ]\n[0   0]")
    elif dieRoll == 5:
        print("[0   0]\n[  0  ]\n[0   0]")
    elif dieRoll == 6:
        print("[0   0]\n[0   0]\n[0   0]")
    print("[-----]")
    askAgain = input("Would you like to roll again? (y/n): ")
    if askAgain == "y":
        rollDie()
      
askForRoll = input("Would you like to roll the die? (y/n): ")

while askForRoll != "y":
    askForRoll = input("Would you like to roll the die? (y/n): ")

if askForRoll == "y":
    rollDie()