# 🍵 , Hanji Kaise ho aap sabhi this is 17th day of #100Days_Of_Python I'm back and ready to code.let's start to do code.

# ====================== Create Own Classses ====================== #

# PascalCase use for classes name, also we have camelCase, and in use snake_case for variables

class User:
    # pass # => make empty classes
    # def __init__(self,user_id,username,followers=0):
    def __init__(self,user_id,username):
        self.id=user_id
        self.username=username
        # self.followers=0 # can set default here or as a fnc parameters
        self.followers=0
        self.following=0
        # print("New use is created.")
# when fnc associated with obj that called method
    def follow(self,user):
        user.followers+=1
        self.following+=1

# user_1=User("013","Hariom Joshi",13)
user_1=User("013","Hariom Joshi")
user_2=User("0013","Software Engineer")
print(user_1.id,user_1.username)

print()

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)


# user_1.id="001"
# user_1.username="Hariom"
# print(user_1.username)

# user_2=User()
# user_3=User()

# if we have many user than we need to constructor => it define what things are perform when object is created.

#constructot:
    # def __init/it is name of constructor/it is special fnc__(self):
        # initialise attributes

# print(user_1)







