import random
class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  def __init__(self, brand, model, numWheels):
    super().__init__(brand,model)
    self.numWheels = numWheels

class Boat(Vehicle):
  def __init__(self, brand, model, numWheels):
    super().__init__(brand,model)
    self.numWheels = numWheels
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def __init__(self, brand, model, numWheels):
    super().__init__(brand,model)
    self.numWheels = numWheels
  def move(self):
    print("Fly!")

myVehiculars = []
for i in  range(random.randint(10,30)):
    car1 = Car("Ford", "Mustang", 4) #Create a Car object
    myVehiculars.append(car1)
    boat1 = Boat("Ibiza", "Touring 20", 0) #Create a Boat object
    myVehiculars.append(boat1)
    plane1 = Plane("Boeing", "747", 3) #Create a Plane object
    myVehiculars.append(plane1)

wheelCount = 0
count = 0

for x in (myVehiculars):
  print("I am a",x.brand, x.model, "and I")
  wheelCount += x.numWheels
  count += 1
  x.move()

print("Our fleet of", count, "vehicles has",wheelCount,"wheels.")