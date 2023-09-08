#import libraries
import random, time

#create lists
materials = ['brick', 'sand', 'glass']
location = ["In a dense forest", "By the seashore", "In your mom's house"]
lights = ["candles","torches","flashlights"]
lightPrompt = ["Using","Illuminated by"]
inhabitants = ["cockraches","crows","kings"]

trueFalse = True
counter = 0

#make while loop, use random.choice(x) to randomly select strings from lists
while True:
    #print("A house of",random.choice(materials))
    #print("   ",random.choice(location))
    #print("      ",random.choice(lights))
    #print("         Inhabited by",random.choice(inhabitants))
    for letter in "        INHABITED BY " + random.choice(inhabitants):
            print(letter, end="", flush=True)
            time.sleep(0.05)
    print()
    for letter in "     " + random.choice(location):
            print(letter, end="", flush=True)
            time.sleep(0.05)
    print("\n")
    time.sleep(1)


#extra credit 1: use random.random() and an if statement to select between two light source phrases 50% of the time
            #or you can figure out how to use random.choice again!


#extra credit 2: learn how to use print statements to print letter by letter rather than an entire statement