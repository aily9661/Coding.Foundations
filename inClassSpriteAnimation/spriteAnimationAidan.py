import pygame, sys


#"Player" is a child class of pygame.sprite.Sprite
#must have a memember called "self.image"
#image data that is assigned to "self.image"
#will be drawn to the screen at (pos_x and pos_y)
#when the pygame.sprite.Group.draw(screen) method is 
#called (instantiated as the "moving_sprites" object below). 

class AnimationData():
    def __init__(self,fname_prefix,numFiles, color):
        self.fname_prefix = fname_prefix
        self.numFiles = numFiles
        self.isAnimating = False
        self.spriteIndex = 0
        self.spriteList = []

        for i in range(numFiles):
            if color == "NONE": self.spriteList.append(pygame.image.load(fname_prefix + '%01d' % i +'.png'))
            else: self.spriteList.append(self.getColorImage(pygame.image.load(fname_prefix + '%01d' % i +'.png'), color))

    def animate(self):
        self.isAnimating = True

    def getNextImage(self):
        if self.isAnimating:
            self.spriteIndex += 0.25

        if self.spriteIndex >= len(self.spriteList):
            self.spriteIndex = 0
            self.isAnimating = False

            #set self.image which is what is drawn when the moving_sprites.draw(screen)
            #call is made below in the main while loop. 
        self.image = self.spriteList[int(self.spriteIndex)]
        return self.image

    def getColorImage(self,myImage,color):
        colorImage = pygame.Surface(myImage.get_size()).convert_alpha()
        colorImage.fill(color)
        myImage.blit(colorImage, (0,0), special_flags = pygame.BLEND_RGBA_MULT)
        return myImage


class Player(pygame.sprite.Sprite):
    speed = 10
    def __init__(self, pos_x,pos_y, color):
        super().__init__()
        self.walkingAnimation = AnimationData("skel_",6,color)
        self.jumpingAnimation = AnimationData("skeljmp_",8,color)
        #initial image will be the first one, index 0
        self.image = self.walkingAnimation.getNextImage()
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
        if self.walkingAnimation.isAnimating: self.image = self.walkingAnimation.getNextImage()
        if self.jumpingAnimation.isAnimating: self.image = self.jumpingAnimation.getNextImage()
       
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
player = Player(0,100,"NONE")
playerTwo = Player(0,300,pygame.Color(0,255,0))
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
    jump = keystate[pygame.K_j]

    #<a new variable that captures the "pressed state" of the "j" key
    #if the "j" is pressed, this variable will be assigned the boolean "True"
    #use this variable in an if statement to call "animationJump()" if it is "True">
    if jump:
        player.jumpingAnimation.animate()

    if directionX != 0:
        player.walkingAnimation.animate()
        player.moveX(directionX)
        playerTwo.walkingAnimation.animate()
        playerTwo.moveX(-directionX)

    if directionY != 0:
        player.walkingAnimation.animate()
        player.moveY(directionY)
        playerTwo.walkingAnimation.animate()
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