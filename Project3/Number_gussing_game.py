import random

na_number = random.randrange(1,100)

gu_number = int(input("Guess the number :"))

if gu_number > na_number :
    print(na_number)
    print("the guess number is high")

elif gu_number < na_number:
    print(na_number)
    print("the guess number is low")

else:
    print(na_number)
    print("the guess number is correct")
