import pygame, sys

#a class for our "Player" sprite
#it inherits from the parent class
#pygame.sprite.Sprite which works
#with pygame.sprite.Group to manage
#updating and drawing groups of sprites

#a child class of pygame.sprite.Sprite
#must have a memember called "self.image"
#image data that is assigned to "self.image"
#will be drawn to the screen at (pos_x and pos_y)
#when the pygame.sprite.Group.draw(screen) method is 
#called. To animate a sprite, we will need a list
#of images, and our update function needs to manage
#which image is being drawn and when

class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x,pos_y):
        super().__init__()
        #a boolean property that determines whether we are
        #animating or not. Animating in this context will reduce to
        #managing an index variable "self.current_sprite" which will
        #be used to access a particular image at a particular index in
        #a list of images
        self.is_animating = False
        
        #Our list of images saved as a property called self.sprites
        #we initialize it as an empty list and append to it in a for loop
        self.sprites = []

        #In our current example, we have 6 images named "skel_0.png" through
        #"skel_5.png." We use a for loop over a range(6) function to use the
        #i control variable to build the file name in the pygame.image.load
        #function below. The part of the string "'%01d' % i" means turn the integer
        # "i" into a string with no leading zeros. If our animation had 10 or
        #more images composing it, it would be important to add a leading zero to
        #the single digit numbers, so functions that list directories and folders
        #to find file names will get the file names in the right order.
        #for this reason if we had 20 files in our animation,the first ten files
        #would need the form "skel_00.png" "skel_01.png...skel_09.png" You will notice 
        #that Piskel.app (online sprite builder) will package the files in the zip
        #this way when more than 10 files are made.
        for i in range(6):
            self.sprites.append(pygame.image.load('skel_'+ '%01d' % i +'.png'))

        #self.current_sprite is a property we are using as an index into our
        #list, self.sprites. Our update() function will need to increment
        #this value to access the different images in our list to "play" the 
        #animation each time update is called.
        #NOTE: An index into a list has to be an integer. In our
        #current example, only indicies 0 through 5 are valid sine we have 6
        #images. However, we will use a trick where we treat it as a float
        #in our update() function and increment it by a value less than one 
        # (e.g. 0.2), when we use self.current_sprite to access an image in
        #self.sprites[] we will use the int() function to "floor" the value.
        #For instance int(0.2) = 0 int(0.4) = 0 ... and int(2.2) = 2 int(2.4) =2
        #etc..
        self.current_sprite = 0

        #initial image will be the first one, index 0
        self.image = self.sprites[self.current_sprite]

        #get the rectangle for this image, the rect is a strcture
        #that has the following form rect(x_origin,y_origin,width,height)
        #when we call "get_rect()" on an image we get its size and
        #can set its location with an x,y coordinate. However, imagine
        #a rectangle that encompasses your image, what part of the
        #rect do you place at the x,y coordinate? To address this, there are 
        #attributes of the rect class that are referenced in the Oct 17th
        #Slides, and found at https://www.pygame.org/docs/ref/rect.html
        #(the first yellow box about a page of scrolling down) Each of the attributes
        #are relative locations on the "rect." Try switching the code below to
        #self.rect.bottomleft = [pos_x,pos_y] and see how it affects the placement
        #of the image.
        self.rect = self.image.get_rect()

        #use the passed-in values to our class __init__ function, pos_x,pos_y
        #to place the image using the "topleft" corner of it's "rect"
        self.rect.topleft = [pos_x,pos_y]
    
    # we will need to develop our update function to animate
    # our sprite and perhaps add another function!
    def update(self):

        #self.is_animating is set to True in the main while loop
        #when any key is pressed down by calling the animate().
        #function below. When self.is_animating is True
        #we increment self.current_sprite, but we do so with
        #a floating point number that is less than one. When
        #we use self.current_sprite to access or list, we
        #do it with the int() function, which "floors" the value
        # (i.e. int(0.25) = 0...int(0.75)=0, int(1.25) = 1, etc..)
        #in the case of incrementing by 0.25, it means that we draw
        #each image 4 times in a row, which will slow down the animation.
        #the smaller the increment value the slower the animation will go
        #the larger it is the faster it will go.
        if self.is_animating:
            self.current_sprite += 0.1

        #we need to check if the self.current_sprite >= len(self.sprites)
        # because we increment it first, and if we increment by a value 
        # less than one that is greater than 0.25, it's value will be greater
        # than the length of the list. We set self.current_sprite back to 0
        # and self.is_animating to False so animation stops until another
        # KEYDOWN event is detected in the main while loop 
        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
            self.is_animating = False

        #set self.image which is what is drawn when the moving_sprites.draw(screen)
        #call is made below in the main while loop. We pass int(self.current_sprite)
        #so that we get an integer index as described above
        self.image = self.sprites[int(self.current_sprite)]
    
    #when any key is pressed (KEYDOWN event)
    #we set self.is_animating to True (see the main while loop)
    #this makes the update function increment self.current_sprite
    #and run the animation (draw each image N times) until
    #another KEYDOWN event is detected
    def animate(self):
        self.is_animating = True
       
#initializes the pygame environment
pygame.init()
#gives a clock with which we can run
#the game at a certain frame rate (frames per second or FPS)
clock = pygame.time.Clock()

#the width and height of our screen
screen_width = 640
screen_height = 480

#create screen that will provide a pygame.Surface to draw to
#all images, including the screen are pygrame.Surfaces
screen = pygame.display.set_mode((screen_width,screen_height))
#a caption for our game app
pygame.display.set_caption("Sprite Animation")

#pygame.sprite.Group() is a class that manages updating
#and drawing sprites to a screen. Each instance of a sprite
#is added to this object with the "add" method
#moving_sprites is our sprite group. Calling "draw()" and
#update() on our sprite group will draw and update all the
#sprites that have been added to the group

moving_sprites = pygame.sprite.Group()

#an instance of our Player class
#the coordinates here, are the screen coordinates
#we wish to place our sprite. Within our Player class
#we will specify which "rect" attribute (topleft, bottomleft, top, bottom, etc)
#this screen coordinate gets assigned to which will affect how
#the image is placed on the screen
player = Player(0,100)

#add the sprite to the sprite group
moving_sprites.add(player)

#the main drawing and event loop of a pygame application
#In this infinite while loop, the first thing we do is loop
#over events, which could be input from the mouse, keyboard
#or some kind of game controller. In this example we are checking
#for the pygame.QUIT event which occurs when the user clicks on
#the close application button
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            player.animate()

    #color fill the screen with black,
    #notice this is a tuple
    screen.fill((0,0,0))
    
    #draw our sprites to our screen
    moving_sprites.draw(screen)
    
    #call our update function
    moving_sprites.update()
    
    #call pygame.display.flip() which renders a whole screen
    #for this frame
    pygame.display.flip()
    
    #make the while loop and game operate at
    #60 FPS, updates are throttled to this amount
    clock.tick(60)
