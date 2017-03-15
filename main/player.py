__author__ = 'Andy'
"""
This is the model where the player and all the moving sprites are created.
"""

import pygame
import os, sys
import glob
# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Screen dimensions
SCREEN_WIDTH = 1300
SCREEN_HEIGHT = 650


class Player(pygame.sprite.Sprite):
    """ This is the class where the player is being created. """
    def __init__(self):
        """ Constructor function """

        # Call the parent's constructor
        super().__init__()

        player_first_look = os.path.join(os.path.dirname(__file__), os.pardir, 'robot/p1_right.png')
        self.image = pygame.image.load(player_first_look)

        self.rect = self.image.get_rect()

        # Set speed vector of player
        self.change_x = 0
        self.change_y = 0

        # List of sprites we can bump against
        # This is how the player gets a reference to the list of walls.
        self.level = None
        self.dead_status = False
        self.jumping_status = False

    def shoot(self):
        """

        :return: creates a circle to shoot
        """
        bullet = pygame.draw.circle(self.color[BLACK], (self.change_x, self.change_y), 10, 20)

    # collision with the enemy bullets
    def enemy_bullet_check(self, bullets):
        """

        :param bullets:
        :return: check is the enemy bullets are being hit to the player
        """
        enemy_bullet_list = pygame.sprite.spritecollide(self, bullets, False)
        if not not enemy_bullet_list:
            return True


    def update(self):
        """

        :return: updates the player movments during the game
        """
        self.calc_grav()

        # Move left/right
        self.rect.x += self.change_x

        # See if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right

        # Move up/down
        self.rect.y += self.change_y

        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:

            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom

            # Stop our vertical movement
            self.change_y = 0


        #spike
        spike_hit_list = pygame.sprite.spritecollide(self, self.level.enemy_list, False, pygame.sprite.collide_mask)
        if not not spike_hit_list:
            self.dead_status = True

        #coin
        coin_hit_list = pygame.sprite.spritecollide(self, self.level.credit_list, True, pygame.sprite.collide_mask)

        #spring
        spring_hit_list = pygame.sprite.spritecollide(self, self.level.spring_list, False)
        if not not spring_hit_list:
            #x
            # for s in self.level.spring_list:
            #     g = os.path.join(os.path.dirname(__file__), os.pardir, spring_list[i])
            #     s.image = pygame.image.load(g)
            #     self.rect = self.image.get_rect()
            self.jumping_status = True

    def calc_grav(self):
        """ Calculate effect of gravity. """
        if self.change_y == 0:
            self.change_y = 1 # if platform moves down player will not float now
        else:
            self.change_y += .35 # controls amount of gravity

        # See if we are on the ground.
        # Don't want to fall off the screen (unless you want offscreen deaths!)
        if self.rect.y >= SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = SCREEN_HEIGHT - self.rect.height

    #moves the player up and down when the player is dead
    def dead_jump(self):
        """

        :return: moves the player's y position when the player is dead
        """
        self.rect.y += 20
        self.stop()


    def jump(self):
        """ Called when user hits 'jump' button. """

        # move down a bit and see if there is a platform below us.
        # Move down 2 pixels because it doesn't work well if we only move down
        # 1 when working with a platform moving down.
        self.rect.y += 2 # Does NOT draw the player two pixels down.
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2

        # If it is ok to jump, set our speed upwards
        # (You don't want to jump if you are already jumping)
        if len(platform_hit_list) > 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.change_y = -10

    # Player-controlled movement:
    def go_left(self):
        """ Called when the user hits the left arrow. """
        self.change_x = -5

    def go_right(self):
        """ Called when the user hits the right arrow. """
        self.change_x = 5

    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.change_x = 0

    def jump_spring(self):
        """ Called when user hits 'jump' button. """

        # move down a bit and see if there is a platform below us.
        # Move down 2 pixels because it doesn't work well if we only move down
        # 1 when working with a platform moving down.
        self.rect.y += 5 # Does NOT draw the player two pixels down.
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.spring_list, False, pygame.sprite.collide_mask)
        self.rect.y -= 200

        # If it is ok to jump, set our speed upwards
        # (You don't want to jump if you are already jumping)
        if len(platform_hit_list) > 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.change_y = -10

#################################################################################################################3
class MovingEnemy(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the player
        controls. """
    def __init__(self):
        """ Constructor function """

        # Call the parent's constructor
        super().__init__()


        player_first_look = os.path.join(os.path.dirname(__file__), os.pardir, 'robot/p1_right.png')
        self.image = pygame.image.load(player_first_look)

        self.rect = self.image.get_rect()
        #self.speed = 1
        counter = 0
        # Set speed vector of player
        self.enemy_change_x = 0
        self.enemy_change_y = 0

        # List of sprites we can bump against
        # This is how the player gets a reference to the list of walls.
        self.level = None

    def enemy_go_left(self):
        """ Called when the user hits the left arrow. """
        self.enemy_change_x = -2

    def enemy_go_right(self):
        """ Called when the user hits the right arrow. """
        self.enemy_change_x = 2

    def update(self):
        """

        :return:updates the users moving enemy movment
        """
        self.rect.x += self.enemy_change_x
    def stop(self):
        """

        :return:stops the enemies movments
        """
        self.enemy_change_x = 0


#################################################################################################################
class Bullet(pygame.sprite.Sprite):
    """ This class represents the bullet . """
    def __init__(self, player_facing, x, y):
        # Call the parent class (Sprite) constructor
        super().__init__()
        self.player_facing = player_facing

        if self.player_facing:
            bullet = os.path.join(os.path.dirname(__file__), os.pardir, 'images/knife_left.png')
        else:
            bullet = os.path.join(os.path.dirname(__file__), os.pardir, 'images/knife_right.png')

        self.image = pygame.image.load(bullet)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        """ Move the bullet. """
        if self.player_facing:
            self.rect.x -= 10
        else:
            self.rect.x += 10

######################################################################################################
class Enemy_Bullet(pygame.sprite.Sprite):
    """
    This is for enemy bullets
    """

    def __init__(self, player_facing, x, y):
        super().__init__()
        self.player_facing = player_facing
        bullet = os.path.join(os.path.dirname(__file__), os.pardir, 'images/enemy_player_bullet.png')

        self.image = pygame.image.load(bullet)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y + 25
    def update(self):
        """ Move the bullet. """
        if self.player_facing:
            self.rect.x -= 12
        else:
            self.rect.x += 12
class Tank_Bullet(pygame.sprite.Sprite):
    """
    Tank bullets that are coming about of the tank
    """

    def __init__(self, x, y):
        super().__init__()
        #self.player_facing = player_facing
        bullet = os.path.join(os.path.dirname(__file__), os.pardir, 'images/tank_bullet.png')
        self.image = pygame.image.load(bullet)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def update(self):
        """ Move the bullet. """

        self.rect.x -= 12


class Blood(pygame.sprite.Sprite):
    """
    The blood when the enemy gets hit
    """

    def __init__(self, x, y):
        super().__init__()
        blood = os.path.join(os.path.dirname(__file__), os.pardir, 'images/blood1.png')

        self.image = pygame.image.load(blood)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Player_life:
    """
    Shows how much life the player has
    """
    def __init__(self):
        self.enemy_size = 50
        self.player_size = 50


    def draw(self, screen):
        pygame.draw.rect(screen, GREEN, [70, 5, self.player_size, 10])
        #self.size -= 10

    def draw_enemy_life(self, screen):
        pygame.draw.rect(screen, GREEN, [200, 5, self.enemy_size, 10])
        #self.size -= 10

    def hit_enemy(self):
        self.enemy_size -= 10
    def hit_player(self):
        self.player_size -= 5








