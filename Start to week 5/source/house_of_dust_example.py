import random

matPromptList = ["A house of", "Materialized via", "Structured with"]
lightPromptList = ["Illuminated by", "Using", "Ignited from", "Lit with"]
inhabitPromptList = ["Inhabited by", "Filled with", "Home to", "Welcoming all", "A family of"]

materialList = ["bricks", "sand", "glass", "toilet paper", "flesh"]
locationList = ["Deep in the heart of Chicago", "Lost in a dense forest", "Hidden within a cave", "By the seaside", "In the sky"]
lightsList = ["torchlight", "ceiling lights", "candles", "fireplace"]
inhabitsList = ["cockroaches", "pigs", "hermit crabs", "chickens", "crows"]

lightEmotionsList = ["angry", "sad", "happy", "mundane"]

greeting = "\nHello, welcome to the random poem generator!"
print(greeting)
print("\n\n")

repeatCount = int(input("How many times should we randomly generate the poem? "))

for i in range(repeatCount):
    materialPrompt = random.randint(0,len(matPromptList)-1)
    lightPrompt = random.randint(0,len(lightPromptList)-1)
    inhabitPrompt = random.randint(0,len(inhabitPromptList)-1)

    material = random.randint(0,len(materialList)-1)
    location = random.randint(0,len(locationList)-1)
    lights = random.randint(0,len(lightsList)-1)
    inhabit = random.randint(0,len(inhabitsList)-1)

    lightEmotion = random.randint(0,len(lightEmotionsList)-1)

    print("\n")
    print(matPromptList[materialPrompt], materialList[material])
    print("     ",locationList[location])
    print("         ",lightPromptList[lightPrompt],lightEmotionsList[lightEmotion],lightsList[lights])
    print("            ",inhabitPromptList[inhabitPrompt],inhabitsList[inhabit])
    print("\n")