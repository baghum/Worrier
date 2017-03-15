__author__ = 'Andy'
"""
This module takes care of all the sprite groups to be updated on the screen on this level.
"""

import pygame, sys
import os
from pygame.locals import *
# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


class Level(object):
    """ This is where all the sprites groups are and going to be updated in this class every
    time the update is called. """

    def __init__(self, player, enemy_player):

        """ Constructor. Pass in a handle to player. Needed for when moving platforms
            collide with the player. """
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.credit_list = pygame.sprite.Group()
        self.spring_list = pygame.sprite.Group()

        self.player = player
        self.enemy_player = enemy_player

    # Update everything on this level
    def update(self):
        """ Update everything in this level."""
        self.platform_list.update()
        self.enemy_list.update()
        self.credit_list.update()
        self.spring_list.update()


    def draw(self, screen):
        """ Draw everything on this level. """
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)
        self.credit_list.draw(screen)
        self.spring_list.draw(screen)

