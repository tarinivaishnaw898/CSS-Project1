# project for a game of stone , paper ,scissors #
import random


def game(Computer, User):
    if (Computer == User):
        return None
    elif (Computer == 's'):
        if (User == 'p'):
            return True
        elif (User == 'sc'):
            return False

    elif (Computer == 'p'):
        if (User == 's'):
            return False
        elif (User == 'sc'):
            return True


print("Computer Turn: Stone(s) , Paper(p) , Scissors(sc)")
randNo = random.randint(1, 3)
if (randNo == 1):
    Computer = 's'
if (randNo == 2):
    Computer = 'p'
if (randNo == 3):
    Computer = 'sc'

User = input("User Turn: Stone(s) , Paper(p) , Scissors(sc)")
a = game(Computer, User)
print(f"Computer choice {Computer}")
# f string is used so that we can use variables in curly braces{}....
print(f"User choice {User}")

if (a == None):
    print("The game is a tie!")
elif (a == True):
    print("User Won!!")
else:
    print("User Lose!")
