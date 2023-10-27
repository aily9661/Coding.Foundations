class AnimationData():
    def __init__(self,fname_prefix,numFiles,color):
        self.fnamePrefix = fname_prefix
        self.numberOfFiles = numFiles
        self.is_animating = False
        self.spriteIndex = 0
        self.spriteList = []

        for i in range(self.numberOfFiles):
            <load an image> #use self.fnamePrefix in place of hardcoded string to build fname
            <if color != NONE>
                <add self.spriteList(getColorImage(myImage,color))
            <else>
                <add self.spriteList(myImage)>
            
    def getNextImage(self):
        <use the update() code from last week but using the above properties>
        return <image> #return the image rather than assign to self.image
                       #that will still happen in the Player update() method

    def getColorImage()
        <use getColorImage() from previous code>
        return <image>
    
    def animate(self):
        self.is_animating = True