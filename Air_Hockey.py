#!/usr/bin/python2.7
#
# Air Hockey Game Ported to Python by aSilverDpad
#
# Released under the GNU General Public License

VERSION = '0.1'

try:
    import sys
    import random
    import math
    import os
    import getopt
    import pygame
    from socket import *
    from pygame.locals import *
except ImportError, err:
    print "couldn't load module. %s" % (err)
    sys.exit(2)

def load_png(name): # {{{1
    '''Load image and return object.
        looks for image in ./images
        Returns: image, image.rect.'''
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
        if image.get_alpha() is None: #Transparency
            image = image.convert()
        else:
            image = image.convert_alpha()
    except pygame.error, message:
        print 'Cannot load image:', fullname
        raise SystemExit, message
    return image, image.get_rect()
# }}}1
class Puck(pygame.sprite.Sprite): # {{{1
    '''A circle shaped hockey puck that will
    move across the screen when hit by the paddles.
    Returns: puck object
    Functions: ... ...
    Attributes: ... ...'''

    def __init__(self, (xy), vector): #{{{2
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_png('puck.png')
        screen = pygame.display.get_surface() #TODO: make global? in main()?
        self.moveable_area = screen.get_rect()
        self.vector = vector
        self.hit = 0



# }}}1
class Paddle(pygame.sprite.Sprite): # {{{1
    '''Movable hockey paddle with which to hit the puck
    Returns: paddle objects
    Functions:
    Attributes:  '''

    def __init__(self, side): # {{{2
            pygame.sprite.Sprite.__init__(self)
            self.image, self.rect = load_png('puck.png')
            screen = pygame.display.get_surface() #TODO: make global?
            self.moveable_area = screen.get_rect() # devide it in two later
            self.side = side
            self.speed = 10
            self.state = 'still'
            self.reinit()

# }}}1
def main(): # {{{1
    pygame.init()
    screen = pygame.display.set_mode((640,480))
    pygame.display.set_caption('Air Hockey')

    # Init clock
    clock = pygame.time.Clock()

    # Event loop
    while True:
        clock.tick(60) # 60 fps max

        for event in pygame.event.get():
            if event.type == QUIT:
                return

if __name__ == '__main__': main()
