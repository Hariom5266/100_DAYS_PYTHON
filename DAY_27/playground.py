
def add(*args):
    for n in args:
        print(n)
    
add(1,2,3,4,5,6,7,8,9)

def calculate(**kwarges):
    print(kwarges)
    
calculate(add=3,multiple=5)

class Car:
    def __init__(self,**kw):
        self.make=kw["make"]
        self.model=kw["model"]
        # can use get meathod useing . operator
        
my_car=Car(make="Nissan",model="GT-8")
print(my_car)