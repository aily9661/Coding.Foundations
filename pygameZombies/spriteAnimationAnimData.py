import pygame, sys
import random
import math

SCREENRECT = pygame.Rect(0,0,1024,768)

class AnimationData():
    def __init__(self,fname_prefix,numFiles,color):
        self.fname_prefix = fname_prefix
        self.numberOfFiles = numFiles
        self.spriteList = []
        self.spriteListIdx = 0
        self.is_animating = False

        #load our images, if the color parameter is NONE just load
        #the image, otherwise pass it through getColorImage to color the sprite
        for i in range(self.numberOfFiles):
            myImage = pygame.image.load(self.fname_prefix + "%01d" % i + ".png")
            if color != "NONE":
                self.spriteList.append(self.getColorImage(myImage,color))
            else:
                self.spriteList.append(myImage)

    def animate(self):
        self.is_animating = True

    def getNextImage(self):
        #increment the index by 0.25, you may want
        #to add this as an additional parameter that we
        #pass to the __init__ function
        self.spriteListIdx += 0.25

        #if self.spriteListIdx is greater than or equal to
        #the length of the self.spriteList list then reset
        #self.spriteListIdx to 0 and set is_animating to False
        if self.spriteListIdx >= len(self.spriteList):
            self.spriteListIdx = 0
            self.is_animating = False

        #return the image at the index int(self.spriteListIdx)
        return self.spriteList[int(self.spriteListIdx)]
    
    def getColorImage(self,myImage,color):
        colorImage = pygame.Surface(myImage.get_size()).convert_alpha()
        colorImage.fill(color)
        myImage.blit(colorImage, (0,0), special_flags = pygame.BLEND_RGBA_MULT)
        return myImage
    
class Player(pygame.sprite.Sprite):
    speed = 10
    def __init__(self, pos_x,pos_y,color):
        super().__init__()
        #we add two properties, one for each type of animation
        #the walking and jumping animations, we can now
        #call methods like: self.walkingAnimation.animate() 
        #or check properties like: self.walkingAnimation.is_animating
        #when a Player() class is instantiated to an object we can access
        #these properties and methods like: player.walkingAnimation.animate()
        #and player.walkingAnimation.is_animating
        self.walkingAnimation = AnimationData("skel_",6,color)
        self.jumpingAnimation = AnimationData("skeljmp_",8,color)
        self.diesAnimation = AnimationData("skeldies_",9,color)
    
        #use the getNextImage() method from self.walkingAnimation to set initial image
        self.image = self.walkingAnimation.getNextImage()
        #get the rectangle for this image
        self.rect = self.image.get_rect()
        #use the passed-in values to our class __init__ function, pos_x,pos_y
        #to place the image using the "topleft" corner of it's "rect"
        self.rect.topleft = [pos_x,pos_y]
    
    def moveX(self, direction):
        self.rect.move_ip(direction * self.speed, 0)
        self.rect = self.rect.clamp(SCREENRECT)

    def moveY(self, direction):
        self.rect.move_ip(0, direction * self.speed)
        self.rect = self.rect.clamp(SCREENRECT)

    # we will need to develop our update function to animate
    # our sprite and perhaps add another function!
    def update(self):
        #Test to see if the "is_animating" property is true
        #for self.walkingAnimation.is_animating and
        #for self.jumpingAnimation.is_animating. If these
        #booleans are True (test separately in if statements)
        #then call getNextImage() on that animation property
        #and assign the output (an image) to self.image
        if self.walkingAnimation.is_animating:
            self.image = self.walkingAnimation.getNextImage()
        if self.jumpingAnimation.is_animating:
            self.image = self.jumpingAnimation.getNextImage()

class Shot(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y,isLeft):
        super().__init__()
        self.shotAnimation = AnimationData("shots_",2,"NONE")
        self.isLeft = isLeft 
        self.speed = 5
        if self.isLeft: 
            self.image = self.shotAnimation.spriteList[0]
        else: 
            self.image = self.shotAnimation.spriteList[1]

        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y

    def update(self):
        if self.isLeft:
            self.rect.move_ip(-1*self.speed, 0)
            if self.rect.left <= 0:
                self.kill()
        else:
            self.rect.move_ip(-1*self.speed, 0)
            if self.rect.right >= SCREENRECT.width:
                self.kill()

#will add an NPC class
class NPC(Player):
    def __init__(self,pos_x,pos_y,color,player):
        super().__init__(pos_x,pos_y,color)

        self.rect = self.image.get_rect()
        self.player = player

        # Set the NPC's initial position
        self.rect.x = random.randint(0, SCREENRECT.width)
        self.rect.y = random.randint(0, SCREENRECT.height)

        # Set the speed the semi-random walk
        self.speed = 2

    def update(self):
        #assign a new image
        self.image = self.walkingAnimation.getNextImage()
        #Calculate the distance between our "player" rectangle
        #and our "NPC" rectangle. We calculate the distance separately
        #in x and y by subtracting the centerx and centery attributes
        #of the two rectangles

        #distance between player and NPC in x
        dx = self.player.rect.centerx - self.rect.centerx 
        #distance between player and NPC in y
        dy = self.player.rect.centery - self.rect.centery 
        #the total distance (pythagorean theorem) we will use
        #this to scale or normalize, dx and dy in a range between -1. and 1
        distance = math.sqrt(dx**2 + dy**2)
        #if the player character is jumping use the opposite direction to
        #make the NPC move away from the player
        if player.jumpingAnimation.is_animating:
            distance = -distance

        #Move the NPC towards or away from the player
        #must check for absolute value of the distance for
        #this. With distance being normalized between -1. and 1.
        #we are changing the centerx and centery attributes
        #of our NPC rect by -6 to 6 pixels, based on the default
        #value of the speed being 2 and the random change for every
        #one out of ten updates of the speed between 1 and 6 (below)
        if abs(distance) > 0:
            dx_normalized = dx / distance
            dy_normalized = dy / distance
            #we could also use our moveX and moveY methods
            #from our Player class. Can you tell if there is a 
            #difference between the below and using
            #self.moveX(self.speed * dx_normalized)
            #self.moveY(self.speed * dy_normalized)    
            self.rect.centerx += self.speed * dx_normalized
            self.rect.centery += self.speed * dy_normalized
           
        #for every one out ten updates randomly change
        #the speed between 1 and 6
        if random.random() < 0.1:
            self.speed = random.randint(1,6)


#initializes the pygame environment
pygame.init()
#gives a clock with which we can run
#the game at a certain frame rate (frames per second or FPS)
clock = pygame.time.Clock()


#create screen that will provide a pygame.Surface to draw to
#all images, including the screen are pygrame.Surfaces
width = SCREENRECT.width
height = SCREENRECT.height
screen = pygame.display.set_mode((width,height))
#a caption for our game app
pygame.display.set_caption("Sprite Animation")

#pygame.sprite.Group() is a class that manages updating
#and drawing sprites to a screen. 
player_group = pygame.sprite.Group()
shot_group = pygame.sprite.Group()
npc_group = pygame.sprite.Group()

#add one instance of our Player class, colored RED 
#add two instances of our NPC class, colored GREEN
player = Player(0,100,pygame.Color(255,0,0)) #RED
npcOne = NPC(0,300,pygame.Color("green"),player) #GREEN
npcTwo = NPC(0,300,pygame.Color("green"),player) #GREEN

#add the sprites to the sprite group
player_group.add(player)
npc_group.add([npcOne,npcTwo])


#the main drawing and event loop of a pygame application
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    keystate = pygame.key.get_pressed()
    directionX = keystate[pygame.K_RIGHT] - keystate[pygame.K_LEFT]
    directionY = keystate[pygame.K_DOWN] - keystate[pygame.K_UP]

    #detect 'j' keypress
    jumpCommand = keystate[pygame.K_j]
    
    #if 'j' was pressed
    if jumpCommand != 0: 
        #call animate on the player jumpingAnimation property
        #this causes one full animation through our list
        #of images per detection of the 'j' event
        player.jumpingAnimation.animate()

    shootLeft = keystate[pygame.K_k]
    if shootLeft != 0:
        shot = Shot(player.rect.centerx,player.rect.centery,True)
        shot_group.add(shot)

    shootRight = keystate[pygame.K_l]
    if shootRight != 0:
        shot = Shot(player.rect.centerx,player.rect.centery,False)
        shot_group.add(shot)
  
    #If the left,right (diretionX) or up,down (directionY) keys
    #have been pressed then call the walkingAnimation.animate()
    #method foreach player. Replace the four comments below
    #with the right call.
    if directionX != 0:
        #call animate on the player walkingAnimation property
        player.walkingAnimation.animate()
        player.moveX(directionX)
      
    if directionY != 0:
        #call animate on the player walkingAnimation property
        player.walkingAnimation.animate()
        player.moveY(directionY)
      
    #color fill the screen with black,
    #notice this is a tuple
    screen.fill((0,0,0))
    
    #call our update function
    player_group.update()
    npc_group.update()
    shot_group.update()

    for npc in pygame.sprite.groupcollide(npc_group, shot_group, 0, 1).keys():
        npc.diesAnimation.animate()
    #draw our sprites to our screen
    player_group.draw(screen)
    npc_group.draw(screen)
    shot_group.draw(screen)
    
    #call pygame.display.flip() which renders a whole screen
    #for this frame
    pygame.display.flip()
    
    #make the while loop and game operate at
    #60 FPS, updates are throttled to this amount
    clock.tick(60)