# 🍵, Hi this is 3rd day project of python I'm back and eady to code.
# ==================== Treasure isalnd ==================== #

island = '''                                            
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_| 
 '''

print(island)
print("Wlecome to treasure island.")
print("Your mission to find the treasue...!")
path = input('''You at crossroad, where you want to go left or right? write "left" or "right"\n ''')
if path == "left":
    path = input("How you want to cross ocean by swim and want to do wait?\n")
    if path == "wait":
        path = int(input("choose any room? 0 for red, 1 for yellow and 2 for blue.\n"))
        if path == 0:
            print("Game over!.")
        elif path == 1:
            print("You win the game.! You have many rupees")
        else:
            print("Game over!.")
    else :
        print("Game Over.!")
else :
    print("Game over!.")