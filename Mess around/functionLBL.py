import time

myList = ["one","two","three","four","five","six","seven","eight","nine","ten"]

def printByLetter(myString):
    for char in myString:
        print(char.capitalize(),end=" ",flush=True)
        time.sleep(0.1)

for string in myList:
    printByLetter(string)
    print()
