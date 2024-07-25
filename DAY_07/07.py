# 🍵, Hanji Kaise ho aap sabhi ,This is 7th day of Pyhton Challenge.I’m back and ready to code,Let's roll the code!

# start 
# generate random word
# generate as many blanks as letters in world
# ask the user to guess a letter
# is the guessed letter in world?
# yes                                                                     no
# replace the blank with the letter                                      lose a life
# are all the blanks filed?                                             have they run out of lives?
# no     yes                                                            yes      no ---------- check condition
#                                             game over

#import random
# version -----------------> 1
# word_list = ["ardvark","baboon","camel"]

# chosen_word=random.choice(word_list)
# # print(chosen_word)
# guess=input("Guess a letter:").lower()
# for letter in chosen_word:
#     if letter==guess:
#         print("Right")
#     else:
#         print("Wrong")

# # version -----------------> 2

# word_list = ['ardvark','baboon','camel']
# chosen_word = random.choice(word_list)

# print(f'Pssst, the solution is {chosen_word}')

# display = []
# word_length = len(chosen_word)

# for _ in range(word_length):
#     display+="_"
# print(display)

# guess = input("Guess a letter:").lower()

# for position in range(word_length):
#     letter = chosen_word[position]
#     if letter == guess:
#         display[position] = letter
    
# print(display)

# version -----------------> 3

# word_list = ['ardvark','baboon','camel']
# chosen_word = random.choice(word_list)

# print(f'Pssst, the solution is {chosen_word}')

# display = []
# word_length = len(chosen_word)

# for _ in range(word_length):
#     display+="_"
# print(display)

# end_of_game = False

# while not end_of_game:
#     guess = input("Guess a letter:").lower()

#     for position in range(word_length):
#         letter = chosen_word[position]
#         if letter == guess:
#             display[position] = letter
        
#     print(display)

#     if "_" not in display:
#         end_of_game = True
#         print("You win.")
        
# version -----------------> 4
# import random

# word_list = ['ardvark', 'baboon', 'camel']
# chosen_word = random.choice(word_list)

# print(f'Pssst, the solution is {chosen_word}')  # For testing purposes

# display = ['_'] * len(chosen_word)
# lives = 6

# print(display)

# while lives > 0 and '_' in display:
#     guess = input("Guess a letter: ").lower()

#     if guess in display:
#         print(f"You've already guessed {guess}")
#         continue

#     if guess in chosen_word:
#         for position in range(len(chosen_word)):
#             if chosen_word[position] == guess:
#                 display[position] = guess
#     else:
#         lives -= 1
#         print(f"Incorrect guess. You have {lives} lives left.")
        
#     print(display)

# if lives == 0:
#     print("You lose. Game over.")
#     print(f'The word was {chosen_word}')
# else:
#     print("You win.")


# version -----------------> 5
import random
from word_list import word_list
import os
os.system('cls')
chosen_word = random.choice(word_list)

print(f'Pssst, the solution is {chosen_word}') 

display = ['_'] * len(chosen_word)
lives = 6

print(display)

while lives > 0 and '_' in display:
    guess = input("Guess a letter: ").lower()
    os.system('cls')

    if guess in display:
        print(f"You've already guessed {guess}")
        continue

    if guess in chosen_word:
        for position in range(len(chosen_word)):
            if chosen_word[position] == guess:
                display[position] = guess
    else:
        lives -= 1
        print(f"Incorrect guess. You have {lives} lives left.")
        
    print(display)

if lives == 0:
    print("You lose. Game over.")
    print(f'The word was {chosen_word}')
else:
    print("You win.")
