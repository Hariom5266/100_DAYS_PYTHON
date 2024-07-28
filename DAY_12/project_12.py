# 🍵 , Hanji Kaise ho aap sabhi this is 12th day of #100Days_Of_Python I'm back and ready to code.let's start to do code.

# ======================== RESOURCES ======================== #
# https://appbrewery.github.io/python-day12-demo/
# https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20

# ======================== GUESS THE NUMBER ======================== #
import art
from random import randint
EASY_LEVEL_TURNS=10
HARD_LEVEL_TURNS=5

def check_answer(guess,answer,turns):
    """Checks answer agianst guess. Returns remaining turns."""
    if guess>answer:
        print("Too high.")
        return turns-1
    elif guess<answer:
        print("Too low.")
        return turns-1
    else:
        print(f"You got it! The answer was {answer}.")
        
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level=="easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS        

def game():
    print(art.logo)
    print("Welcom to the Number Guessing Game!")
    print("I'm thinking of a number between 1 to 100.")
    answer=randint(1,100)
    print(f"Pssst, the correct answer is {answer}")

    turns = set_difficulty()
    guess=0
    while guess!=answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess=int(input("Make a guess:"))
        turns = check_answer(guess=guess,answer=answer,turns=turns)
        if turns==0:
            print("You've run out of gusses, you lose.")
            return
        elif guess!=answer:
            print("Guess again.")

game()
print("\n")
print(art.devloper_name)



                                                                                                                      
                                                                                                                      
                                                                                                                      
                                                                                                                      
                                                                                                                      
                                                                                                                      
                                                                                                                      
                                                                                                                      
                                                                                                                      
                                                                                                                      
                                                                                                                      
                                                                                                                      







