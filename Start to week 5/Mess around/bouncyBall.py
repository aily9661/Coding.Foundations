import turtle
import random
import time

# Set up the Turtle screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Rainbow Bouncy Balls Room")

# Create a list to store bouncing balls
t = turtle.Turtle()
t.hideturtle()
t.speed(0)
colors = ["red","orange","grey","green","yellow"]
# Function to create a new bouncing ball
def drawBall(y,color = random.choice(colors)):
    screen.tracer(0)
    while True:
        t.penup()  
        y+=10
        t.goto(0,y)
        t.pendown()
        t.pencolor(color)
        t.color(color)
        t.dot(25)
        screen.update()
        t.clear()
        time.sleep(0.1)
        

# Close the window when clicked (optional)
y=0
drawBall(y)
screen.exitonclick()
