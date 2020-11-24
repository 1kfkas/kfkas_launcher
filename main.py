# Check operational system

import sys, platform

type = platform.system()

if(type == "Windows"):
    print("\nThe program is gonna start in a few seconds\n")
else:
    sys.exit("\nSorry, our program don't have support for your system\n")

# Program

import pygame, math, subprocess
from pygame.locals import *

pygame.init()

display = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Menu')

clock = pygame.time.Clock()

# Path to Sprites

path = './System/'

# Background Color

hue = 0

# Mouse Variable

mouseSprite = pygame.image.load(path+'Mouse.png')
mousePos = pygame.mouse.get_pos()
pygame.mouse.set_visible(False)

# Cloud Variable

cloudSprite = pygame.image.load(path+'Cloud.png')
cloudWidth, cloudHeight = cloudSprite.get_rect().size
cloudX, cloudY = (128, 128)

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

    if keys[K_U]:
        subprocess.run("python update.py")
        sys.exit()

    # Change Background Color

    color = pygame.Color(0)
    color.hsla = (hue, 100, 40, 50)
    hue = hue + 0.05

    if(hue > 360):
        hue = 0
    
    display.fill(color)

    # Draw Cloud

    if getCollision(mousePos, (cloudX+cloudWidth/2, cloudY+cloudHeight/2), 32):
        display.blit(cloudSprite, (cloudX, cloudY))
    else:
        display.blit(cloudSprite, (cloudX, cloudY))

    # Draw Mouse

    display.blit(mouseSprite, mousePos)

    pygame.display.flip()
