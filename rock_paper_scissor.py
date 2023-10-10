import random
#create random choices for the computer to pick.
computer_choice = random.choice(['rock','paper', 'scissors'])
user_choice = input("Do you want rock, paper, or scissors?")
#Show copmuter choice
print('Computer choice:', computer_choice)

if computer_choice == user_choice:
    print('tie')
elif user_choice == 'rock' and computer_choice == 'scissors':
    print('win')
elif user_choice == 'paper' and computer_choice == 'rock':
    print('win')    
elif user_choice == 'scissors' and computer_choice == 'paper':
    print('win')
else:
    print('you lose')
