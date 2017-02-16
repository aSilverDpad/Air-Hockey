#!/usr/bin/python2.7

VERSION = "0.2"

try:
    import sys
    import os
    import pygame
except ImportError, err:
    print "couldn't load module. %s" % (err)
    sys.exit(2)

def load_png(name): # {{{1
    """ Load image and return image object"""
    fullname = os.path.join('images', name)
    try:
        image = pygame.image.load(fullname)
        if image.get_alpha() is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
    except pygame.error, message:
        print 'Cannot load image:', fullname
        raise SystemExit, message
    return image, image.get_rect()

class Puck(pygame.sprite.Sprite): # {{{1
    '''A Hockey puck that moves around the screen
    Returns: puck object
    Functions:
    Attributes:'''

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_png('puck.png')
        self.vector = [1,1]


def main(): #{{{1
    pygame.init()
    size = width, height = 800, 500
    black = 0,0,0

    screen = pygame.display.set_mode(size)

    pygame.mouse.set_pos(0,0)
    paddle, paddlerect = load_png('bluepaddle.png')
    puck = Puck()
    pucksprite = pygame.sprite.RenderPlain(puck)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        puck.rect = puck.rect.move(puck.vector)
        paddlerect = paddlerect.move(pygame.mouse.get_rel())

        # puck - wall collition
        if puck.rect.left < 0 or puck.rect.right > width:
            puck.vector[0] = -puck.vector[0]
        if puck.rect.top < 0 or puck.rect.bottom > height:
            puck.vector[1] = -puck.vector[1]
        # paddle - puck collition
        if puck.rect.colliderect(paddlerect) == 1:
            puck.vector[0] = -puck.vector[0]

        screen.fill(black)
        screen.blit(screen, puck.rect)
        screen.blit(paddle, paddlerect)
        pucksprite.update()
        pucksprite.draw(screen)
        pygame.display.flip()

if __name__ == '__main__': main()
