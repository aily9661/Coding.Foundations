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

t.shape("turtle") #this will make our drawing pointer look like a turtle
t.turtlesize(1) #this will make it a little bigger

##HERE WE WILL DEFINE FUNCTIONS THAT DRAW SHAPES AT A GIVEN LOCATION##
def drawASquare(t, x, y, length, color="yellow"):
    t.penup()
    t.goto(x-length/2,y-length/2)
    t.pendown()
    t.pencolor(color)
    for i in range(4):
        t.forward(length)
        t.left(90)

def drawARect(t, x, y, width, height, color="yellow"):
    t.penup()
    t.goto(x-width/2,y-height/2)
    t.pendown()
    t.pencolor(color)
    for i in range(4):
        if i % 2 == 0:
            t.forward(width)
        else:
            t.forward(height)
        t.left(90)

def drawACircle(t, x, y, radius, strokeColor="yellow", fillColor="NONE"):
    t.penup()
    t.goto(x,y - radius)
    t.pendown()
    if fillColor != "NONE":
        t.color(strokeColor,fillColor)
        t.begin_fill()
        t.circle(radius)
        t.end_fill()
    else:
        t.color(strokeColor)
        t.circle(radius)


##HERE IS WHERE THE DRAWING WILL HAPPEN, WE WILL CALL THE FUNCTIONS
##DEFINED ABOVE IN VARIOUS WAYS
myColors = ["red","blue","purple","yellow","green","orange","aquamarine"]

for i in range(100):
    x = random.randint(-300,300)
    y = random.randint(-400,400)
    radius = random.randint(10,250)
    #outline the circle and fill it with a random color
    drawACircle(t,x,y,radius,random.choice(myColors), random.choice(myColors))
    #outline the circle with "black" (so the outline won't showup on a black backround)
    #and fill with a random color
    x = random.randint(-300,300)
    y = random.randint(-400,400)
    radius = random.randint(10,250)
    #drawACircle(t,x,y,radius,"black", random.choice(myColors))
    #outline circle with a random color and fill with "black" so it won't be colored because of the
    #black background
    x = random.randint(-300,300)
    y = random.randint(-400,400)
    radius = random.randint(10,250)
    #drawACircle(t,x,y,radius,random.choice(myColors),"NONE")


#This keeps the turtle screen active until it is clicked on
#to exit
screen.exitonclick()
