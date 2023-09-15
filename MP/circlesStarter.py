import turtle
import math
import colorsys
import random
"""

"""
# Set up the Turtle screen
# by assigning the screen vairable we can also
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(1024,1024) #make the drawing canvas 1024x1024 pixels
screen.title("Drawing Circles")

# Create a Turtle object
t = turtle.Turtle() #instantiate your Turtle
t.speed(0)  # Set the drawing speed (0) which is the "fastest"
t.color("purple") #this will be the active color of everything Turtle draws until it is changed
                  #more named colors for Turtle can be found here: 
                  #https://cs111.wellesley.edu/labs/lab02/colors


def drawOverlappingCircles(t, x, y, radius, forward_movement, angle_to_rotate, color):
    numberOfCircles = 360//angle_to_rotate
    return

def getRainbowColor(hue):
    color = colorsys.hsv_to_rgb(hue, 1, 1)
    return color

#main part of the program
#experiment with changing the values of the first five variables
radius = 80 #this is the radius of the circle in pixels
forward_movement = 2 #play with changing this value. What happens when it is the size of the radius?
                     #what happens when it is radius*2? What happens when it is bigger?
angle_to_rotate = 30 #the angle to rotate will determine how many circles we will draw. We want to
                     #draw enough circles to circumscribe 360 degrees, so the number of circles will be
                     #360/angle_to_rotate (notice we use the "//" operator the plain division operator "/"
                     #always returns float values)

x = 0 #the x coordinate of the center of the circle, try changing this values
y = 0 #the y coordinate of the center of the circle, try changing this value

##MAIN DRAWING CODE##
numberOfCircles = 360//angle_to_rotate
for i in range(numberOfCircles):
    t.penup() #what happens when you don't call the penup() and corresponding pendown() calls
              #try commenting them out to see
    t.goto(x,y - radius) #the Turtle "circle()" function always starts drawing at the
                         #bottom border of the circle
    t.pendown()
    t.pencolor("purple") #even though we set the global color to purple at the top
                         #here we have a chance to change the color
    t.circle(radius)
    t.forward(forward_movement) #move the turtle forward from its current orientation forward_movement pixels
    t.right(angle_to_rotate) #rotate the Turtle angle_to_rotate degrees
##MAIN DRAWING CODE##
    
screen.exitonclick()
