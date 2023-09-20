import turtle as t
import math

# Set up the Turtle screen
t.bgcolor("white")
t.title("Spirograph")

# Create a turtle for drawing
spirograph = t.Turtle()
spirograph.shape("turtle")
spirograph.color("blue")
spirograph.speed(50)

# Function to draw a Spirograph pattern
def draw_spirograph(R, r, d):
    # R - radius of the large circle
    # r - radius of the small circle
    # d - distance from the pen to the center of the small circle
    spirograph.penup()
    spirograph.goto(R - r + d, 0)
    spirograph.pendown()
    angle = 0
    while angle < 1120:
        x = (R - r) * math.cos(math.radians(angle)) + d * math.cos(math.radians((R - r) / r * angle))
        y = (R - r) * math.sin(math.radians(angle)) - d * math.sin(math.radians((R - r) / r * angle))
        spirograph.goto(x, y)
        if angle % 2 == 0:
            spirograph.color("red")
        if angle % 3 == 0:
            spirograph.color("green")
        angle += 1

# Set parameters for the Spirograph
R = 100  # Radius of the large circle
r = 30   # Radius of the small circle
d = 70   # Distance from pen to small circle center

# Draw the Spirograph
draw_spirograph(R, r, d)

# Hide the turtle
spirograph.hideturtle()

# Close the window when clicked
t.exitonclick()
