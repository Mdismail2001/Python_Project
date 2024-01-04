answer = input("Are you play this game: [Yes/No]")
if answer == "yes":
    print("You are well come to game")

    answer = input("Are you going to [jungle/cave] :")

    if answer == "jungle":
        print("one hour letter a tiger come in front of you")
        answer = input("Do you fight the tiger?[yes/no] :")
        if answer == "yes":
            print("You are die because of the tiger is string getter then you ")
        elif answer == "no":
            print("Go back to the jungle")

    elif answer == "cave":
        print("A python sleeping in the entre side of cave")
        answer = input("Do you fight the python?[yes/no] :")
        if answer == "yes":
            print("You are die because of the python is string getter then you ")
        elif answer == "no":
            print("Go back to the cave")


else:
    print("Atlist one time try to play this game")