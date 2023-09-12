import random

myList = list()

for i in range(100):
    myList += ["placeholder"]
    myList[i] = random.random()

print(myList)
print(len(myList))