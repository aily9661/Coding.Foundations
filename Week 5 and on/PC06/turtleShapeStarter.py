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
        #that is defined in turtleShape (see below) for details. The terminolgy here
        #is that we are "binding" the "self.drag()" function to the ondrag() method
        #of turtle. The drag function needs to have self and x,y (the cordinates of the mouse) 
        # as arguments (see below)
        self.turtle.ondrag(self.drag)
    
    #an example of additional method that sets the stroke or outline color of the shape
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
     
    #PART #1 of PC06, write the drag() event handler function
    def drag(self, x, y):
        #the drag function (which is an event handler that listens for mouse events)
        #needs to set the incoming x,y coordinates of the mouse to the self.x and self.y
        #properties of the object. Since we instantiate child classes (circles, squares, polygons)
        #"self" is one of these particular objects, so when we call "draw(self)" it calls the
        #appropriate draw routine (polymorphism) of one of three child classes: turtleCircle
        #turtleSquare, and turtlePolygon, which you will adpat from your original "drawPolygon()"
        #function. We then need to turn off screen updates, clear the turtle graphics, call
        #draw(self), and then update the screen. This will ensure that we can drag around
        #the shape as a single drawn instance because we only actually draw to the screen
        #when we call self.turtle.screen.update()
        
        
        #here is the pseudocode for this function, each line corresponds to a line of code
        #hint, when I say something is a property, that means it accessed through "self"

        #PSEUDOCODE BEGIN

        #<property x of turtleShape is assigned to the passed-in variable x>
        #<property y of turtleShape is assigned to the passed-in variable y>
        #<turn off screen updates by calling "screen.tracer(0)" on the turtle property>
        #<clear the current turtle graphics by calling "clear()" on the turtle property>
        #<call self.draw()>
        #<update the screen by calling "screen.update()" on the turtle property>

        #PSEUDOCODE END
        print("Dragged on Shape")

#a child class of turtleShape that draws a circle
class turtleCircle(turtleShape):
    def __init__(self,x,y,xoff,yoff,radius):
        super().__init__(x,y,xoff,yoff)
        self.radius = radius

    def draw(self):
        print("TURTLE CIRCLE DRAW")
        super().draw()
        self.turtle.circle(self.radius)

#a child class of turtleShape that draws a square
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

#PART #2 PC06: Write a class called "turtlePolygon" that is a child class of turtleShape.
#you will follow the same logic as in the turtleCircle and turtleSquare examples. In both
#cases the draw() function of the child class does the shape-specific drawing, and the parent
#class, turtleShape, handles where the shape is drawn, and provides a setStrokeColor() method
#and a drag() event handler function. You need to adpat the "drawPolygon()" function from your previous 
#turtle drawing functions into a child class. The "turtlePolygon" function will have two unique properties:
#self.numSides and self.sideLength

#BEGIN CLASS DEINITION

        #EXTRA CREDIT ONE: CLOSE THE POLYGON WITH numSides THAT DOES NOT DIVIDE EVENLY INTO 360
        #EXTRA CREDIT ONE, consists of three lines of code. An if statement that
        #If myVertexes[0] is not equal to myVertexes[len(myVertexes) -1]
        #goto mVertexes[0][0]-self.sideLength,myVertexes[0][1] (starting x, y coordinates) 
        #to close the polygon. The x coordinate to goto is mVertexes[0][0]-self.sideLength
        #because the first vertex is where the turtle is after its first forward and left
        #call. You need to keep track of the total angle for polygons with numSides
        #that doesn't divide evenly into 360. The remaining rotation angle will be
        #360 - total_rotate_angle, if you don't do this the polygon will rotate when its
        #moved because it is not starting at 180 degrees pointing left
        
#main code, some global variables
#a main screen, four empty list definitions
#and then a mian for loop

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

#Saving our "turtleCircle," "turtleSquare," and "turtlePolygon" objects 
#in three lists allows us to hide and show the turtle cursor by using 
#the main "screen" defined above to listen for keyboard input events. 
# 
#When we press "h" the turtles will be hidden
#When we press "s" the turtles will be shown. 
# 
#This allows us to compose a drawing by moving shapes around with the turtles 
# being shown (it is the turtles themselves that we have to click on interact with 
# the turtleShape) and then we can hide the turtles to see what the drawing looks 
#like without them look below at the final loop pseudocode below the 
#HIDE/SHOW TURTLES comment

#a list called "myCircles" that stores a list of turtleCircles
myCircles = []
#a list called "mySquares" that stores a list of turtleSquares
mySquares = []
#a list called "myPolygons" that stores a list of turtlePolygons
myPolygons = []
#a list called "allShapes" that stores all of our turtleShape child objects (see below)
allShapes = []


for i in range(10):
    #a random x,y coordinate for our different turtleShapes
    #we will draw a turtleCircle and turtleSquare and a turtlePolygon
    #at the same x,y coordinate
    x = random.randint(-412,412)
    y = random.randint(-412,412)
    #we'll use the value of radius for both our turtleCircles and our length for
    #our turtleSquares
    radius = random.randint(10,100)
    #we need to generate numSides and sideLength values for our ploygon
    numSides = random.randint(3,23)
    sideLength = random.randint(10,150)

    #PART #3 PC06: Instantiate a turtleCircle, turtleSquare, and turtlePolygon
    #for each run through the for loop (set to range(10)). Set a random stroke
    #color using the setStrokeColor() method of turtleShape. Call the "draw()" function.
    #Append the instantiated child object to the appropriate list. Here is an example
    #for the turtleCircle child class. Repeat for turtleSquare and turtlePolygon: 
    
    myCircle = turtleCircle(x,y,0,radius,radius)
    myCircle.setStrokeColor(random.choice(myColors))
    myCircle.draw()
    myCircles.append(myCircle)

#append our lists of different child turtleShape objects
#to allShapes, which will be a list of a list of objects   
allShapes.append(myCircles)
allShapes.append(mySquares)
allShapes.append(myPolygons)


#HIDE/SHOW TURTLES
#PART #4 PC06: Write two event handler functions to bind to the main
#screen "onkey" event method. One function, hideallturtles(), will hide the turtles
#bylooping over "allShapes" and then looping over the list of turtleShape child
#objects (a nested loop) and calling the "hideturtle()" method of the turtleShape property 
#"self.turtle." This will happen when the user presses "h" (see the KEYBINDING SECTION below).
#The second function, showallturtles(), will do the same nested loop, but call,
#self.turtle.showturtle()

#FUNCTION DEFINITIONS AND PSEUDOCODE
def hideallturtles():
    print("Goodbye: ",len(allShapes))
    #<for "shapeTypes" over allShapes>
    #    <for "shapeObject" over "shapeTypes">
    #         <call "shapeObject.turtle.hideturtle()">
    #<update main screen>
    
#Loop over allShapes which is a list of lists
#loop over each shape, show the turtle
def showallturtles():
    print("HELLO: ",len(allShapes))
    #<for "shapeTypes" over allShapes>
    #    <for "shapeObject" over "shapeTypes">
    #         <call "shapeObject.turtle.showturtle()">
    #<update main screen>

#KEYBINDING SECTION
#listen for key strokes on the m,ain screen
#bind the "onkey" method with the hideallturtles
#and showallturtles functions, use "h" for hide
#and "s" for show
screen.listen()
screen.onkey(hideallturtles, "h")
screen.onkey(showallturtles, "s")
#run forever in a mainloop()
screen.mainloop()
