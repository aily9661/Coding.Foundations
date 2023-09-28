import turtle
import math

# Set up the Turtle screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Parametric Butterfly")

# Create a Turtle object
butterfly = turtle.Turtle()
butterfly.shape("turtle")
butterfly.speed(0)  # Set the drawing speed

# Define colors for the wings
wing_colors = ["red", "blue", "green", "purple"]

# Function to calculate the x and y coordinates using parametric equations
def butterfly_curve(t):
    x = math.sin(t) * (math.exp(math.cos(t)) - 2 * math.cos(4 * t) - math.sin(t/12)**5)
    y = math.cos(t) * (math.exp(math.cos(t)) - 2 * math.cos(4 * t) - math.sin(t/12)**5)
    return x * 100, y * 100

# Draw the butterfly curve with colorful wings
butterfly.penup()
butterfly.goto(butterfly_curve(0))
butterfly.pendown()

for t in range(0, 628, 1):  # Iterate from 0 to 2*pi
    x, y = butterfly_curve(t / 100.0)
    butterfly.goto(x, y)
    
    # Set the fill color for the wings based on the list of colors
    color_index = t // 157  # Adjust this value to change how often colors change
    butterfly.fillcolor(wing_colors[color_index % len(wing_colors)])
    butterfly.begin_fill()
    butterfly.circle(1)  # Draw a small circle at each point to fill the wings
    butterfly.end_fill()

# Hide the Turtle and display the result
butterfly.hideturtle()
screen.mainloop()
