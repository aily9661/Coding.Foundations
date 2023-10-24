import pygame
import sys

class Player(pygame.sprite.Sprite):
    speed = 10

    def __init__(self, pos_x, pos_y):
        super().__init__()

        # Initialize animation flags
        self.is_animating = False
        self.is_jumping = False

        # Lists for storing images
        self.sprites_left = [pygame.image.load('spacemanwalk_' + str(i) + '.png') for i in range(9)]
        self.sprites_right = [pygame.transform.flip(image, True, False) for image in self.sprites_left]
        self.jumpSprites = [pygame.image.load('spacemanjump_' + str(i) + '.png') for i in range(3)]

        # Initialize current sprite, direction, and image
        self.current_sprite = 0
        self.current_jumpSprite = 0
        self.is_facing_left = False
        self.image = self.sprites_left[self.current_sprite]

        # Get the rectangle for this image
        self.rect = self.image.get_rect()

        # Use the passed-in values to set the initial position
        self.rect.topleft = [pos_x, pos_y]

    def moveX(self, direction):
        # Update direction based on movement
        if direction < 0:
            self.is_facing_left = False
        elif direction > 0:
            self.is_facing_left = True

        self.rect.move_ip(direction * self.speed, 0)
        self.rect = self.rect.clamp((0, 0, 640, 480))

    def moveY(self, direction):
        self.rect.move_ip(0, direction * self.speed)
        self.rect = self.rect.clamp((0, 0, 640, 480))

    def update(self):
        self.runAnimationBasic()
        self.runAnimationJump()

    def runAnimationBasic(self):
        if self.is_animating:
            self.current_sprite += 0.25

            if self.current_sprite >= len(self.sprites_left):
                self.current_sprite = 0
                self.is_animating = False

            # Set self.image based on direction
            if self.is_facing_left:
                self.image = self.sprites_left[int(self.current_sprite)]
            else:
                self.image = self.sprites_right[int(self.current_sprite)]
        else: self.image = self.jumpSprites[0]

    def runAnimationJump(self):
        if self.is_jumping:
            self.current_jumpSprite += 0.1

            if self.current_jumpSprite >= len(self.jumpSprites):
                self.current_jumpSprite = 0
                self.is_jumping = False

            self.image = self.jumpSprites[int(self.current_jumpSprite)]

    def animate(self):
        self.is_animating = True

    def animateJump(self):
        self.is_jumping = True

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
player = Player(0, 240)
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

    jumped = keystate[pygame.K_j]

    if jumped:
        if jumpPause < 0:
            player.animateJump()
            jumpCounter = 25
            jumpPause = 25            

    if directionX != 0:
        player.animate()
        player.moveX(directionX)

    #if directionY != 0:
        #player.animate()
        #player.moveY(directionY)

    if jumpCounter > 7.5 and jumpCounter < 16:
        jumpCounter -= 0.25
        player.jumpUp(15-jumpCounter)
    elif jumpCounter > 0 and jumpCounter < 16:
        jumpCounter -= 0.25
        player.jumpUp(jumpCounter-7.5)
    else: jumpCounter -= 0.5
    jumpPause-=1
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
