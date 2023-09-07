myList1 = [1,3,5,7,9,2,4,6,8,10]
myList2 = []

for i in range(len(myList1)):
    if (myList1[i] % 2) == 0:
        myList2.append(myList1[i])

print(myList2)