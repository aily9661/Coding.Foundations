import turtle
import random


class turtleShape(object):
    def __init__(self,x,y,xoff,yoff):
        #we give each turtleShape its own
        #turtle, stored in a property called
        #self.turtle, this enables us to click
        #on each shape (by clicking on its turtle)
        #and drag it around. Since a class can have
        #anything as a property, it is useful to have
        #each shape to have its own turtle to enable
        #this behavior
        self.turtle = turtle.Turtle()
        self.turtle.speed(0)
        self.turtle.color("red")
        self.turtle.shape("turtle")
        self.turtle.turtlesize(1)

        #Every shape has an x,y location and an offset
        #that centers the shape at x,y. We have four properties
        #that every turtleShape will have, self.x, self,y
        #self.xoffset and self.yoffset
        self.x = x
        self.y = y
        self.xoffset = xoff
        self.yoffset = yoff

      
        #This initializes the ondrag event handler with a function called "drag"
        #that is defined in turtleShape (see below) for details. Ther terminolgy here
        #is that we are "binding" the "self.drag()"
        self.turtle.ondrag(self.drag)
       
    def setStrokeColor(self,color):
        self.turtle.color(color)

    def draw(self):
        print("TURTLE SHAPE DRAW")
        #The parent draw function simply moves
        #the turtle to the x,y location with the default
        #behavior of subtracting the x and y offsets from the x and y
        #coordinates. It is up to the user the pass in the appropriate
        #offsets
        self.turtle.penup()
        self.turtle.goto(self.x-self.xoffset,self.y-self.yoffset)
        self.turtle.pendown()
     
    #STUDENTS WILL WRITE MOST OF THIS FUNCTION
    def drag(self, x, y):
        #set the x y coordinates of the mouse
        #to the self.x and self.y properties
        self.x = x
        self.y = y
        #turn off screen updates
        self.turtle.screen.tracer(0)
        #clear the current turtle graphics, experiment with commenting out for pen effect
        self.turtle.clear()
        #call self.draw() this is key, because self.draw() is the particular object
        #the correct child object draw function will be called
        self.draw()
        #update the screen
        self.turtle.screen.update()
        
        print("Dragged on Shape")

class turtleCircle(turtleShape):
    def __init__(self,x,y,xoff,yoff,radius):
        super().__init__(x,y,xoff,yoff)
        self.radius = radius

    def draw(self):
        print("TURTLE CIRCLE DRAW")
        super().draw()
        self.turtle.circle(self.radius)

class turtleSquare(turtleShape):
    def __init__(self,x,y,xoff,yoff,length):
        super().__init__(x,y,xoff,yoff)
        self.length = length

    def draw(self):
        print("TURTLE SQUARE DRAW")
        super().draw()
        for _ in range(4):
            self.turtle.forward(self.length)
            self.turtle.left(90)        

#The students will need to write this class
class turtlePolygon(turtleShape):
    def __init__(self,x,y,xoff,yoff,numSides,sideLength):
        super().__init__(x,y,xoff,yoff)
        self.numSides = numSides
        self.sideLength = sideLength
    
    def draw(self):
        super().draw()
        #rotate angle doesn't need to be a property
        #its a transient value we assign in the draw
        #method based on self.numSides
        rotate_angle = 360//self.numSides
        myVertexes = [] #we need this for extra credit one (which is hard)
        total_rotate_angle = 0 #we need this for extra credit one (which is hard)
        for _ in range(self.numSides):
            self.turtle.forward(self.sideLength)
            self.turtle.left(rotate_angle)
            myVertexes.append(self.turtle.pos())
            total_rotate_angle += rotate_angle
        #EXTRA CREDIT ONE
        #If myVertexes[0] is not equal to myVertexes[len(myVertexes) -1]
        #goto mVertexes[0][0]-self.sideLength,myVertexes[0][1] (starting x, y coordinates) 
        #to close the polygon. The x coordinate to goto is mVertexes[0][0]-self.sideLength
        #because the first vertex is where the turtle is after its first forward and left
        #call. They need to keep track of the total angle for polygons with numSide
        #that don't split evenly  into 360. The remaining rotation angle will be
        #360 - total_rotate_angle, if they don't do this the polygon will rotate when its
        #moved because it is not starting at 180 degrees pointing left
        if myVertexes[0] != myVertexes[len(myVertexes)-1]:
            self.turtle.goto(myVertexes[0][0]-self.sideLength,myVertexes[0][1])
            self.turtle.left(360 - total_rotate_angle)

#a list of colors:
myColors = ["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple"
            , "navy", "blue", "skyblue", "cyan", "turquoise", "lightgreen", "green", "darkgreen", 
            "chocolate", "brown", "gray", "white"]
# Set up the Turtle screen
# by specifying a background color
# and a width and height in pixels (1024px by 1024px here) 
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(1024,1024) #make the drawing canvas 1024x1024 pixels
screen.title("Drawing Basic Shapes Using Functions")
screen.mode("standard")

#Saving our "turtleCircle" and "turtleSquare" objects in two lists
#this allows us to use the main "screen" defined above to listen for
#keyboard input events. When we press "h" the turtles will be hidden
#when we press "s" the turtles will be shown. This allows to compose
#a drawing by moving shapes around with the turtles being shown (it is
# the turtles themselves that we have to click on interact with the turtleShape)
# and then we can hide the turtles to see what the drawing looks like without them
#look below at the final loop below the #HIDE/SHOW TURTLES comment

#a list called "myCircles" that stores a list of turtleCircles
#a list called "mySquares" that stores a list of turtleSquares
#a list called "allShapes" that stores all of our turtleShape child objects (see below)
myCircles = []
mySquares = []
allShapes = []
myPolygons = []

for i in range(10):
    x = random.randint(-412,412)
    y = random.randint(-412,412)
    radius = random.randint(10,100)
    numSides = random.randint(3,23)
    sideLength = random.randint(10,150)

    #STUDENTS WILL NEED TO WRITE INSTANTIATING THE
    #CLASSES IN THE LOOP AND STORING THEM IN A LIST
    #create some random turtleCircle objects
    #append them to myCircles
    myCircle = turtleCircle(x,y,0,radius,radius)
    myCircle.setStrokeColor(random.choice(myColors))
    myCircle.draw()
    myCircles.append(myCircle)

    #create some random turtleSquare objects
    #append them to mySquares
    mySquare = turtleSquare(x,y,radius/2,radius/2,radius)
    mySquare.setStrokeColor(random.choice(myColors))
    mySquare.draw()
    mySquares.append(mySquare)

    #create some random turtlePolygon objects
    #append them to myPolygons
    myPolygon = turtlePolygon(x,y,radius/2,radius/2,numSides,sideLength)
    myPolygon.setStrokeColor(random.choice(myColors))
    myPolygon.draw()
    myPolygons.append(myPolygon)

allShapes.append(myCircles)
allShapes.append(mySquares)
allShapes.append(myPolygons)

#STUDENTS WILL ALSO DEAL WITH THE
#hideallturtles() showallturtles() functions
#that run as event handlers when "h" and "s" are pressed

#Loop over allShapes which is a list of lists
#loop over each shape, hide the turtle
def hideallturtles():
    print("Goodbye: ",len(allShapes))
    for shapeTypes in allShapes:
        for shape in shapeTypes:
            shape.turtle.hideturtle()
            print(shape.turtle.isvisible())
    screen.update()

#Loop over allShapes which is a list of lists
#loop over each shape, show the turtle
def showallturtles():
    print("HELLO: ",len(allShapes))
    for shapeTypes in allShapes:
        for shape in shapeTypes:
            shape.turtle.showturtle()
            print(shape.turtle.isvisible())
    screen.update()

#listen for key strokes on the m,ain screen
#bind the "onkey" method with the hideallturtles
#and showallturtles functions, use "h" for hide
#and "s" for show
screen.listen()
screen.onkey(hideallturtles, "h")
screen.onkey(showallturtles, "s")
screen.mainloop()
#screen.exitonclick()