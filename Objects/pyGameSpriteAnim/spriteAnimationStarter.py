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
        self.sprites = []
        for i in range(6):
            self.sprites.append(pygame.image.load('/Users/aidanlynch/Documents/GitHub/Coding.Foundations/Objects/pyGameSpriteAnim/skel_'+ '%01d' % i + '.png'))
        
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x,pos_y]

        self.is_animating = False
    
    # we will need to develop our update function to animate
    # our sprite and perhaps add another function!
    def update(self):
        if self.is_animating: 
            self.current_sprite += 1

        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0

        self.image = self.sprites[self.current_sprite]
        
       
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
            Player.is_animating = True

      
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
