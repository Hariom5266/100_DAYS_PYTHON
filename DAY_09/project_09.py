# 🍵, Hanji Kaise ho aap sabhi ,This is 9th day of Pyhton Challenge.I’m back and ready to code,Let's roll the code!


# ==================== Silent auction program ==================== #
import os

var = '''
___________
        /
)_______(
|"""""""|_.-._,.---------.,_.-._
|       | | |               | | '-.
|       |_| |_             _| |_..-'
|_______| '-' -----------'-'
)"""""""(
/_________\
.-------------.
/_______________\
'''

print(var)

import os

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""  # Initialize the winner variable
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]  # Corrected assignment
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ₹{highest_bid}")

while not bidding_finished:
    name = input("What is your name?\n")
    price = int(input("What is your bid? ₹\n"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    
    if should_continue.lower() == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue.lower() == "yes":
        os.system('cls' if os.name == 'nt' else 'clear')  # Cross-platform console clear
    else:
        print("Invalid input. Please type 'yes' or 'no'.")

# https://pythontutor.com/ ------> for visuvalize the python code








