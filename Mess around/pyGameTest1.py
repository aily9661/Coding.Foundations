import pygame as py, random

#define objects
class player1:
    def __init__(self, SPos): #initialize object ALWAYS RAN
        self.position = SPos
        self.color = "blue"
        self.size = 30

class enemy:
    def __init__(self, SPos): #initialize object ALWAYS RAN
        self.position = SPos
        self.color = "red"
        self.size = 10
        self.vx = 10 # velocity x of object
        self.vy = 10 # velocity y of object

    def flipX(self):
        self.vx *= -1

    def flipX(self):
        self.vy *= -1

#basic init
py.init()
screen = py.display.set_mode((1280, 720))
clock = py.time.Clock()
running = True
dt = 0

SPos = py.Vector2(screen.get_width() / 2, screen.get_height() / 2)
player = player1(SPos)

e1SPos = screen.get_width() / 2 - random.randint(50,250), screen.get_height() / 2 + random.randint(50,250)
e2SPos = screen.get_width() / 2 + random.randint(50,250), screen.get_height() / 2 - random.randint(50,250)
e3SPos = screen.get_width() / 2 - random.randint(50,250), screen.get_height() / 2 - random.randint(50,250)
e4SPos = screen.get_width() / 2 + random.randint(50,250), screen.get_height() / 2 + random.randint(50,250)
e1 = enemy(e1SPos)
e2 = enemy(e2SPos)
e3 = enemy(e3SPos)
e4 = enemy(e4SPos)

enemyList = [e1,e2,e3,e4]


#all of program goes in while loop
while running:
    #allow user to quit
    for event in py.event.get(): 
        if event.type == py.QUIT:
            running = False

    screen.fill("black") #reset screen 

    py.draw.circle(screen, player.color, player.position, player.size) # draw player
    
    #draw enemies by manipulated v position
    for enemies in enemyList:
        py.draw.circle(screen, enemies.color, enemies.position, enemies.size)
    #e1.position.x += enemies.vx * dt
    #e1.position.y += enemies.vy * dt   

    #player movement
    keys = py.key.get_pressed()
    if keys[py.K_w]:
        player.position.y -= 300 * dt
    if keys[py.K_s]:
        player.position.y += 300 * dt
    if keys[py.K_a]:
        player.position.x -= 300 * dt
    if keys[py.K_d]:
        player.position.x += 300 * dt

    #draws things to screen
    py.display.flip() 

    #limits FPS to 60
    dt = clock.tick(60) / 1000