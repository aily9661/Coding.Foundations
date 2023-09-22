import turtle
import math
import colorsys
import random

# Set up the Turtle screen
# by 
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(1024,1024) #make the drawing canvas 1024x1024 pixels
screen.title("Drawing Basic Shapes Using Functions")

# Create a Turtle object
t = turtle.Turtle() #instantiate your Turtle
t.speed(0)  # Set the drawing speed (0) which is the "fastest"
t.color("purple") #this will be the active color until/if it is changed
t.turtlesize(0.5) #this will make it a little bigger


def drawPolygon(t,x,y,numSides,sideLength, color="yellow"):
    rotationAngle = 360//numSides
    t.penup()
    t.goto(x-(sideLength/2),  y-(sideLength/2))
    t.pendown()

    for i in range(numSides):
        t.forward(sideLength)
        t.left(rotationAngle)

drawPolygon(t,0,0,5,100)
screen.exitonclick()

#I have a new python file under Modules on canvas for today it is marked:
#turtleDrawShapes.py (for PC04)

#This is what you should start with for recitations. It would be good
#to review the code with them so you can get an idea of how it works
#with them and read some of the comments which explain a lot.

#First just be sure and run the code and have them run it as well.
#It will call each of the drawing functions, but then also draws a scene
#at the end that is defined in a function "drawSunSettingBehindMountains"

#I'd really like them to try to use these functions rather than jump
#straight to the internet for parameteric equations or insane lines
#of turtle code that draw reall complex things. I think having them figure out
#how to place things like in the mountains drawing would be a good thing.

#Let me know if you have any questions. I'll be around tomorrow if 
#something comes up.

#Take care, --Brad