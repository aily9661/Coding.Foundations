import pygame
class AnimationData():
    def __init__(self,fname_prefix,numFiles, color):
        self.fname_prefix = fname_prefix
        self.numFiles = numFiles
        self.isAnimating = False
        self.spriteIndex = 0
        self.spriteList = []

        for i in range(numFiles):
            if color != "NONE": self.spriteList.append(pygame.image.load(fname_prefix + '%01d' % i +'.png'))
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
