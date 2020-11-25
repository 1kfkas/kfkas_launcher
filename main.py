# Check operational system

import sys, platform

type = platform.system()

if(type == "Windows"):
    print("\nThe program is gonna start in a few seconds\n")
else:
    sys.exit("\nSorry, our program don't have support for your system\n")

# Program

import pygame, math, subprocess, requests, os, shutil
from pygame.locals import *

pygame.init()

display = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Menu')

clock = pygame.time.Clock()

loading = False

# Path to Sprites

path = './System/'

# Background Variables

hue = 0
bgSprite = pygame.image.load(path+'Background.png')
bgSprite2 = bgSprite.copy()
bgX = 0
bgXAngle = 0
bgYStart = -200
bgY = bgYStart
bgYAngle = 0

# Mouse Variable

mouseSprite = pygame.image.load(path+'Mouse.png')
print(mouseSprite)

mousePos = pygame.mouse.get_pos()
pygame.mouse.set_visible(False)

# Cloud Variable

cloudSprite = pygame.image.load(path+'Cloud.png')
cloudWidth, cloudHeight = cloudSprite.get_rect().size
cloudX, cloudY = (128, 128)

# Update Variable

updateSprite = pygame.image.load(path+'Update.png')
updateWidth, updateHeight = updateSprite.get_rect().size
updateX, updateY = (256, 128)

# Defs

def getCollision(pos1, pos2, size):

    distance = math.dist(pos1, pos2)

    if distance <= size:
        return True
    else:
        return False

while True:

    # Close Game

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    clock.tick(60)

    # Step Variables

    mousePos = pygame.mouse.get_pos()

    keys = pygame.key.get_pressed()
    
    if keys[K_ESCAPE]:
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

    #if getCollision(mousePos, (cloudX+cloudWidth/2, cloudY+cloudHeight/2), 32):
    display.blit(cloudSprite, (cloudX, cloudY))

    # Draw Update

    if getCollision(mousePos, (updateX+updateWidth/2, updateY+updateHeight/2), 32):
        url = "https://raw.githubusercontent.com/JaoKFkas/kfkas_launcher/main/System/update.py"
        r = requests.get(url)
        open('update.py', 'wb').write(r.content)

        subprocess.run("python update.py")
        pygame.quit()
        sys.exit()
    
    display.blit(updateSprite, (updateX, updateY))

    # Draw Background

    bgX+=1

    if bgX > 800:
        bgX = 0

    bgXAngle += 0.01

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
    display.blit(pygame.transform.rotate(bgSprite, math.cos(bgXAngle)), (bgX, bgY))
    display.blit(pygame.transform.rotate(bgSprite, math.cos(bgXAngle)), (bgX-800, bgY))

    # Draw Mouse

    display.blit(mouseSprite, mousePos)

    print(clock.get_fps())

    pygame.display.flip()
