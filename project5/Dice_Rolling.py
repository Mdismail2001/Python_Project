import random
dicerolling = True

while dicerolling:
    print(random.randint(1,6))
    playAgin = input("Do you want to play agin?[yes/no] :")
    if playAgin == "y":
        continue
    else:
        print("game is over")
        break