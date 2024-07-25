#🍵Hanji kaise ho aap sabhi, this is 5th project of 100DaysofPython , I'm back and ready to code, let's start to do code...!

# ====================================== Rock, Papper, Scissor ====================================== #
import random
rock = ''' 
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

papper = '''  
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

'''

scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock,papper,scissor]

user_choice = int(input("What do you choose? 0 for Rock, 1 for Papper and 2 for scissor\n"))
if user_choice>=3:
    print("You typed an invalid choice,you lose.")
else:
    print("You choose:",game_images[user_choice])
    computer_choice = random.randint(0,2)
    print(f"Computer chose :",game_images[computer_choice])

    if user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose")
    elif computer_choice > user_choice:
        print("You lose")
    elif user_choice>computer_choice:
        print("You win!")
    elif computer_choice == user_choice:
        print("It's is a draw")




