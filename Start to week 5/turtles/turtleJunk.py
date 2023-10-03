import turtle
import math

# Set up the Turtle screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Parametric Butterfly")

# Create a Turtle object
turts = []
turts2 = []

# Define colors for the wings
colors = ["red", "blue", "green", "purple"]

x,y,y2,x2 = 0,-250,-250,0
for i in range(100):
    turts.append(turtle.Turtle())
    turts2.append(turtle.Turtle())

    turts[i].goto(x,y)
    turts2[i].goto(x2,y2)

    turts[i].penup()
    turts2[i].penup()

    turts[i].setheading((i*10)+90)
    turts2[i].setheading((i*-10)+90)

    turts[i].pendown()
    turts2[i].pendown()

    turts[i].forward(100/(i+1))
    turts2[i].forward(100/(i+1))

    turts[i].hideturtle()
    turts2[i].hideturtle()

    x = turts[i].xcor()
    y = turts[i].ycor()

    x2= turts2[i].xcor()
    y2 = turts2[i].ycor()
