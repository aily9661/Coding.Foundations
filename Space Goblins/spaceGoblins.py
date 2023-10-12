'''
Space goblins is a display of OOP. The program is a game reminiscent of spaceinvaders. The user must move their ship side to side
dodging goblins while firing bullets at them. The user gets a point for every goblin killed and proceeds to the next level upon killing
all the goblins. The goal of the game is to compelete all 5 levels and upon winning or losing the users score is saved to a high score
text file.
AUTHOR: Aidan Lynch
DATE: 12/1/2022
'''

import pygame, random, re
pygame.init()

# constants
w = 800
h = 800

# ====== loading pygame =====
win = pygame.display.set_mode((w, h))
clock = pygame.time.Clock() # clock for animation
font = pygame.font.Font(None, 25) # set font size
pygame.mixer.music.load('spaceSong.mp3') # royalty freemusic used for game from zapsplat

class Player(): # player class
    def __init__(self, pXPos, pYPos):
        self.x = pXPos # player x assigned to parameter
        self.y = pYPos # player y position assigned to paramter
        self.size = 50
        self.player = pygame.Rect(self.x,self.y,self.size,self.size/2)
        self.playerFace = pygame.Surface((self.size,self.size/2))
        self.step = 15
        spaceShipPic = 'spaceShip.gif' # ship image
        self.spaceShipScreen = pygame.image.load(spaceShipPic)  # loading the image on top of the game

    def show(self):
        win.blit(self.playerFace,(self.x,self.y))
        win.blit(self.spaceShipScreen, (self.x,self.y)) # draw spaaceship image

    def moveLeft(self):
        if self.x > 5:
            self.x -= self.step

    def moveRight(self):
        if self.x < h - 5:
            self.x += self.step

    def getPlayerPos(self):
        return self.x, self.y

    def hitbox(self): # returns a hitbox for self
        self.Hitbox = pygame.Rect(self.x,self.y, self.size, self.size)
        return self.Hitbox

class Bullet(): # bullet class for shooting
    def __init__(self, bXPos=-30, bYPos=0):
        self.color = (255,255,255) # bullet is white
        self.x = bXPos # player x assigned to parameter
        self.y = bYPos # player y position assigned to paramter
        self.size = 10
        self.bullet = pygame.Rect(self.x,self.y,self.size,self.size)
        self.bulletFace = pygame.Surface((self.size,self.size))
        self.bulletFace.fill(self.color)
        self.Ystep = 2

    def show(self):
        win.blit(self.bulletFace,(self.x,self.y))
        self.y -= 5

    def moveToPlayer(self, bXY):
        bXY = list(bXY) # change bullet pos into list
        self.x = bXY[0] + 22 # set x to player x offset by size
        self.y = bXY[1] - 12.5 # set y to player y offset by player size

    def hitbox(self):
        self.Hitbox = pygame.Rect(self.x,self.y, self.size, self.size)
        return self.Hitbox

    def bulletJump(self):
        self.y -= h*2

class Enemy(): # create enemy class
    def __init__(self, eXPos, eYPos, eHp):
        self.x = eXPos # enemy x assigned to parameter
        self.y = eYPos # enemy y assigned to parameter
        self.size = 25
        self.enemy = pygame.Rect(self.x,self.y,self.size,self.size)
        self.enemyFace = pygame.Surface((self.size,self.size))
        self.hp = eHp
        self.collision = 0 # tests if enemy has been collided with
        self.eXStep = 2
        self.eYStep = 1
        self.redPic = 'redGoblin.gif' # ship image
        self.redGobScreen = pygame.image.load(self.redPic)  # loading the image on top of the game
        self.purplePic = 'purpleGoblin.gif' # ship image
        self.purpleGobScreen = pygame.image.load(self.purplePic)  # loading the image on top of the game
        self.orangePic = 'orangeGoblin.gif' # ship image
        self.orangeGobScreen = pygame.image.load(self.orangePic)  # loading the image on top of the game
        self.death = False

    def show(self): # change color based on hp count, draw if h is > 0
        if self.hp > 0:
            win.blit(self.enemyFace,(self.x,self.y))
        if self.hp == 3 and self.hp > 0:
            win.blit(self.orangeGobScreen, (self.x,self.y)) # draw goblin image
        if self.hp == 2 and self.hp > 0:
            win.blit(self.redGobScreen, (self.x,self.y)) # draw goblin image
        if self.hp == 1 and self.hp > 0:
            win.blit(self.purpleGobScreen, (self.x,self.y)) # draw goblin image

    def enemyStartingPositions(self, eXPos, eYPos):
        self.x += eXPos
        self.y = eYPos

    def changeHP(self):
        self.hp -= 1 # change hp based off of return

    def currentHp(self):
        return self.hp

    def hitbox(self): # returns a hitbox for self
        self.Hitbox = pygame.Rect(self.x,self.y, self.size, self.size)
        return self.Hitbox

    def movement(self, yMove): # move down and bounce agaist sides
        if self.x < 10:
            self.eXStep *= -1
        if self.x > w - 10:
            self.eXStep *= -1 
        self.x += self.eXStep
        if yMove: # if y movement is on
            if self.y < h - 20 : # if enemies are above bottom of screen
                self.y += self.eYStep/4

    def hpBelowZero(self): # tracks when all enemies have been killed
        if self.hp > 0:
            return 0 
        else:
            return 1

    def dead(self): # lets you know if enemy is dead
        if self.hp <= 0 and self.death == False:
            self.death = True
            return 1
        elif self.death == True:
            return 0
        elif self.death == False:
            return 0

    def enemyJump(self):
        self.x -= w*100

    def enemyMovementChangeX(self):
        if self.x > 50 and self.x < w - 50:
            self.eXStep *= -1

    def enemyMovementChangeY(self, step):
        if self.y < h - self.size:
            self.y += step

class Backdrop():# class for backgrond
    def __init__(self):
        self.starPic = 'starBack.gif'
        self.backdropScreen = pygame.image.load(self.starPic)  # loading the image on top of the game
        self.y = 0
        self.step = 0.5

    def show(self):
        win.blit(self.backdropScreen,(0,self.y))

    def yChange(self):
        self.y -= self.step


def main(points, yTimer = 0, randomEnemyMovement = 0): # y timer defines when enemies drop randomy enemy movement determines enemy movement by level
    # =============== define constants ====================
    running = True
    bulletCounter = 0 # chooses bullet to display
    reload = 0 # reload variable to prevent spam firing
    reloadTimer = 0 # timer for reload animation
    reloading = False # determines whether reloading is happening
    eYPos = 30 # temp enemy y position
    eXPos = 0 # temp enemy y position
    eT3Hp = 1
    eT2Hp = 2
    eT1Hp = 3
    yMove = False # enemies dont move by y initially

    # ================= player objects and backdrop ==================
    background = Backdrop()
    player = Player(w/2, h - 40) # player starting x and y positions

    #================ define enemy objects and set starting positions ==========
    enemyT1List = []
    enemyT2List = []
    enemyT3List = []
    for enemyi in range(10):
        enemyT1List.append(Enemy(eXPos,eYPos,eT1Hp)) # append tiered enemy lists based off of starting hhealth
        enemyT2List.append(Enemy(eXPos,eYPos,eT2Hp))
        enemyT3List.append(Enemy(eXPos,eYPos,eT3Hp))

    for enemyT1 in range(len(enemyT1List)):
        eXPos += w/11 # space out enemies along screen
        enemyT1List[enemyT1].enemyStartingPositions(eXPos, eYPos) # move t1 enemies using starting position using function
        enemyT2List[enemyT1].enemyStartingPositions(eXPos, eYPos=70) # move T2 enemies using starting position using function
        enemyT3List[enemyT1].enemyStartingPositions(eXPos, eYPos=110) # move T3 enemies using starting position using function

    # ================= define and list bullet objects =================
    bulletList = []
    for bulleti in range(15):
        bulletList.append(Bullet())

    # =============== game loop ===================
    while running:
        win.fill((0,0,0)) #reset screen to black

        # =========== move background ===========
        background.show()
        background.yChange()

        # ============= pygame events ==============
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT: # move player right
                        player.moveRight()
                    if event.key == pygame.K_LEFT: # move player left
                        player.moveLeft()

                    if event.key == pygame.K_SPACE and reload < len(bulletList): # shoot bullet on space press if ammo is left
                        bXY = player.getPlayerPos()
                        bulletList[bulletCounter].moveToPlayer(bXY)
                        bulletCounter += 1 # move to next bullet
                        reload += 1
                        if bulletCounter >= len(bulletList):
                            bulletCounter = 0 # reset bullet counter after reaching max list 
                    

        # ================== reload animation and bullet count display ===========
        if reload >= len(bulletList) and reloading == False:
            reloadTimer = 100 # simulates 2 seconds base on clock tick
            reloading = True

        if reloadTimer == 0:
            reload = 0 # set reload to 0 upon timer reach
            reloading = False # set reloading to false

        if reloading == True:
            win.blit(font.render(f'Reloading...', True, (255,255,255)), (10, h-30)) # show reloading upon ammo run out
        else:
            win.blit(font.render(f'Ammo: {15 - bulletCounter}', True, (255,255,255)), (10, h-30)) # location for text) # show ammo left
        
        # ================= bullet enemy collision detection and player collision detection ==============
        enemyList = enemyT1List + enemyT2List + enemyT3List # concatenate enemy objects into one list
        playerHitbox = player.hitbox() # sets player hitbox

        for bulletSeries in range(len(bulletList)): # tests if bullet hitboxes collide with T1 enemy hitboxes
            bulletHitbox = bulletList[bulletSeries].hitbox()
            for enemySeries in range(len(enemyList)):
                enemyHitbox = enemyList[enemySeries].hitbox()
                if pygame.Rect.colliderect(enemyHitbox, bulletHitbox) == True: # if enemy hasnt been collided with recently update health
                    enemyList[enemySeries].changeHP() 
                    bulletList[bulletSeries].bulletJump() # remove bullet

                if pygame.Rect.colliderect(enemyHitbox, playerHitbox) == True and enemyList[enemySeries].currentHp() > 0: # if enemy has health and touches player initate game loss
                    running = False
                    gameLoss(points)

                if enemyList[enemySeries].dead() == 1: # points go up if enemy has just been killed
                    points += 1
        
        # =========== enemy movement =========
        if yTimer == 1200:
            yMove = True
        for eMovement in range(len(enemyList)):
            enemyList[eMovement].movement(yMove)

        if randomEnemyMovement == 1: # ENEMY RANDOMZIER FOR LEVEL 2
            for enemyXChange in range(len(enemyList)):
                diceRoll = random.randint(1,64)
                if diceRoll == 1:
                    enemyList[enemyXChange].enemyMovementChangeX()
                if diceRoll == 2:
                    enemyList[enemyXChange].enemyMovementChangeY(0.5)

        if randomEnemyMovement == 2: # ENEMY RANDOMZIER FOR LEVEL 3
            for enemyXChange in range(len(enemyList)):
                diceRoll = random.randint(1,72)
                if diceRoll == 1:
                    enemyList[enemyXChange].enemyMovementChangeX()
                if diceRoll == 2 or diceRoll == 4:
                    enemyList[enemyXChange].enemyMovementChangeY(0.5)

        if randomEnemyMovement == 3: # ENEMY RANDOMZIER FOR LEVEL 4
            for enemyXChange in range(len(enemyList)):
                diceRoll = random.randint(1,72)
                if diceRoll == 1:
                    enemyList[enemyXChange].enemyMovementChangeX()
                if diceRoll == 2 or diceRoll == 4:
                    enemyList[enemyXChange].enemyMovementChangeY(1)

        if randomEnemyMovement == 4: # ENEMY RANDOMZIER FOR LEVEL 5
            for enemyXChange in range(len(enemyList)):
                diceRoll = random.randint(1,96)
                if diceRoll == 1:
                    enemyList[enemyXChange].enemyMovementChangeX()
                if diceRoll == 2 or diceRoll == 4 or diceRoll == 6:
                    enemyList[enemyXChange].enemyMovementChangeY(1.5)


        # =============== show enemies and player and bullets =============
        player.show()
        for enemyShowT1 in range(len(enemyT1List)):
            enemyT1List[enemyShowT1].show() # show all T1 enemies
            enemyT2List[enemyShowT1].show() # show all T2 enemies
            enemyT3List[enemyShowT1].show() # show all T3 enemies
            
        for bullet in range(len(bulletList)): # go through bullet list and show bullets 
            bulletList[bullet].show()

        # ================= update ==============
        reloadTimer -= 1 # reduce reload timer
        yTimer += 1
        clock.tick(60)
        pygame.display.update()

        # ================== track level completion =================
        enemyDeathCount = 0
        for enemyDeath in range(len(enemyList)):
            enemyDeathCount += enemyList[enemyDeath].hpBelowZero()
            if enemyList[enemyDeath].hpBelowZero() > 0:
                enemyList[enemyDeath].enemyJump()
        if enemyDeathCount == len(enemyList):
            running = False
    return points # return player current point total)

def digitCheck(user):
  return any(char.isdigit() for char in user) # checks if username contains digits used from thefourtheye on stackoverflow

# ============= define game loss =========
def gameLoss(points, won=False):
    # ========== propmpt user to enter username ===========
    win.fill((0,0,0))
    win.blit(font.render(f'Enter your username in the terminal', True, (255,255,255)), (50,h/2)) # user enter game prompt
    pygame.display.update()
    # =============== make a list of player scores and list of scores ===========
    newHighScore = open('highscores.txt', 'r')
    highScoreList = [] # create list for saving high scores
    line = 0 
    highScoreListCheck = [] # create list for checking high scores
    while line != '': # fill high score list with items from txt
        line = newHighScore.readline()
        line = line.rstrip('\n')
        check = str(line)
        if line != '': 
            highScoreList.append(check)
        score = re.sub('\D', '', check)
        if line != '': # create a list of just the values from highscore txt
            highScoreListCheck.append(score)
    newHighScore.close()

    #=========== test if new high score and replace score if such ===============
    for scoreCheck in range(len(highScoreList)): # run through high score numbers until a value less than user score is found
        scoreChecker = highScoreListCheck[scoreCheck]
        if points > int(scoreChecker):
            correct = False # check for alpha in user
            while correct == False: # if user has a new high score replace the spot with the new value
                user = input('Congrats on the new high score? What is your username: ')
                if digitCheck(user) == True: # ensure user only uses alpha characters in username
                    print('Only alpha chracters are allowed')
                else: 
                    correct = True
            newUser = user + ' ' + str(points) # replace highscore list with updated scores
            highScoreList.insert(scoreCheck, newUser) # insert new high score into list
            highScoreList.pop(len(highScoreList)-1) # remove the last element in the list
            break

    # ========= overwrite high scores ==========
    outfile = open('highscores.txt', 'w') # write new high scores from list to highscore txt
    for writing in range(len(highScoreList)):
        if writing < len(highScoreList) - 1:
            outfile.write(highScoreList[writing] + '\n')
        else:
            outfile.write(highScoreList[writing])

    outfile.close()

    running = True
    while running: # display win vs. loss txt, and updated high scores
        win.fill((0,0,0))
        textDrop = 30

        for event in pygame.event.get():
                # ========= Add events here ========= 
                if (event.type == pygame.QUIT):
                    pygame.quit()
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0]:      
                        pygame.quit()
        if won == True:                    
            win.blit(font.render(f'Wow you actually beat the game! Click on the x to leave the game', True, (255,255,255)), (50,h/2 - 90)) # game rules
        else:
            win.blit(font.render(f'Aw man you lose! Click on the x to leave the game', True, (255,255,255)), (50,h/2 - 90)) # game rules
        win.blit(font.render(f'Your final score {points}', True, (255,255,255)), (50,h/2 - 60)) # user enter game prompt
        win.blit(font.render(f'Top scores', True, (255,255,255)), (50,h/2 - 30)) # alternative close
        win.blit(font.render(f'==========', True, (255,255,255)), (50,h/2)) # alternative close
        for highscore in range(len(highScoreList)):
            win.blit(font.render(highScoreList[highscore], True, (255,255,255)), (50,h/2 + textDrop)) # alternative close
            textDrop += 30
        pygame.display.update()

# =============== run the program ==============
def startScreen(gameStart): #game Start screen
    pygame.mixer.music.play() # start music
    while gameStart:
        gsScreen = pygame.display.set_mode((w, h))
        GameStartPic = 'spaceGoblinsTitle.gif' # image that will show up if you lose the game
        GameStartScreen = pygame.image.load(GameStartPic)  # loading the image on top of the game
        gsScreen.blit(GameStartScreen,(0,0)) # making the loaded image appear'''
        pygame.display.update()
        for GSevent in pygame.event.get():
            if GSevent.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0]:    
                        gameStart = False
                        # continues on mouse press

gameStart = True
startScreen(gameStart)
points = 0
points += main(points)

def levelStart(points): # level initiate page
    yTimer = 50
    levelDifficulty = 1
    for i in range(4):
        running = True
        while running:
            win.fill((0,0,0))

            for event in pygame.event.get():
                    # ========= Add events here ========= 
                    if (event.type == pygame.QUIT):
                        pygame.quit()
                    
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if pygame.mouse.get_pressed()[0]:      
                            running = False
                                
            win.blit(font.render(f'Nice job passing level {levelDifficulty}! ', True, (255,255,255)), (50,h/2 - 30)) # game rules
            win.blit(font.render(f'Click on the screen to start level {levelDifficulty+1}', True, (255,255,255)), (50,h/2)) # user enter game prompt
            win.blit(font.render(f'Score {points}', True, (255,255,255)), (50,h/2 + 30)) # alternative close
            pygame.display.update()  
        points = main(points, yTimer, levelDifficulty)
        yTimer += 50
        levelDifficulty += 1
    return points

points = levelStart(points)

if points >= 150:
    won = True # if user gets to this point they have won the game
gameLoss(points, won)