import turtle
import math
import colorsys
import random

# Set up the Turtle screen
# by 
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(1024,1024) #make the drawing canvas 1024x1024 pixels
screen.title("Drawing Circles")

# Create a Turtle object
t = turtle.Turtle() #instantiate your Turtle
t.speed(0)  # Set the drawing speed (0) which is the "fastest"
t.color("purple") #this will be the active color of everything Turtle draw until it is changed


def drawOverlappingCircles(t, x, y, radius, forward_movement, angle_to_rotate,color):
    numberOfCircles = 360//angle_to_rotate
    for i in range(numberOfCircles):
        t.penup()
        t.goto(x,y - radius)
        t.pendown()
        t.pencolor(color)
        #t.pencolor(getRainbowColor(i/numberOfCircles)) #they can use this function to draw each circle
        #with a different color of the rainbow
        t.circle(radius)
        t.forward(forward_movement)
        t.right(angle_to_rotate)
    return

def getRainbowColor(hue):
    color = colorsys.hsv_to_rgb(hue, 1, 1)
    return color

radius = 80
forward_movement = 10
angle_to_rotate = 10
colors = ["blue","red","yellow","aquamarine","orange"]
screen.tracer(0)
for i in range(30):
    drawOverlappingCircles(t,random.randint(-512,512),random.randint(-512,512),random.randint(10,80),
                           forward_movement,angle_to_rotate,random.choice(colors))
    screen.update()
    
screen.exitonclick()
