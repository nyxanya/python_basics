
from random import random

i = int(random() * 1000)
att=0
# random number

# until guess is correct 
guess = False
while guess == False:
    inp = input("Guess the secret number: ")
    att = att + 1
    if int(inp) > i:
        print("Too High!")


    elif int(inp) < i:
        print("Too Low")


    else:  
        print("You're Correct!")
        guess = True

# count number of inputs
if att < 10:
    print("You Did Awesome")
elif att < 15:
    print("You Did Good")
elif att < 19:
    print("You Did Average")
else:
    print ("You Didn't Do well")
# accept number