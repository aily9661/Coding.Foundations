import pygame, sys


#"Player" is a child class of pygame.sprite.Sprite
#must have a memember called "self.image"
#image data that is assigned to "self.image"
#will be drawn to the screen at (pos_x and pos_y)
#when the pygame.sprite.Group.draw(screen) method is 
#called (instantiated as the "moving_sprites" object below). 

class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x,pos_y):
        super().__init__()
        #a boolean property that determines whether we are animating or not. 
        self.is_animating = False
        self.x = pos_x
        self.y = pos_y
        self.is_jumping = False
        #Our list of images saved as a property called self.sprites
        #we initialize it as an empty list and append to it in a for loop
        self.sprites = []
        #a loop for loading images
        for i in range(6):
            self.sprites.append(pygame.image.load('skel_'+ '%01d' % i +'.png'))   
        #a property for storing the current index of the list
        self.current_sprite = 0
        #initial image will be the first one, index 0
        self.image = self.sprites[self.current_sprite]
        #get the rectangle for this image
        self.rect = self.image.get_rect()
        #use the passed-in values to our class __init__ function, pos_x,pos_y
    
    # we will need to develop our update function to animate
    # our sprite and perhaps add another function!
    def update(self):
        #increment self.current_sprite if self.is_animating is True
        if self.is_animating:
            self.current_sprite += 0.25

        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0

        if self.is_jumping:
            player.y -= 2
        else:
            if player.y <= 100:
                player.y += 1

        #to place the image using the "topleft" corner of it's "rect"
        self.rect.topleft = [self.x,self.y]

        #set self.image which is what is drawn when the moving_sprites.draw(screen)
        #call is made below in the main while loop. 
        self.image = self.sprites[int(self.current_sprite)]
    
    #when any key is pressed (KEYDOWN event)
    #we set self.is_animating to True 
    def animate(self,bool):
        if bool:
            self.is_animating = True
        else:
            self.is_animating = False

    def move(self,where):
        if where == "RIGHT":
            self.x += 1.5
        if where == "LEFT":
            self.x -= 1.5
    
    def jump(self,bool):
        if bool:
            self.is_jumping = True
        else:
            self.is_jumping = False
        
       
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
player = Player(0,100)

#add the sprite to the sprite group
moving_sprites.add(player)
is_animating = False
is_jumping = False

currentkey = "NONE"

#the main drawing and event loop of a pygame application
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        #if any key is pressed (pygame.KEYDOWN event)
        #call player.animate() which just sets player.is_animating = True
        if event.type == pygame.KEYDOWN:
            is_animating = True
            player.animate(is_animating)
            if event.key == pygame.K_UP:
                currentkey = "UP"
                is_jumping = True
            if event.key == pygame.K_DOWN:
                currentkey = "DOWN"
            if event.key == pygame.K_LEFT:
                currentkey = "LEFT"
            if event.key == pygame.K_RIGHT:
                currentkey = "RIGHT"

        if event.type == pygame.KEYUP:
            is_animating = False
            player.is_jumping = False
            player.animate(False)
            player.current_sprite = 0
            currentkey = "NONE"

    if is_animating:
        player.move(currentkey)
    
    if is_jumping and currentkey == "UP":
        player.jump(currentkey)

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
