list2 = [1,3,5,7,9,2,4,6,8,10]
list1 = []

for items in list2: 
    if items % 2 == 0:
        list1.append(items)

print(list1)