# Check operational system

import sys, platform

type = platform.system()

if(type == "Windows"):
    print("\nThe program is gonna start in a few seconds\n")
else:
    sys.exit("\nSorry, our program don't have support for your system\n")

# Version
 
version="0.0.2"

# Program

import pygame, math, subprocess, requests, os, shutil
from pygame.locals import *

pygame.init()

display = pygame.display.set_mode((800, 600))
pygame.display.set_caption('KFkas Launcher')

clock = pygame.time.Clock()

loading = False

exists = os.path.exists

# Path to Sprites

pathS = './System/Sprites/'

# Path to Sounds

pathM = './System/Sounds/'

# Background Variables

hue = 0

bgSprite = False

if exists(pathS+'Background.png'):
    bgSprite = pygame.image.load(pathS+'Background.png')

bgX = 0
bgXAngle = 0

bgYStart = -200
bgY = bgYStart
bgYAngle = 0

# Mouse Variable

mouseSprite = False

if exists(pathS+'Mouse.png'):
    mouseSprite = pygame.image.load(pathS+'Mouse.png')

mousePos = pygame.mouse.get_pos()

if mouseSprite != False:
    pygame.mouse.set_visible(False)

# Cloud Variable

cloudSprite = False

if exists(pathS+'Cloud.png'):
    cloudSprite = pygame.image.load(pathS+'Cloud.png')
    cloudWidth, cloudHeight = cloudSprite.get_rect().size

cloudX, cloudYStart = (128, 256)
cloudY = cloudYStart

# Update Variable

updateSprite = False

if exists(pathS+'Exit.png'):
    updateSprite = pygame.image.load(pathS+'Update.png')
    updateWidth, updateHeight = updateSprite.get_rect().size

updateX, updateYStart = (256, 256)
updateY = updateYStart

# Exit Variable

exitSprite = False

if exists(pathS+'Exit.png'):
    exitSprite = pygame.image.load(pathS+'Exit.png')

exitWidth, exitHeight = exitSprite.get_rect().size
exitX, exitY = (700, 500)
exitAlpha = 0

# Version Variable

versionSprite = False

if exists(pathS+'Version.png'):
    versionSprite = pygame.image.load(pathS+'Version.png')

versionPos = (30, 500)

# Defs

def getCollision(pos1, pos2, size):

    distance = math.dist(pos1, pos2)

    if distance <= size:
        return True
    else:
        return False

# Create Event

close = False

#pygame.mixer.music.load(pathM+'Hotline.mp3')
#pygame.mixer.music.play(loops=1, start=0.0, fade_ms = 10000)

while True:

    # Close Game

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loading = True
            close = True

    clock.tick(60)

    # Step Variables

    mousePos = pygame.mouse.get_pos()

    keys = pygame.key.get_pressed()
    mouses = pygame.mouse.get_pressed()
    
    if keys[K_ESCAPE] and not loading:
        loading = True
        close = True

    if close and loading and bgYStart <= -200:
        pygame.quit()
        sys.exit()

    # Change Background Color

    color = pygame.Color(0)
    color.hsla = (hue, 100, 40, 50)
    hue += 0.2

    if(hue > 360):
        hue = 0
    
    display.fill(color)

    # Draw Cloud

    if getCollision(mousePos, (cloudX+cloudWidth/2, cloudY+cloudHeight/2), 32) and mouses[0]:
        subprocess.run("python ./Cloud/fileSynch.py")

    cloudY = cloudYStart - bgYStart/5

    if cloudSprite != False:
        display.blit(cloudSprite, (cloudX, cloudY))

    # Draw Update

    #if getCollision(mousePos, (updateX+updateWidth/2, updateY+updateHeight/2), 32):
    #    url = "https://raw.githubusercontent.com/JaoKFkas/kfkas_launcher/main/System/update.py"
    #    r = requests.get(url)
    #    open('update.py', 'wb').write(r.content)

    #    subprocess.run("python update.py")
    #    pygame.quit()
    #    sys.exit()

    updateY = updateYStart - bgYStart/5

    display.blit(updateSprite, (updateX, updateY))

    # Draw Background

    bgX+=1

    if bgX > 800:
        bgX = 0

    bgXAngle += 0.05

    if bgXAngle > 10:
        bgXAngle = -10

    if loading:
        if bgYStart > -200:
            bgYStart-=10
    else:
        if bgYStart < 300:
            bgYStart+=10

    if not loading:
        bgYAngle += 1
    bgY = bgYStart + math.sin(bgYAngle/100)*32

    pygame.draw.rect(display, (0, 30, 60), (0, bgY+150, 800, 700))

    if bgSprite != False:
        display.blit(pygame.transform.rotate(bgSprite, math.cos(bgXAngle)), (bgX, bgY))
        display.blit(pygame.transform.rotate(bgSprite, math.cos(bgXAngle)), (bgX-800, bgY))

    # Draw Exit

    if exitAlpha >= 1 and exitSprite != False:
        if getCollision(mousePos, (exitX+exitWidth/2, exitY+exitHeight/2), 32) and mouses[0]:
            loading = True
            close = True

    if loading:
        if exitAlpha >= 0:
            exitAlpha-=0.05
    else:
        if bgYStart >= 300 and exitAlpha < 1:
            exitAlpha+=0.01

    if exitSprite != False:
        exitSprite.set_alpha(exitAlpha*1000)
        display.blit(exitSprite, (exitX, exitY))

    # Draw Version

    if versionSprite != False:
        display.blit(versionSprite, versionPos)

    # Draw Mouse

    if mouseSprite != False:
        display.blit(mouseSprite, mousePos)

    print(clock.get_fps())

    pygame.display.flip()
