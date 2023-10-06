import turtle as t

# Set up the screen
screen = t.Screen()
screen.title("Flappy Bird Clone")
screen.bgcolor("lightblue")
screen.setup(width=600, height=400)

# Create the bird
bird = t.Turtle()
bird.shape("triangle")
bird.color("yellow")
bird.penup()
bird.goto(-200, 0)
bird.speed(0)
bird.dx = 2
bird.dy = 0

# Create gravity
gravity = -0.1

# Create pipes
pipe_width = 20
pipe_height = 150
pipe_color = "green"

pipe_top = t.Turtle()
pipe_top.shape("square")
pipe_top.color(pipe_color)
pipe_top.shapesize(stretch_wid=pipe_height/20, stretch_len=pipe_width/20)
pipe_top.penup()
pipe_top.goto(300, 100)

pipe_bottom = t.Turtle()
pipe_bottom.shape("square")
pipe_bottom.color(pipe_color)
pipe_bottom.shapesize(stretch_wid=pipe_height/20, stretch_len=pipe_width/20)
pipe_bottom.penup()
pipe_bottom.goto(300, -100)

# Create score
score = 0
score_display = t.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 170)
score_display.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))

# Functions
def jump():
    bird.dy = 3

def is_collision(obj1, obj2):
    x_distance = abs(obj1.xcor() - obj2.xcor())
    y_distance = abs(obj1.ycor() - obj2.ycor())
    if x_distance < (pipe_width / 2) and y_distance < (pipe_height / 2):
        return True
    return False

# Keyboard bindings
screen.listen()
screen.onkeypress(jump, "space")

# Main game loop
while True:
    bird.dy += gravity
    bird.sety(bird.ycor() + bird.dy)

    pipe_top.setx(pipe_top.xcor() - bird.dx)
    pipe_bottom.setx(pipe_bottom.xcor() - bird.dx)

    if pipe_top.xcor() < -300:
        pipe_top.setx(300)
        pipe_top.sety(100)
        pipe_bottom.setx(300)
        pipe_bottom.sety(-100)

    if bird.ycor() > 190:
        bird.sety(190)
        bird.dy = 0

    if is_collision(bird, pipe_top) or is_collision(bird, pipe_bottom) or bird.ycor() < -190:
        bird.goto(-200, 0)
        bird.dy = 0
        score = 0

    if pipe_top.xcor() == -200:
        score += 1
        score_display.clear()
        score_display.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))

    screen.update()
