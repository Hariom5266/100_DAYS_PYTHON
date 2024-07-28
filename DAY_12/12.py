# 🍵 , Hanji Kaise ho aap sabhi this is 12th day of #100Days_Of_Python I'm back and ready to code.let's start to do code.

# ===================== Scope, Namespace and etc ===================== #

#  think in our house we have tree of apple who can acess the apple obviously our family memeber and think tree on road then who can access those apple, anyone write. like that we can visuvalize tree as a variable and apple as a value of varabile and home or road is scope of variable.

enemies =1 

def increase_enemies():
    enemies=2
    print(f"Enemies inside fnc: {enemies}")

increase_enemies()
print(f"enemies outside fnc: {enemies}")

# Local Scope -- it exist at end of fnc
def drink_potion():
    potion_strength=2 # Local Scope
    print(potion_strength)
drink_potion()

print(potion_strength)

# Global Scope
player_health = 10

def game():
    def drink_potion():
        potion_strength=2 # Local Scope
        player_health=50
        print(player_health)
    drink_potion()

game()
print(player_health)

# There is no Block Scope in if - else, in loops local scope in only fnc

game_level = 3
def create_enemy():
    enemies = ["Skeleton","Zombie","Alien"]
    if game_level<5:
        new_enemy = enemies[0]

print(new_enemy)


# Modifying Global Scope

enemies = "Skeleton"
def increase_enemies():
    # # we cant able to do like this : -------------------------
    # enemies="Skeleton"
    # enemies+="Zombies" # --> crete new local var enemies by python
    # #  -------------------------------------------------- #
    global enemies # here we should use return enemies not do modify it for best practices
    enemies="Zombies"
    print(f"Enemies inside fnc: {enemies}")

print(f"Enemies outside fnc: {enemies}")
increase_enemies()
print(f"Enemies outside fnc: {enemies}")

# # ===================== Python Contsnts and Globals ===================== 

PI = 3.14159
URL = "https://www.google.com"
TWITTER_MANDLE="@yu_angela"

def calc():
    TWITTER_MANDLE="Hari"
    print(TWITTER_MANDLE)
calc()
print(TWITTER_MANDLE)











