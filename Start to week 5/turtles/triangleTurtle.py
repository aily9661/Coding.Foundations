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

#equilateral triangle
def drawATriangle(iso=False,right=False):
    for i in range(3):
        t.forward(50)
        t.left(360/3)
    if iso == True:
        t.forward(50)
        for i in range(3):
            t.forward(50)
            t.left(360/3)


def drawARightTriangle(fill=False,drawRight=True):
    t.penup()
    #define triangle variables
    base = random.randint(0,200)
    height = random.randint(0,200)
    hypotenuse = math.sqrt(height*height + base*base)
    x = random.randint(-250,250)    
    y = random.randint(-250,250)
    colors = ["red","orange","grey","green","yellow"]
    color = random.choice(colors)
    t.goto(x,y)
    t.setheading(random.randint(0,360))
    t.pendown()
    t.pencolor(color)
    t.color(color)

    #draw triangle
    if drawRight:
        if fill==True: t.begin_fill()
        t.forward(base)
        t.left(180. - math.asin(height/hypotenuse)*(180./math.pi))
        t.forward(hypotenuse)
        t.left(180. - math.asin(base/hypotenuse)*(180./math.pi))
        t.forward(height)
        if fill==True: t.end_fill()
        if fill==True: t.begin_fill()
        t.backward(base)
        t.right(180. - math.asin(height/hypotenuse)*(180./math.pi))
        t.backward(hypotenuse)
        t.right(180. - math.asin(base/hypotenuse)*(180./math.pi))
        t.backward(height)
        if fill==True: t.end_fill()

#drawATriangle()
#drawATriangle(iso=True)
#drawATriangle(right=True)
for i in range(200):
    #if i>= 100: drawARightTriangle()
    drawARightTriangle(fill=True)
#This keeps the turtle screen active until it is clicked on
t.hideturtle()
screen.exitonclick()
