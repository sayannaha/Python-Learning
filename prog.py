#Author: Sayan Naha
#Date: 13/06/2018
#Python Tutorial
import random
def gameWin(c, y):
    if c == y:
        return None
    elif c == "s":
        if y == "p":
            return True
        elif y == "c":
            return False
    elif c == "p":
        if y == "s":
            return False
        elif y == "c":
            return True
    elif c == "c":
        if y == "s":
            return True
        elif y == "p":
            return False
print("Computer's Turn : Stone(s) / Paper(p) / Scissors(c)...")
randNo = random.randint(1, 3)
if randNo == 1:
    comp = "s"
elif randNo == 2:
    comp = "p"
else:
    comp = "c"
you = input("Your Turn : Stone(s) / Paper(p) / Scissors(c)?...")
a = gameWin(comp, you)
print(f"Computer Chose {comp}")
print(f"You Chose {you}")
if a == None:
    print("Tie!")
elif a == True:
    print("You Win!")
else:
    print("You Lose!")