import turtle 
import math
import colorsys
import random
import numpy as np
import simpleaudio as sa

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

# Create a Turtle object
t = turtle.Turtle() #instantiate your Turtle
t.speed(0)  # Set the drawing speed (0) which is the "fastest"
t.color("red") #this will be the active color until/if it is changed

t.shape("turtle") #this will make our drawing pointer look like a turtle
t.turtlesize(1) #this will make it a little bigger

##HERE WE WILL DEFINE FUNCTIONS THAT DRAW SHAPES AT A GIVEN LOCATION##
def getRainbowColor(hue):
    color = colorsys.hsv_to_rgb(hue, 1, 1)
    return color

def drawASquare(t, x, y, length, color="yellow"):
    #make sure and call t.penup() so we do not see a line for where the turtle moves
    t.penup()
    t.goto(x-length/2,y-length/2) #we offset the x and y coordinates by (-length/2) so that
    t.pendown()                   #our square is centered on x,y, otherwise it will start
    t.color(color)             #drawing the square at one of the corners at x,y
    #since a square is four sides we can loop over a range(4) function
    #and call either t.forward(length), t.left(90), or t.backward(lentgh), t.right(90)
    for i in range(4):
        t.forward(length)
        t.left(90)

def drawARect(t, x, y, width, height, strokeColor="yellow", fillColor="NONE"):
    t.penup()
    t.goto(x-width/2,y-height/2) #offset the x coordinate by (-width/2)
    t.pendown()                  #offset the y coordinate by (-height/2)

    #here we are checking to see if a "fill" color is defined, if so
    #define t.color with two colors, first will be the "stroke" color (outline)
    #and the second color will be the "fill" color
    if fillColor != "NONE": #draw the rectangle with a stroke and fill color
        t.color(strokeColor,fillColor)
        t.begin_fill()
        for i in range(4):
            if i % 2 == 0:       #for every second step through the loop draw a width
                t.forward(width) #else draw a height
            else:
                t.forward(height)
            t.left(90)
        t.end_fill()
    else: #draw the rectangle only with a stroke color (outline only, no fill)
        t.color(strokeColor)
        for i in range(4):
            if i % 2 == 0:
                t.forward(width)
            else:
                t.forward(height)
            t.left(90)

def drawACircle(t, x, y, radius, strokeColor="yellow", fillColor="NONE"):
    t.penup()
    t.goto(x,y - radius) #to center circle at x,y we need to offset the y coordinate by
    t.pendown()          #-radius , tutrle draw circles starting at the bottom border
    #here we use an if statement and have a branch in the code
    #the draw the circle with both an outline and fill color, or just an outline color
    if fillColor != "NONE":
        t.color(strokeColor,fillColor)
        t.begin_fill()
        t.circle(radius)
        t.end_fill()
    else:
        t.color(strokeColor)
        t.circle(radius)

def drawRightTriangle(t, x, y, base, height, isoMode, drawRight, strokeColor="gray", fillColor="NONE"):
    #calculate the hypotenuse using the pythagorean theorem
    #since we pass in a base and height, we can immediately do this
    hypotenuse = math.sqrt(base*base + height*height)
    t.penup()
    t.goto(x, y-(height/2)) #center the triangle in the middle of its height
    t.pendown()

    #if fillColor is equal to "NONE" (default)
    #set strokeColor. Otherwise set strokeColor and fillColor and
    #call t.begin_fill()
    if fillColor == "NONE":
        t.color(strokeColor)
    else:
        t.color(strokeColor,fillColor)
        t.begin_fill()

    if drawRight: #if this is true, we will draw a right triangle with the base acute angle
                  #pointing to the right if false it points to the left
        t.forward(base) #draw the base of the triangle
        #calculate the angle "A" which is the acute on the base
        t.left(180. - math.asin(height/hypotenuse) * (180./math.pi)) 
        t.forward(hypotenuse)  #go "forward" to draw the hypotenuse  
        #calculate the "top" or "B" angle (the other angle that is not 90 degrees!)
        t.left(180. - math.asin(base/hypotenuse) * (180./math.pi))
        #if we are using this function to draw an isoceles triangle
        #then don't draw the "height"
        if isoMode:
            t.penup()
            t.forward(height)
            t.pendown()
        else:
            t.forward(height)

        t.left(90.) #do a final rotation so that we are back to our initial orientation
        
        #draw the triangle that points in the other direction
        #everything is the same but we use backward and right instead of forward and left
    else:
        t.backward(base)
        t.right(180. - math.asin(height/hypotenuse) * (180./math.pi))
        t.backward(hypotenuse)
        t.right(180. - math.asin(base/hypotenuse) * (180./math.pi))
        if isoMode:
            t.penup()
            t.backward(height)
            t.pendown()
        else:
            t.backward(height)
        t.right(90.)
    #be sure to call end_fill if fillColor is not equal to "NONE"
    if fillColor != "NONE":
        t.end_fill()

def drawIsoTriangle(t, x, y, base, height, strokeColor="yellow", fillColor="NONE"):
    #we can now draw any type of isosceles triangle by drawing two
    #right triangles that are mirror images of each other, we pass
    #True to the seventh argument (drawRight) to draw a right triangle
    #that points to the right and False to draw a right triangle that
    #points to the left. We set isoMode=True so that we don't draw
    #the "height" line for the isosceles triangle.
    drawRightTriangle(t,x,y, base, height, True, True, strokeColor, fillColor)
    drawRightTriangle(t,x,y, base, height, True, False, strokeColor, fillColor)

#this function will draw 360//angle_to_rotate circles to create an overlapping
#circles object, a smaller "angle_to_roatate" value will draw more circles
def drawOverlappingCircles(t, x, y, radius, forward_movement, angle_to_rotate, useRainbow, color):
    #forward_movement is a "spoke" that is drawn within each circle
    #experiment with changing this value
    numberOfCircles = 360//angle_to_rotate #we want to draw a full 360 degrees of overlapping circles
    for i in range(numberOfCircles):  #loop over number circles, draw the circle, draw the "spoke"
        t.penup()                     #then rotate the turtle by "angle_to_rotate"
        t.goto(x,y - radius) #offset y coordinate by -radius to center the circle
        t.pendown()
        if useRainbow:
            t.color(getRainbowColor(i/numberOfCircles)) #they can use this function to draw each circle
        else:                                           #with a different color of the rainbow
            t.color(color)
        #with a different color of the rainbow
        t.circle(radius) #draw a circle with radius
        t.forward(forward_movement) #draw a spoke
        t.right(angle_to_rotate) #rotate the turtle for next run through the loop

##You should be able to draw a similar "bullseye" function for
##every type of shape. You just need to scale the width and height
##or length of the shape in the same way that the radius is scaled below
def drawCircleBullsEye(t,x,y,initradius,numRings,strokeColor="yellow",fillColor="NONE"):
    for i in range(numRings):
        t.penup()
        t.goto(x,y-initradius)
        t.pendown()
        t.color(strokeColor)
        ##scale the the size of the radius by the control variable i
        ##this will make each circle larger than the last.
        #if the fillcolor is NONE draw concentric circles starting from the center
        #if the fillcolor is defined then draw filled concentric circles starting
        #with the largest circle which will have a radius of (numRings*initradius)
        if fillColor == "NONE":
            drawACircle(t,x,y,i*initradius,strokeColor,fillColor)
        else:
            #here we choose a random color for each filled concentric circle
            #if you want more control over this, you could write your own
            #drawCircleBullsEye() function or just use carefully placed circles with
            #drawACircle()
            drawACircle(t,x,y,(numRings-i)*initradius,strokeColor,random.choice(myColors))

def drawStopLight(t,x,y,scale=1.0):
    #lets make a stop light with a default
    #rectangle width of 50 and a height of 120, lightRadius of 15
    #we'll place our circles in y at + 0.3*rectHeight, rectCenter, - 0.3*rectHeight
    #we can use our scale number to change its overall size
    rectWidth = 50. * scale
    rectHeight = 120. * scale
    lightRadius = 15. * scale
    drawARect(t,x,y,rectWidth,rectHeight,"white","gray")
    drawACircle(t,x,y+(rectHeight*0.3),lightRadius,"gray","red")
    drawACircle(t,x,y,lightRadius,"gray","yellow")
    drawACircle(t,x,y-(rectHeight*0.3),lightRadius,"gray","green")

def drawSunSettingBehindMountains(t):
    #sun
    drawACircle(t,50,-250,250,"orange","darkred")
    #far away mountains
    drawIsoTriangle(t,-350,-350,200,800,"white","darkorchid4")
    drawIsoTriangle(t,0,-350,200,600,"white","darkorchid4")
    drawIsoTriangle(t,300,-350,200,500,"white","darkorchid4")
    #close mountain
    drawIsoTriangle(t,-250,-250,200,1000,"white","darkorchid")
    
##PUT YOUR drawPolygon() FUNCTION HERE!!!
def drawPolygon(t,x,y,numSides,sideLength,strokeColor="yellow", fillColor="NONE"):
    myVertextCoordinates = []
    angle_to_rotate = 360//numSides
    t.penup()
    t.goto(x-(sideLength/2),y-(sideLength/2))
    t.pendown()
    for i in range(numSides):
        t.forward(sideLength)
        t.left(angle_to_rotate)
        myVertextCoordinates.append(t.pos())

    return myVertextCoordinates

##Add your getNewNote() function HERE!!
def getNewNote(baseFreq,nSemitones):
      return baseFreq*2**(nSemitones/12)

baseFrequency = 440
nSemitones = 3

print(getNewNote(baseFrequency,nSemitones))
##Add the play_tone function here
def play_tone(x, y,radius):
    # Map x and y coordinates to frequencies
    base_frequency = 220.0  # Adjust as needed

    #BRADS COMMENT: Instead of basing the frequency on its x,y location
    #we will compute a frequency using our getNewNote(baseFreq,nSemitones)
    #function and we can use the two lists of semitones below, which will
    #always give us the notes of a major (the first list) or minor pentatonic
    #scale, which will always sound somewhat consonant

    semitoneListMajor = [0,2,4,7,9,12,16,19] #major pentatonic scale
    semitoneListMinor = [0,3,5,7,10,12,15,17] #minor pentatonic scale

    #We can get rid of all of this
    x_scale = 5.0  # Adjust to change the scale of the x-axis mapping
    y_scale = 2.0  # Adjust to change the scale of the y-axis mapping
    frequency = getNewNote(base_frequency,random.choice(semitoneListMajor))
    #And replace it with:
    #frequency = getNewNote(base_frequency,
    # random.choice(semiToneListMajor or semiToneListMinor))

    # Calculate the duration based on circle radius

    #BRADS COMMENT: This is not the radius but the distance to the
    #center. Since we are specifying a radius for our circle
    #either explictly or through a random number generator
    #lets just change the function and pass in the radius
    #as an argument and delete the radius assignment below

    #this will make the tone duration longer with a bigger radius
    duration = radius * 0.005  # Adjust the scale as needed, 0.005 is lowest you should go

    # Generate a sine wave with fade-in and fade-out
    sample_rate = 44100  # Sample rate in Hz
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    fade_duration = 0.05  # Adjust the fade-in/fade-out duration as needed
    fade_samples = int(fade_duration * sample_rate)

    # Create a fade-in and fade-out envelope
    fade_in = np.linspace(0, 1, fade_samples)
    fade_out = np.linspace(1, 0, fade_samples)

    # Generate the sine wave
    wave = 0.5 * np.sin(2 * np.pi * frequency * t)

    # Apply fade-in and fade-out
    wave[:fade_samples] *= fade_in
    wave[-fade_samples:] *= fade_out

    # Play the sine wave
    play_obj = sa.play_buffer((wave * 32767).astype(np.int16), 1, 2, sample_rate)
    play_obj.wait_done()

##HERE IS WHERE THE DRAWING WILL HAPPEN, WE WILL CALL THE FUNCTIONS
##DEFINED ABOVE IN VARIOUS WAYS

#if you want to see your turtle
#comment out the line below
t.hideturtle()

#experiment with uncommenting the line below
#alonh with uncommenting the "screen.update()" call
#below. What happens? What happens if you indent the
# "screen.update()" call all the way to the left?

#draw some circles and play some tones
screen.tracer(0)
radius = 10 #start the radius at 10
modFreq = 10 #change the radius and modFreq after 10 initial circles are drawn
for i in range(400): #draw 400 circles and play 400 notes
    #draw a circle
    x = 0
    y = 0
    #use a while loop to make sure we don't
    #have x or y assigned to zero by random.randint
    #if either x or y happens to be assigned zero the
    #loop will make it try again until it isn't equal to zero
    while x == 0 and y == 0:
        x = random.randint(-300,300)
        y = random.randint(-400,400)

    #this will change the radius and
    #the frequency at which the radius is changed (modFreq)
    #this gives the "music" more rhythmic changes
    #playing with the ranges of the random.randint calls
    #will change the rhythym because the bigger the radius
    #the longer the duration and the smaller the modFreq
    #the more often both things will be changed
    if i % modFreq == 0:
        radius = random.randint(10,100)
        modFreq = random.randint(3,9)
    #will draw a circle with both a stroke and fill color
    drawACircle(t,x,y,radius,random.choice(myColors), random.choice(myColors))
    screen.update()
    play_tone(x,y,radius) #need to add and adapt this function from
                          #play_tone_function_chatgpt.py
#This keeps the turtle screen active until it is clicked on
#to exit
screen.exitonclick()
