import random, time

#constants
keepPlaying = True
correctGuesses = 0
wrongGuesses = 0

#game welcome
print("Welcome to the dice stadium! Ready to play?")
userCom = input("Y/N ")

#response based on user initial ready confirtmation
if userCom == "N" or userCom == "n": print("Too bad!")
elif userCom == "Y" or userCom == "y": print("Sweet, let's get into it")
else: print("Well that's not a correct input... but let's play anyway")

time.sleep(1)
print("Here's the game: Guess whether the dice roll will be high or low. If you guess correctly you win!")
time.sleep(1)

#loop ends when user chooses to stop playing
while keepPlaying == True:
    diceRoll = random.randint(1,6)
    userGuess = input("Do you think the dice roll will be high or low? H/L ")
    print("Rolling...")
    time.sleep(1)
    if diceRoll > 3 and userGuess == "H": 
        print("Correct! Dice roll was ", diceRoll)
        correctGuesses+=1
    elif diceRoll <= 3 and userGuess == "L": 
        print("Correct! Dice roll was ", diceRoll)
        correctGuesses+=1
    elif diceRoll <= 3 and userGuess == "H":
        print("Wrong! Dice roll was ", diceRoll)
        wrongGuesses += 1
    elif diceRoll > 3 and userGuess == "L":
        print("Wrong! Dice roll was ", diceRoll)
        wrongGuesses += 1
    time.sleep(1)
    print("Correct guesses: ",correctGuesses)
    time.sleep(1)
    print("Wrong guesses: ", wrongGuesses)
    time.sleep(1)
    keepPlaying2 = input("Wanna play again? Y/N ")
    if keepPlaying2 == "N" or keepPlaying2 == "n": 
        print("Goodbye!")
        keepPlaying = False
    elif keepPlaying2 == "Y" or keepPlaying2 == "y": 
        print("Restarting game...")
        time.sleep(1)
    else: print("Incorrect input! Try again."), time.sleep(1)

