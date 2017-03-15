__author__ = 'Andy'

"""
This is where all the positions are defined for all the final sprites that are
     going to be on the screen.
"""

from level1 import Level
from platform import Platform,Spring, Heart, Shooting_machine
from platform import Spike, Next_level
from platform import Credit


# Create platforms for the level
class Level_01(Level):

    """ we get the position of walls, spring, tank, coin
     """
    def __init__(self, player, enemy_player):
        self.number = 1
        """ Create level 1 based on the position that are given """

        # Call the parent constructor
        Level.__init__(self, player, enemy_player)

        # Array with width, height, x, and y of platform
        level = [[0, 500],
                 [300, 350],
                 [300, 150]
                 ]
        #Array with all the enemy's positions
        enemy = [[700, 637],
                 [500, 336]
                 ]
        #Array with all the credits.
        credit_coin = [[820, 580],
                       [865, 580],
                       [910, 580],
                       [955, 580],
                       [1000, 580],
                       [1045, 580],
                       [1090, 580],
                       [1135, 580],
                       [1180, 580]]
        # array for heart
        heart_array = [800, 200]

        #Array for the spring
        jumping_spring = [50, 455]

        shooting_machine = [1250, 320]
        # next level image position
        level_image = [1000, 80]

        #Go through the array above and add platforms
        for platform in level:
            block = Platform()
            block.rect.x = platform[0]
            block.rect.y = platform[1]
            block.player = self.player
            self.platform_list.add(block)

        for spike in enemy:
            enemy_block = Spike()
            enemy_block.rect.x = spike[0]
            enemy_block.rect.y = spike[1]
            enemy_block.player = self.player
            self.enemy_list.add(enemy_block)

        for coin in credit_coin:
            coin_credit = Credit(self.number)
            coin_credit.rect.x = coin[0]
            coin_credit.rect.y = coin[1]
            coin_credit.player = self.player
            self.credit_list.add(coin_credit)
            self.number += 1

        spring = Spring()
        spring.rect.x = jumping_spring[0]
        spring.rect.y = jumping_spring[1]
        spring.player = self.player
        self.spring_list.add(spring)

        heart = Heart()
        heart.rect.x = heart_array[0]
        heart.rect.y = heart_array[1]
        heart.player = self.player
        self.credit_list.add(heart)

        tank = Shooting_machine()
        tank.rect.x = shooting_machine[0]
        tank.rect.y = shooting_machine[1]
        self.spring_list.add(tank)

        next_level = Next_level()
        next_level.rect.x = level_image[0]
        next_level.rect.y = level_image[1]
        self.spring_list.add(next_level)












