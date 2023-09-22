import turtle

def draw_polygon(n, x, y, side_length, color):
    # Create a Turtle object
    polygon_turtle = turtle.Turtle()

    # Set the turtle's starting position
    polygon_turtle.penup()
    polygon_turtle.goto(x, y)
    polygon_turtle.pendown()

    # Set the fill color
    polygon_turtle.fillcolor(color)
    polygon_turtle.begin_fill()

    # Draw the polygon
    for _ in range(n):
        polygon_turtle.forward(side_length)
        polygon_turtle.right(360 / n)

    # Fill the polygon
    polygon_turtle.end_fill()

    # Close the turtle graphics window on click
    turtle.exitonclick()

# Example usage:
n = 6  # Number of sides
x = 0  # X-coordinate of the starting point
y = 0  # Y-coordinate of the starting point
side_length = 100  # Length of each side
color = "blue"  # Fill color

draw_polygon(n, x, y, side_length, color)
