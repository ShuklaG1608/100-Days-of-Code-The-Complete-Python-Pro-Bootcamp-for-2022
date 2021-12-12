import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
'''Rock wins against scissors.
Scissors win against paper.
Paper wins against rock.
Type 0 for Rock, 1 for Paper or 2 for Scissors.
'''
print('Welcome to the Rock, Paper, Scissors game.')
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
computer_choice = random.randint(0,2)

if(computer_choice == 0):
  if(user_choice ==0):
    print("Computer Chose Rock, & You Chose Rock, Game Draw!\n",rock)
  elif(user_choice == 1):
    print("Computer Chose Rock, & You Chose Paper, You Won!\n",paper)
  elif(user_choice == 2):
    print("Computer Chose Rock,& You Chose Scissors, Computer Won!\n",rock)
  else:
    print(" You have made an Invalid Choice, Game Over !!")
  

elif(computer_choice == 1):
  if(user_choice ==0):
    print("Computer Chose Paper, & You Chose Rock, Computer Won!\n",rock)
  elif(user_choice == 1):
    print("Computer Chose Paper, & You Chose Paper, Game Draw!\n",paper)
  elif(user_choice == 2):
    print("Computer Chose Paper, & You Chose Scissors, You Won!\n",scissors)
  else:
    print(" You have made an Invalid Choice, Game Over !!")


elif(computer_choice == 2):
  if(user_choice ==0):
    print("Computer Chose Scissors, & You Chose Rock, You Won!\n",rock)
  elif(user_choice == 1):
    print("Computer Chose Scissors, & You Chose Paper, Computer Won!\n",scissors)
  elif(user_choice == 2):
    print("Computer Chose Scissors, & You Chose Scissors, Game Draw!\n",scissors)
  else:
    print(" You have made an Invalid Choice, Game Over !!")

else:
  print(" You have made an Invalid Choice, Game Over !!")
