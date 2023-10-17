
import pygame 
  
pygame.init() 
  
color = (255,255,255) 
red = (255,0,0) 
blue = (0,0,255)
clock = pygame.time.Clock()
  
# CREATING CANVAS 
width, height = 500, 500
canvas = pygame.display.set_mode((width,height))
  
# TITLE OF CANVAS 
pygame.display.set_caption("Bouncing Squaes") 
  
exit = False

x = 250
y = 20
size = 60
xStep = 5
yStep = 5
shapeColor = red
FPS = 60
  
while not exit: 
    #canvas.fill(color) 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            exit = True
  
    pygame.draw.rect(canvas, shapeColor, pygame.Rect(x,y,size,size)) 
    if x >= width-size or x <= 0:
        xStep*=-1
        shapeColor = blue
    if y >= height-size or y <= 0:
        yStep*=-1
        shapeColor = red
    
    x+=xStep
    y+=yStep

    clock.tick(FPS)
    pygame.display.update() 