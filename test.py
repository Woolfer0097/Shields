import pygame,sys
from pygame import *
from pygame.locals import *


displayIndex = 0
pygame.init()



##standard 16:9 display ratios
DISPLAYS = [(1024,576),(1152,648),(1280,720),(1600,900),(1920,1080),(2560,1440)]
screen = pygame.display.set_mode(DISPLAYS[displayIndex])
screen.fill((0,0,0))
### change image path to a string that names an image you'd like to load for testing. I just used a smiley face from google image search.
### Put it in the same place as this file or set up your paths appropriately
imagePath = "./data/images/bg.png"



class Icon(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.smileyImage = pygame.image.load(imagePath)
        self.image = self.smileyImage.convert_alpha()
        ### need to assume a default scale, DISPLAYS[0] will be default for us
        self.rect = self.image.get_rect()
        self.posX = x
        self.posY = y
        self.rect.x = x
        self.rect.y = y
        self.defaultx = (float(self.rect[2])/DISPLAYS[0][0])*100
        self.defaulty = (float(self.rect[3])/DISPLAYS[0][1])*100
        ## this is the percent of the screen that the image should take up in the x and y planes



    def updateSize(self,):
        self.image = ImageRescaler(self.smileyImage,(self.defaultx,self.defaulty))
        self.rect = self.image.get_rect()
        self.rect.x = self.posX
        self.rect.y = self.posY



def ImageRescaler(image,originalScaleTuple): #be sure to restrict to only proper ratios
    newImage = pygame.transform.scale(image,(int(DISPLAYS[displayIndex][0]*(originalScaleTuple[0]/100)),
                                         int(DISPLAYS[displayIndex][1]*(originalScaleTuple[1]/100))))
    return newImage



def resizeDisplay():
    screen = pygame.display.set_mode(DISPLAYS[displayIndex])
    ## this is where you'd have'd probably want your sprite groups set to resize themselves
    ## Just gonna call it on icon here
    icon.updateSize()



icon = Icon(100,100)
while True:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()



        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                displayIndex -=1
                if displayIndex < 0:
                    displayIndex = 5
                resizeDisplay()
            elif event.key == K_RIGHT:
                displayIndex+=1
                if displayIndex > 5:
                    displayIndex = 0
                resizeDisplay()



    screen.blit(icon.image,(icon.rect.x,icon.rect.y))
    pygame.display.update()
