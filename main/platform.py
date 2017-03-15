__author__ = 'Andy'

"""
This module will take care of all the image loading for each level and pass it to the
specified level.
"""
import pygame
import os

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


class Platform(pygame.sprite.Sprite):
    """ Platform where the walls are created """


    def __init__(self):
        super().__init__()

        wall = os.path.join(os.path.dirname(__file__), os.pardir, 'images/wall.png')
        self.image = pygame.image.load(wall).convert()

        # Set the color that should be transparent
        self.image.set_colorkey(pygame.Color(0, 0, 0))
        self.rect = self.image.get_rect()



class Spike(pygame.sprite.Sprite):
    """ Platform will load the spike on the level on different position"""

    def __init__(self):
        """ Loading the spike. """
        super().__init__()
        spike = os.path.join(os.path.dirname(__file__), os.pardir, 'images/s1.png')
        self.image = pygame.image.load(spike)

        # Set the color that should be transparent
        #self.image.set_colorkey(pygame.Color(0, 0, 0))

        # Required for collision detection
        self.rect = self.image.get_rect()
class Credit(pygame.sprite.Sprite):
    """ Platform loads the coins for the user to collect"""

    def __init__(self, number):
        self.number = number
        """ coins are being added on the first level. """
        super().__init__()

        coin = os.path.join(os.path.dirname(__file__), os.pardir, 'images/coin' + str(self.number) + '.png')
        self.image = pygame.image.load(coin)

        # Required for collision detection
        self.rect = self.image.get_rect()

class Heart(pygame.sprite.Sprite):
    """
    An heart image is being loaded on the level that user can collect in order to get more life
    """
    def __init__(self):
        """
        image being loaded.
        """
        super().__init__()


        heart = os.path.join(os.path.dirname(__file__), os.pardir, 'images/heart.png')
        self.image = pygame.image.load(heart)

        # Required for collision detection
        self.rect = self.image.get_rect()

class Spring(pygame.sprite.Sprite):
    """ Platform is loading a spring that the user needs to use in order to
    go to the third wall, because it is too high.
    """

    def __init__(self):
        """ Spring image is being loaded """
        super().__init__()
        spring = os.path.join(os.path.dirname(__file__), os.pardir, 'images/spring1.png')
        self.image = pygame.image.load(spring)


        # Required for collision detection
        self.rect = self.image.get_rect()

class Final_image (pygame.sprite.Sprite):
    """
    This puts the sprike on the level
    """
    def __init__(self, x, y):
        super().__init__()
        final_image = os.path.join(os.path.dirname(__file__), os.pardir, 'images/spring1.png')
        self.image = pygame.image.load(final_image)
        self.rect.x = x
        self.rect.y = y

class Shooting_machine(pygame.sprite.Sprite):
    def __init__(self):
        """
        This is where we load the little tank machine
        """
        super().__init__()
        heart = os.path.join(os.path.dirname(__file__), os.pardir, 'images/shooter.png')
        self.image = pygame.image.load(heart)
        # Required for collision detection
        self.rect = self.image.get_rect()

class Next_level(pygame.sprite.Sprite):
    def __init__(self):
        """
        This is where the next level image is being loaded
        """
        super().__init__()

        heart = os.path.join(os.path.dirname(__file__), os.pardir, 'images/level.png')
        self.image = pygame.image.load(heart)
        self.rect = self.image.get_rect()