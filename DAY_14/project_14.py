# 🍵 , Hanji Kaise ho aap sabhi this is 14th day of #100Days_Of_Python I'm back and ready to code.let's start to do code.

# ==================== Higher and Lower Game ==================== #

# Breackdown the problen 
# make to do list for project which task is do
# write comment and write code run code fix code
# next task


# here want to make game like that randomly choice different personality and compare followers between them and choose by also user and at the end of the program user can see their score

import random
import os
from art import logo, vs
from game_data import data

def get_random_account():
    """Get random Personality Data"""
    return random.choice(data)

def format_data(account):
    """Format account data for display"""
    name = account["name"]
    desc = account["description"]
    country = account["country"]
    return f"{name}, a {desc} from {country}"

def check_answer(more_follower,person1_follower,person2_follower):
    if person1_follower>person2_follower:
        return more_follower== 'A'
    else:
        return more_follower=='B'
    

def game():
    score = 0
    game_should_continue = True
    person1_account = get_random_account()
    person2_account = get_random_account()

    while game_should_continue:
        person1_account=person2_account
        person2_account=get_random_account()
        while person1_account==person2_account:
            person2_account=get_random_account()
        
        print("Compare A:", format_data(person1_account))
        print(vs)
        print("Against B:", format_data(person2_account))

        more_follower = input("Who has more follower? Type 'A' or 'B': ").upper()
        person1_follower = person1_account['follower_count']
        person2_follower=person2_account['follower_count']
        is_correct=  check_answer(more_follower,person1_follower,person2_follower)

        os.system('cls');
        print(logo)
        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")
    
game()


 
# then choose by user and followers are higher or lower

# if guess is right then another guess else print score


