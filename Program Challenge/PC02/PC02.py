import random, time #import user libraries 

materials = ['brick','sand','glass']
#create 3 more lists with one containing locations, another lightsources, and lastly one with inhabitants
#EXTRA CREDIT 1: create another list with light source prompts

while True: #create an infinite while loop
    print("A house of",random.choice(materials))#use random.choice to randomly print an item from your materials list: 
    #repeat 3 other times with other lists
    #EXTRA CREDIT 1: use lightsource prompts list before printing the lightsources list
    #EXTRA CREDIT 2: Learn yourself from external resources how to print letter by letter (flush, as in the letters print directly next to eachther) rather than line by line
    #create a new line to separate poems from eachother
    time.sleep(1) #use sleep library to pause for one second
