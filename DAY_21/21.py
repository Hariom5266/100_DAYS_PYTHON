# 🍵 , Hanji Kaise ho aap sabhi this is 21th day of #100Days_Of_Python I'm back and ready to code.let's start to do code.

# ==================== Inheritance ==================== #

# we program chef robot it has bake(),stir(), and measure() like fnc
# then we won't to program pasty chef it has much fnc of chef but also have another fnc like bake(), stir(), measure(), knead(), whisk()

# class fish(animal): => here fish inhertiede from animal
#     def __init__(self):
#         super().__init__()

class Animal:
    def __init__(self):
        self.num_eyes=2
    
    def breathe(self):
        print("Inhale,Exhale.")
        
class Fish(Animal):
    def __init__(self):
        super().__init__()
    
    def breathe(self):
         super().breathe()
         print("Doing this in underwater")
    
    def swim(self):        
        print("Moving in water.")
        
nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)

# ==================== Slicing ==================== #
piano_keys=['a','b','c','d','e','f','g']
print(piano_keys[2:5])





