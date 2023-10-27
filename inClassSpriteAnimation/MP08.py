import pygame
class AnimationData():
    def __init__(self,fname_prefix,numFiles,color):
        self.fnamePrefix = fname_prefix
        self.numberOfFiles = numFiles
        self.is_animating = False
        self.spriteIndex = 0
        self.spriteList = []

        for i in range(self.numberOfFiles):
            myImage = pygame.image.load(self.fnamePrefix + "%01d" % i + ".png")
            if color != "NONE":
                self.spriteList.append(self.getColorImage(myImage,color))
            else:
                self.spriteList.append(myImage)
            
    def getNextImage(self):
        self.spriteIndex += 0.25

        if self.spriteIndex >= len(self.spriteList):
            self.spriteIndex = 0
            self.is_animating = False

        return self.spriteList[self.spriteIndex]

    def getColorImage(self,myImage,color):
        colorImage = pygame.Surface(myImage.get_size()).convert_alpha()
        colorImage.fill(color)
        myImage.blit(colorImage, (0,0), special_flags = pygame.BLEND_RGBA_MULT)
        return myImage
    
    def animate(self):
        self.is_animating = True