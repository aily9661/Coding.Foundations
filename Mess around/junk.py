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
t.speed(0) # Set the drawing speed (0) which is the "fastest"
t.color("purple") #this will be the active color until/if it is changed

##HERE WE WILL DEFINE FUNCTIONS THAT DRAW SHAPES AT A GIVEN LOCATION##
def drawACircle(t,x,y,radius,color):
    t.penup()
    t.color(color)
    t.goto(x,y)
    t.pendown()
    t.circle(radius)

##HERE IS WHERE THE DRAWING WILL HAPPEN, WE WILL CALL THE FUNCTIONS
radius = 10
colors = ["yellow","cyan","red","orange","green","purple"]

for i in range(1000):
    x = random.randint(-300,300)
    y = random.randint(-300,300)
    color = random.choice(colors)
    drawACircle(t,x,y,radius,color)

#This keeps the turtle screen active until it is clicked on
#to exit
screen.exitonclick()
