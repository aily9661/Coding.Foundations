import pygame, sys


#"Player" is a child class of pygame.sprite.Sprite
#must have a memember called "self.image"
#image data that is assigned to "self.image"
#will be drawn to the screen at (pos_x and pos_y)
#when the pygame.sprite.Group.draw(screen) method is 
#called (instantiated as the "moving_sprites" object below). 

class Player(pygame.sprite.Sprite):
    speed = 10
    def __init__(self, pos_x,pos_y,color): #need to add for getColorImage extra credit
        super().__init__()
        #a boolean property that determines whether we are animating or not. 
        self.is_animating = False

        #PC07 (1): We need another boolean to control animating our "jump"
        #animation. When we push 'j' in the main event loop this boolean
        #will be set to true

        #<new boolean property for controlling jump animation state>
        self.is_jumping = False
        #Our list of images saved as a property called self.sprites
        #we initialize it as an empty list and append to it in a for loop
        self.sprites = []

        #PC07 (2): We need another list in our Player class to manage our jump images
        #these images are included in your starter code as "skeljmp_0.png", "skeljmp_1.png"
        #etc..

        #<a new list for storing and managing the "jump" animation>
        self.jump_sprites = []
        #a loop for loading images
        for i in range(6):
            myImage = pygame.image.load('skel_'+ '%01d' % i +'.png')
            self.sprites.append(self.getColorImage(myImage,color))  
        #PC07 (3): We need another loop to load our jump animation images and append them
        # to our new list. In the start file there are 8 skeljmp_N.png images. You'll
        # append these images to the list you created above
        #<a new for loop that loads our new skeljmp images and appends them to our new list>
        
        for i in range(8):
            myImage = pygame.image.load('skeljmp_'+ '%01d' % i +'.png')
            self.jump_sprites.append(self.getColorImage(myImage,color))
        #a property for storing the current index of the list
        self.current_sprite = 0

        #PC07 (4): we need a new property to index into our new list of jump image
        #<a new property for keeping track of an index for our new list of jmp images>
        self.current_jump_sprite = 0
        #initial image will be the first one, index 0
        self.image = self.sprites[self.current_sprite]
        #get the rectangle for this image
        self.rect = self.image.get_rect()
        #use the passed-in values to our class __init__ function, pos_x,pos_y
        #to place the image using the "topleft" corner of it's "rect"
        self.rect.topleft = [pos_x,pos_y]
    
    def moveX(self, direction):
        self.rect.move_ip(direction * self.speed, 0)
        self.rect = self.rect.clamp((0,0,640,480))

    def moveY(self, direction):
        self.rect.move_ip(0, direction * self.speed)
        self.rect = self.rect.clamp((0,0,640,480))

    # we will need to develop our update function to animate
    # our sprite and perhaps add another function!
    def update(self):
       self.runAnimationBasic()
       self.runAnimationJump()
    
    #MP07 -- Create a new method "runAnimationBasic()" that does what the update()
    #function currently does. The idea is that we may have several animation
    #behaviors and our update() function can call each of the animation methods.
    #This is mainly to keep things clean and separate different animation behaviors
    #from each other to decrease the chance of introducing errors.
    #For the finished PC07 project we will have "runAnimationBasic()" and 
    # "runAnimationJump()"
    
    #Here is the stub for runAnimationBasic() uncomment the line below to develop
    #this function (which will literally be copying the current contents of update()
    # into this function) to be replaced by calling this function instead
    #What is different about calling a method inside a class versus outside the class?

    def runAnimationBasic(self):
        #increment self.current_sprite if self.is_animating is True
        if self.is_animating:
            self.current_sprite += 0.25

        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
            self.is_animating = False

        #set self.image which is what is drawn when the moving_sprites.draw(screen)
        #call is made below in the main while loop. 
        self.image = self.sprites[int(self.current_sprite)]

    #PC07 (5): We now want to write a function "runAnimationJump()" it is going to be the
    #exact same structure of "runAnimationBasic()" but using the new properties we defined
    #in the Player class (our new boolean, our new list, and our new index variable)
    #in our "update()" function, we will just call "animationBasic()" and "animationJump()"
    #this will keep different animation behaviors separated from each other and reduce
    #the introduction of erros

    #<a runAnimationJump() function, it has the same structure of runAnimationBasic, 
    #but needs to use the new properties we added to the Player class>
    def runAnimationJump(self):
        #increment self.current_sprite if self.is_animating is True
        if self.is_jumping:
            self.current_jump_sprite += 0.25

            if self.current_jump_sprite >= len(self.jump_sprites):
                self.current_jump_sprite = 0
                self.is_jumping = False

            #set self.image which is what is drawn when the moving_sprites.draw(screen)
            #call is made below in the main while loop. 
            self.image = self.jump_sprites[int(self.current_jump_sprite)]
    #When any of the arrow keys are pressed (direction != 0 below in the main loop)
    #we set self.is_animating to True 
    def animate(self):
        self.is_animating = True

    #PC07 (6): We need an "animateJump()" function that sets the new jump animation
    #boolean to true. It is the same as animate() but operates on the first new property
    #you added to the Player class above

    #<a new "animateJump()" function
    def animateJump(self):
        self.is_jumping = True
    #EXTRA CREDIT ONE use getColor to color sprites (works with for loop above)
    def getColorImage(self,myImage,color):
        colorImage = pygame.Surface(myImage.get_size()).convert_alpha()
        colorImage.fill(color)
        myImage.blit(colorImage, (0,0), special_flags = pygame.BLEND_RGBA_MULT)
        return myImage
       
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
#and drawing sprites to a screen. 
moving_sprites = pygame.sprite.Group()

#an instance of our Player class
player = Player(0,100,pygame.Color(255,0,0)) #if they do getColorImage credit they need to do this
playerTwo = Player(0,300,pygame.Color(0,255,0)) #green
#add the sprite to the sprite group
moving_sprites.add([player,playerTwo])

#the main drawing and event loop of a pygame application
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        #if any key is pressed (pygame.KEYDOWN event)
        #call player.animate() which just sets player.is_animating = True
        
    keystate = pygame.key.get_pressed()
    directionX = keystate[pygame.K_RIGHT] - keystate[pygame.K_LEFT]
    directionY = keystate[pygame.K_DOWN] - keystate[pygame.K_UP]

    #PC07 (6): Create a variable for determining whether the lowercase
    #"j" has been pressed. You will use the keystate list and index
    #it with "pygame.K_j" This will return True when the key is pressed
    #To use this variable (maybed called playerJumped or something similar)
    #We need an if statement that tests if this boolean is True and if so
    #it should call "animationJump()" from above which sets our jump animation
    #boolean to True

    #<a new variable that captures the "pressed state" of the "j" key
    #if the "j" is pressed, this variable will be assigned the boolean "True"
    #use this variable in an if statement to call "animationJump()" if it is "True">
    playerJumped = keystate[pygame.K_j]
    if playerJumped:
        player.animateJump()

    if directionX != 0:
        player.animate()
        player.moveX(directionX)
        playerTwo.animate()
        playerTwo.moveX(-directionX)

    if directionY != 0:
        player.animate()
        player.moveY(directionY)
        playerTwo.animate()
        playerTwo.moveY(-directionY)

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

    ##EXTRA CREDIT 2 Points, color your sprite with a user defined color
    #when it is instantiated.
    
    #The following function can be added to the Player class
    #You want to run the images you load in the Player class through this
    #function *BEFORE* you add them to their lists. When you instantiate the class
    #you can pass it a color (which also needs to be added to the __init__ function
    # of the Player class):   player = Player(0,100,Color(255,0,0)) Would make a RED
    #player if the code is used properly in the Player class. Give it a try!
    #def getColorImage(self,myImage,color):
    #    colorImage = pygame.Surface(myImage.get_size()).convert_alpha()
    #    colorImage.fill(color)
    #    myImage.blit(colorImage, (0,0), special_flags = pygame.BLEND_RGBA_MULT)
    #    return myImage

    #EXTRA CREDIT 3 Points, create your own sprite images
    #on https://www.piskelapp.com/p/create/sprite or another
    #image creating program (Adobe Photoshop etc..)