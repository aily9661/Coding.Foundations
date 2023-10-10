class myClass:
    def __init__(self, name, age): #initialize object ALWAYS RAN
        self.name = name
        self.age = age

    def __str__(self): #return when just object is called *CAN BE CALLED*
        return f"{self.name}({self.age})"
    
    def myFunc(self,hobby): #object's functions *CAN BE CALLED*
        print("Hello my name is " + self.name + ", I am " + str(self.age) + " and I like " + hobby)
    


obj1 = myClass("Todd",8)
obj2 = myClass("Jessica",10)
objList = [myClass("Ally",18),myClass("Brock",16),myClass("Donovan",19)] #objects can be defined in lists
hobbyList = ["Dominos","Rummikub","War"]

obj2.name += " Smith"

print()

for i in range(len(objList)): # for loops can be used to manipulate many objects
    objList[i].age += 10
    objList[i].myFunc(hobbyList[i])

print(obj1.age)
print(obj1)

print()