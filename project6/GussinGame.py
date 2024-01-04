word = "Imtiyaz"
chances = 10
GussAdd = []
done = False

while not done:
    for letter in word:
        if letter.lower() in GussAdd:
            print(letter , end = " ")
        else:
            print("_", end="")

    Myguss = input(f"your chances {chances},Guss the letter :")
    GussAdd.append(Myguss.lower())
    if Myguss.lower() not in word.lower():
        chances -= 1
        if chances == 0:
            break

    done = True
    for letter in word:
        if letter.lower() not in GussAdd:
            done =False

if done:
    print(f"yes, you have won the game,the word is  {word} ")
else:
    print("you loss the game")