import random
import time

materials = ["WOOD","SAND","RUSTY NAILS","LEAVES","OLD FISHING NETS",
             "DISCARDED CARDBOARD BOXES","PUTRID SLIME","PLASTIC SHOPING BAGS",
             "CARDS","UNCONVENTIONAL CONSTRUCTION"]
locations = ["UNDERWATER","INSIDE A CAVE","ABOVE THE CLOUDS",
             "VERY FAR AWAY FROM HERE","IN THE DEPTHS OF HELL",
             "BY A BEAUTIFUL BEACH","BESIDE A TOXIC RIVER","OUTSIDE ANOTHER BURNING HOUSE",
             "INSIDE A CONCH SHELL","IN A BEAUTIFUL GREEN MEADOW"]
lightSources = ["SUNLIGHT","THE DARKNESS INSIDE MY SOUL","THE LIGHT INSIDE MY SOUL",
                "A CAMPFIRE","ELECTRIC LIGHT","SICK LED DISCO LIGHTS","A STROBE LIGHT",
                "THE GLOWING EMBERS OF A DYING FIRE","A FOREST FIRE","MOONLIGHT"]
inhabitants = ["ALL MY FRIEND AND ENEMIES","TOO MANY PEOPLE TO COUNT","STRANGE CREATURES OF EVERY TYPE",
               "A COLLECTION OF IMPRESSIVE LIZRDS","BIG BIRD AND COOKIE MONSTER","ROBOTS DOING NOTHING AT ALL",
               "TOO MANY DAMN SPIDERS!", "A CATERPILLAR TURNING INTO A BUTTERFLY","PEOPLE ARGUING",
               "PEOPLE AGREEING WITH EACH OTHER"]

while True:
    print("\n")
    for letter in "A HOUSE OF " + random.choice(materials):
        print(letter, end="", flush=True)
        time.sleep(0.05)
    print()
    for letter in "    " + random.choice(locations):
        print(letter, end="", flush=True)
        time.sleep(0.05)
    print()
    if random.random() > 0.5:
        for letter in "      USING " + random.choice(lightSources):
            print(letter, end="", flush=True)
            time.sleep(0.05)
        print()
    else:
        for letter in "      ILLUMINATED BY " + random.choice(lightSources):
            print(letter, end="", flush=True)
            time.sleep(0.05)
        print()
    for letter in "        INHABITED BY " + random.choice(inhabitants):
            print(letter, end="", flush=True)
            time.sleep(0.05)
    print()
