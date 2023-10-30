import pygame
import sys
class AnimationData():
    def __init__(self,fname_prefix,numFiles,color):
        self.fnamePrefix = fname_prefix
        self.numberOfFiles = numFiles
        self.is_animating = False
        self.spriteIndex = 0
        self.spriteLeftList = []
        self.is_facing_left = False

        for i in range(self.numberOfFiles):
            myImage = pygame.image.load(self.fnamePrefix + "%01d" % i + ".png")
            if color != "NONE":
                self.spriteLeftList.append(self.getColorImage(myImage,color))
                self.spriteRightList = [pygame.transform.flip(image, True, False) for image in self.spriteLeftList]
            else:
                self.spriteLeftList.append(myImage)
                self.spriteRightList = [pygame.transform.flip(image, True, False) for image in self.spriteLeftList]
            
    def getNextImage(self):
        self.spriteIndex += 0.25

        if self.spriteIndex >= len(self.spriteLeftList):
            self.spriteIndex = 0
            self.is_animating = False
        if self.is_facing_left:
            return self.spriteLeftList[int(self.spriteIndex)]
        else: 
            return self.spriteRightList[int(self.spriteIndex)]

    def getColorImage(self,myImage,color):
        colorImage = pygame.Surface(myImage.get_size()).convert_alpha()
        colorImage.fill(color)
        myImage.blit(colorImage, (0,0), special_flags = pygame.BLEND_RGBA_MULT)
        return myImage
    
    def animate(self):
        self.is_animating = True

class Player(pygame.sprite.Sprite):
    speed = 10

    def __init__(self, pos_x, pos_y, color):
        super().__init__()
        self.walkingAnimation = AnimationData("spacemanwalk_",9,color)
        self.zombieWalkingAnimation = AnimationData("zombWalk_",9,color)
        self.jumpingAnimation = AnimationData("spacemanjump_",3,color)
        self.image = self.walkingAnimation.getNextImage()

        # Get the rectangle for this image
        self.rect = self.image.get_rect()

        # Use the passed-in values to set the initial position
        self.rect.topleft = [pos_x, pos_y]

    def moveX(self, direction):
        # Update direction based on movement
        if direction < 0:
            self.walkingAnimation.is_facing_left = False
        elif direction > 0:
            self.walkingAnimation.is_facing_left = True

        self.rect.move_ip(direction * self.speed, 0)
        self.rect = self.rect.clamp((0, 0, 640, 480))

    def moveY(self, direction):
        self.rect.move_ip(0, direction * self.speed)
        self.rect = self.rect.clamp((0, 0, 640, 480))

    def returnPos(self):
        return self.rect.x, self.rect.y

    def zombieMove(self,pos):
        pass

    def update(self):
        if self.walkingAnimation.is_animating:
           self.image = self.walkingAnimation.getNextImage()
        if self.jumpingAnimation.is_animating:
           self.image = self.jumpingAnimation.getNextImage()
        if self.zombieWalkingAnimation.is_animating:
            self.image = self.zombieWalkingAnimation.getNextImage()

    def jumpUp(self, step):
        self.rect.move_ip(0, -step)
        self.rect = self.rect.clamp((0, 0, 640, 480))

# Initialize the pygame environment
pygame.init()

# Create a clock for controlling the frame rate
clock = pygame.time.Clock()

# Set the screen dimensions
screen_width = 640
screen_height = 480

# Create the game screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sprite Animation")

# Create a sprite group to manage the player characters
moving_sprites = pygame.sprite.Group()

# Create player instances and add them to the sprite group
player = Player(0, 240,"NONE")
zombie = Player(40,360,pygame.Color(0,255,0))
moving_sprites.add([player, zombie])
jumpCounter = 0
jumpPause = 0

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Handle player input
    keystate = pygame.key.get_pressed()
    directionX = keystate[pygame.K_RIGHT] - keystate[pygame.K_LEFT]
    directionY = keystate[pygame.K_DOWN] - keystate[pygame.K_UP]

    playerJumped = keystate[pygame.K_j]
    if playerJumped and jumpPause <= 0:
        player.jumpingAnimation.animate()
        jumpCounter = 16
        jumpPause = 70

    if directionX != 0:
        player.walkingAnimation.animate()
        player.moveX(directionX)

    if directionY != 0:
        player.walkingAnimation.animate()
        player.moveY(directionY)

    if jumpCounter > 7.5 and jumpCounter < 16:
        jumpCounter -= 0.25
        player.jumpUp(15-jumpCounter)
    elif jumpCounter > 0 and jumpCounter < 16:
        jumpCounter -= 0.25
        player.jumpUp(jumpCounter-7.5)
    else: jumpCounter -= 0.5
    jumpPause-=1

    #capture player position
    playerPosX, playerPosY = player.returnPos()

    #zombie movement
    zombX, zombY = zombie.returnPos()
    zombX = playerPosX-zombX
    zombY = playerPosY-zombY
    if zombX > 23 or zombX < -23:
        zombie.zombieWalkingAnimation.animate()
    zombie.moveX(zombX*0.005)
    zombie.moveY(zombY*0.005)
    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the sprites on the screen
    moving_sprites.draw(screen)

    # Update the sprites
    moving_sprites.update()

    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)
