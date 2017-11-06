import pygame
from pygame.locals import *
from random import randint
import time

pygame.init()

##import os
##
##os.environ['VIDEO_WINDO_POS'] = "5,5"

score = 0
lives = 1

sw = 800
sh = 600
screenSize = [sw, sh]
screen = pygame.display.set_mode(screenSize)
pygame.display.set_caption("Mario's Revenge!")

clock = pygame.time.Clock()

white  = (255, 255, 255)
black  = (  0,   0,   0)
red    = (255,   0,   0)
green  = (  0, 255,   0)
blue   = (  0,   0, 255)
purple = (180,   0, 180)
yellow = (255, 255,   0)
brown =  (125,  42,  42)

allSprites = pygame.sprite.Group()

class DonkeyKong(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Donkey_Kong.gif")
        self.image = pygame.transform.scale(self.image,(100,100))
        self.rect = self.image.get_rect()

class Barrel(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("DKBarrel.gif")
        self.image = pygame.transform.scale(self.image,(100,100))
        self.rect = self.image.get_rect()

class FireBall(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Fireball.gif")
        self.image = pygame.transform.scale(self.image,(35,25))
        self.rect = self.image.get_rect()


# Begins Donkey Kong code:

def pollKeys():
    global kong
    keys = pygame.key.get_pressed()
    if keys[K_RIGHT]:
        kong.rect.x += 5
    if keys[K_LEFT]:
        kong.rect.x -= 5
    if keys[K_UP]:
        kong.rect.y -= 20
    if keys[K_DOWN]:
        kong.rect.y += 5   
    if kong.rect.x >= 700:
        kong.rect.x = 1
    if kong.rect.x <= 0:
        kong.rect.x = 700
    if kong.rect.y >= 500:
        kong.rect.y = 500

kong = DonkeyKong()
kong.rect.x = 300
kong.rect.y = 500

allSprites.add(kong)

# End of Donkey Kong code.

# Begins Barrel code:

barrels = pygame.sprite.Group()

for i in range(0, 10):
    barrel = Barrel()
    barrel.rect.x = randint(10, sw-10)
    barrel.rect.y = randint(10, sh-10)
    barrels.add(barrel)
    allSprites.add(barrel)

# End of Barrel code.

# Begins FireBall code:
### NOTE ###
# The fireball code is within the for loops so they can spawn faster or slower depending \
# on the difficulty.

fireballs = pygame.sprite.Group()

# End of FireBall code.



# Process/Run code:

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pollKeys()

# Change difficulty here in this range(0, 1) to make it more frequent.
# The fire.rect.y += 2 can also be changed to increase or decrease the fireball speed.

    for i in range(0, 1):
        fire = FireBall()
        fire.rect.x = randint(0, sw*14)
        fireballs.add(fire)
        allSprites.add(fire)

    for fire in fireballs:
        fire.rect.y += 2
        fireballs.add(fire)

# Collision code:

    collideList = pygame.sprite.spritecollide(kong, barrels, True)
    for barrel in collideList:
        allSprites.remove(barrel)
        barrels.remove(barrel)
        funsound = pygame.mixer.Sound("doABarrelRoll.wav")
        funsound.play()
        score = score + 1
        
    collideList = pygame.sprite.spritecollide(kong, fireballs, True)
    for fire in collideList:
        lives = 0


# Draw screen visual:
    screen.fill(white)

    allSprites.draw(screen)

# Draws sentences on the screen. You can use these for "Score" or anything text related.
    font = pygame.font.Font(None, 40)
    text = font.render("Lives: %d" % lives, True, red)
    screen.blit(text, [675, 50])

    font = pygame.font.Font(None, 40)
    text = font.render("Score: %d" % score, True, red)
    screen.blit(text, [675, 0])

    if score == 10:
        fire.remove(fireballs)
        font = pygame.font.Font(None, 25)
        text = font.render("YOU WIN!! Your final score was a whopping %d points! \
Press the Spacebar to exit." % score, True, red)
        screen.blit(text, [55, 400])
        keys = pygame.key.get_pressed()
        if keys[K_SPACE]:
            done = True

    if lives == 0:
        kong.rect.x = 300
        kong.rect.y = 500
        font = pygame.font.Font(None, 25)
        text = font.render("YOU LOSE!! Your final score was a whopping %d points.. \
Press the Spacebar to exit." % score, True, red)
        screen.blit(text, [50, 480])
        keys = pygame.key.get_pressed()
        if keys[K_SPACE]:
            done = True
    
    pygame.display.flip()
    clock.tick(20)

pygame.quit()

# pellets.rect.x = randint(sw, sw + 0.5 * sw)

# bg = pygame.image.load("bg.jpg")
# ret = bg.get_rect()
# screen.blit(bg, ret)
