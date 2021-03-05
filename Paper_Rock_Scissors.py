import random

options = [["rock", "paper", "scissors"],["paper", "scissors", "rock"],["scissors", "rock", "paper"]]
print("Choose rock, paper or  scissors")

def userChoice():
    while True:
        userChoice = str.lower(input(""))
                
        if userChoice != "rock" and userChoice != "paper" and userChoice != "scissors" :
            print("Unfortunately, you have not chosen a valid option, check if you typed it correctly!")
        else:
            break
    if userChoice == "rock":
        userChoice = 0
    elif userChoice == "paper":
        userChoice = 1
    else:
        userChoice = 2

    return userChoice


def winState():
    winState = random.randint(0,2)

    #0 means draw, 1 means win, 2 means loss

    if winState == 0:
        message = "draw"
    elif winState == 1:
        message = "lose"
    else:
        message = "win"

    return [str(winState), message]

while True:
    winnerArray = winState()    
    print("You", winnerArray[1], "\nThe computer picked:", options[userChoice()][int(winnerArray[0])])
    print("\n")
    print("Choose, rock, paper or scissors")
