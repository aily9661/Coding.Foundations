import turtle
import math
import colorsys
import random
import numpy as np
import simpleaudio as sa

#a list of colors:
myColors = ["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple"
            , "navy", "blue", "skyblue", "cyan", "turquoise", "lightgreen", "green", "darkgreen", 
            "chocolate", "brown", "gray", "white"]
# Set up the Turtle screen
# by specifying a background color
# and a width and height in pixels (1024px by 1024px here) 
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(1024,1024) #make the drawing canvas 1024x1024 pixels
screen.title("Drawing Basic Shapes Using Functions")

# Create a Turtle object
t = turtle.Turtle() #instantiate your Turtle
t.speed(0)  # Set the drawing speed (0) which is the "fastest"
t.color("red") #this will be the active color until/if it is changed

t.shape("turtle") #this will make our drawing pointer look like a turtle
t.turtlesize(1) #this will make it a little bigger

##HERE WE WILL DEFINE FUNCTIONS THAT DRAW SHAPES AT A GIVEN LOCATION##
def getRainbowColor(hue):
    color = colorsys.hsv_to_rgb(hue, 1, 1)
    return color

def drawACircle(t, x, y, radius, strokeColor="yellow", fillColor="NONE"):
    t.penup()
    t.goto(x,y - radius) #to center circle at x,y we need to offset the y coordinate by
    t.pendown()          #-radius , tutrle draw circles starting at the bottom border
    #here we use an if statement and have a branch in the code
    #the draw the circle with both an outline and fill color, or just an outline color
    if fillColor != "NONE":
        t.color(strokeColor,fillColor)
        t.begin_fill()
        t.circle(radius)
        t.end_fill()
    else:
        t.color(strokeColor)
        t.circle(radius)

def getNewNote(baseFreq,nSemitones):
    return baseFreq*2.0**(nSemitones/12)

def play_tone(x, y, radius):
   
    base_frequency = 220 # Adjust as needed
   
    semitoneList = [0,2,4,7,9,12,16,19] #major pentatonic scale
    #semitoneList = [0,3,5,7,10,12,15,17] #minor pentatonic scale
   
    frequency = getNewNote(base_frequency,random.choice(semitoneList))

    # Calculate the duration based on circle radius
    duration = radius * 0.005  # Adjust the scale as needed 0.005 is lowest

    # Generate a sine wave with fade-in and fade-out
    sample_rate = 44100  # Sample rate in Hz
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    fade_duration = 0.05  # Adjust the fade-in/fade-out duration as needed
    fade_samples = int(fade_duration * sample_rate)

    # Create a fade-in and fade-out envelope
    fade_in = np.linspace(0, 1, fade_samples)
    fade_out = np.linspace(1, 0, fade_samples)

    # Generate the sine wave
    wave = 0.5 * np.sin(2 * np.pi * frequency * t)

    # Apply fade-in and fade-out
    wave[:fade_samples] *= fade_in
    wave[-fade_samples:] *= fade_out

    # Play the sine wave
    play_obj = sa.play_buffer((wave * 32767).astype(np.int16), 1, 2, sample_rate)
    play_obj.wait_done()


##HERE IS WHERE THE DRAWING WILL HAPPEN, WE WILL CALL THE FUNCTIONS
##DEFINED ABOVE IN VARIOUS WAYS


#if you want to see your turtle
#comment out the line below
t.hideturtle()

#experiment with uncommenting the line below
#alonh with uncommenting the "screen.update()" call
#below. What happens? What happens if you indent the
# "screen.update()" call all the way to the left?

#draw some shapes using our functions
screen.tracer(0)
radius = 10 #start the radius at 10
modFreq = 10 #change the radius and modFreq after 10 initial circles are drawn
for i in range(400): #draw 400 circles and play 400 notes
    #draw a circle
    x = 0
    y = 0
    #use a while loop to make sure we don't
    #have x or y assigned to zero by random.randint
    #if either x or y happens to be assigned zero the
    #loop will make it try again until it isn't equal to zero
    while x == 0 and y == 0:
        x = random.randint(-300,300)
        y = random.randint(-400,400)

    #this will change the radius and
    #the frequency at which the radius is changed (modFreq)
    #this gives the "music" more rhythmic changes
    #playing with the ranges of the random.randint calls
    #will change the rhythym because the bigger the radius
    #the longer the duration and the smaller the modFreq
    #the more often both things will be changed
    if i % modFreq == 0:
        radius = random.randint(10,100)
        modFreq = random.randint(3,9)
    #will draw a circle with both a stroke and fill color
    drawACircle(t,x,y,radius,random.choice(myColors), random.choice(myColors))
    screen.update()
    play_tone(x,y,radius)
#This keeps the turtle screen active until it is clicked on
#to exit
screen.exitonclick()
