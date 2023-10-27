import random
#This function will return a randon number 1-6 assigned to the variable roll
roll = random.randint(1,6)
#/n indicates that the line ends here and remaining characters will be displayed in a new line
guess = int(input('Guess the dice roll:\n'))
if guess == roll:
    #concatenate the number they roll
    print("Correct! They rolled a " + str(roll))
else:
    print("Wrong! They rolled a " + str(roll))
