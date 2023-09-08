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
    print("A HOUSE OF " + random.choice(materials))
    print("    " + random.choice(locations))
    if random.random() > 0.5:
        print("      USING " + random.choice(lightSources))
    else:
        print("      ILLUMINATED BY " + random.choice(lightSources))
    print("        INHABITED BY " + random.choice(inhabitants))
    print()
    time.sleep(3.0)
