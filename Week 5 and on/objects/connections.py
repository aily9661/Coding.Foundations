import random

items1 = ["item1","item2","item3","item4"]
items2 = ["item1","item2","item3","item4"]
items3 = ["item1","item2","item3","item4"]
items4 = ["item1","item2","item3","item4"]
game1 = [items1,items2,items3,items4]

alpha = ["a","b","c","d"]

# calculate each group letter count
count1, count2, count3, count4 = 3,3,3,3

for item in items1:
    for char in item: 
        count1+=1

for item in items2:
    for char in item: 
        count2+=1

for item in items3:
    for char in item: 
        count3+=1

for item in items4:
    for char in item: 
        count4+=1

print(count1, count2, count3, count4)

for i in range(4):
    for x in range(4):
        print("-", end="", flush=True)
        if x == 1 and i == 0:
            for item in items1:
                print(item, end=" ", flush=True)
            x -= count1
                
    print("")