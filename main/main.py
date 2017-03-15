__author__ = 'Andy'

import pygame, sys
import os
from pygame.locals import *
from player import Player, MovingEnemy, Bullet, Enemy_Bullet, Blood, Player_life, Tank_Bullet
from level_01 import Level_01
import time


# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
# Screen dimensions
SCREEN_WIDTH = 1300
SCREEN_HEIGHT = 650

def main():
    """ Main Program """
    pygame.init()
    FPS = 20  # 30 frames per second
    fps_clock = pygame.time.Clock()

    # Set the height and width of the screen
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    #title
    pygame.display.set_caption("Warrior")

    #font
    font = pygame.font.SysFont("Courier", 15)
    font.set_bold(True)

    player_name = "Player"
    player_name = font.render(player_name, 5, RED)

    enemy_name = "Enemy"
    enemy_name = font.render(enemy_name, 5, RED)


    # bg_music = pygame.mixer.Sound(os.path.join(os.path.dirname(__file__), 'Project/Audio/battle_music.wav'))
    # bg_music.play()
    bgfx_path = os.path.join(os.path.dirname(__file__), os.pardir, 'Audio/battle_music.ogg')
    pygame.mixer.music.load(bgfx_path)
    pygame.mixer.music.set_endevent(USEREVENT)
    pygame.mixer.music.play()


    backgroud = pygame.image.load(os.path.join(os.path.dirname(__file__), os.pardir, 'images/home.png'))
    game_over = pygame.image.load(os.path.join(os.path.dirname(__file__), os.pardir, 'images/gameOver.png'))
    screen.blit(backgroud, (0,0))

    #####################################################################################
    # going left images
    player_image_left = []
    player_image_left.append(pygame.image.load(os.path.join(os.path.dirname(__file__), os.pardir, 'robot/p1_left.png')))
    player_image_left.append(pygame.image.load(os.path.join(os.path.dirname(__file__), os.pardir, 'robot/p2_left.png')))
    player_image_left.append(pygame.image.load(os.path.join(os.path.dirname(__file__), os.pardir, 'robot/p3_left.png')))
    player_image_left.append(pygame.image.load(os.path.join(os.path.dirname(__file__), os.pardir, 'robot/p4_left.png')))
    player_current_left = 0

    #####################################################################################
    # going right
    player_image_right = []
    player_image_right.append(pygame.image.load(os.path.join(os.path.dirname(__file__), os.pardir, 'robot/p1_right.png')))
    player_image_right.append(pygame.image.load(os.path.join(os.path.dirname(__file__), os.pardir, 'robot/p2_right.png')))
    player_image_right.append(pygame.image.load(os.path.join(os.path.dirname(__file__), os.pardir, 'robot/p3_right.png')))
    player_image_right.append(pygame.image.load(os.path.join(os.path.dirname(__file__), os.pardir, 'robot/p4_right.png')))
    player_current_right = 0
    enemy_player_current_right = 0
    count_right = 0
    enemy_counter = 0

    #####################################################################################
    # enemy player right
    enemy_player_right = []
    enemy_player_right.append(pygame.image.load(os.path.join(os.path.dirname(__file__), os.pardir,
                                                            'images/enemy_player1_right.png')))
    enemy_player_right.append(pygame.image.load(os.path.join(os.path.dirname(__file__), os.pardir,
                                                            'images/enemy_player2_right.png')))
    enemy_player_right.append(pygame.image.load(os.path.join(os.path.dirname(__file__), os.pardir,
                                                            'images/enemy_player3_right.png')))
    enemy_player_right.append(pygame.image.load(os.path.join(os.path.dirname(__file__), os.pardir,
                                                            'images/enemy_player4_right.png')))

    #####################################################################################

    #enemy player left
    enemy_player_left = []
    enemy_player_left.append(pygame.image.load(os.path.join(os.path.dirname(__file__), os.pardir,
                                                            'images/enemy_player1_left.png')))
    enemy_player_left.append(pygame.image.load(os.path.join(os.path.dirname(__file__), os.pardir,
                                                            'images/enemy_player2_left.png')))
    enemy_player_left.append(pygame.image.load(os.path.join(os.path.dirname(__file__), os.pardir,
                                                            'images/enemy_player3_left.png')))
    enemy_player_left.append(pygame.image.load(os.path.join(os.path.dirname(__file__), os.pardir,
                                                            'images/enemy_player4_left.png')))

    #####################################################################################

    blood_list = []
    blood_list.append(pygame.image.load(os.path.join(os.path.dirname(__file__), os.pardir,
                                                     'images/blood1.png')))
    blood_list.append(pygame.image.load(os.path.join(os.path.dirname(__file__), os.pardir,
                                                     'images/blood2.png')))
    blood_list.append(pygame.image.load(os.path.join(os.path.dirname(__file__), os.pardir,
                                                     'images/blood3.png')))
    blood_list.append(pygame.image.load(os.path.join(os.path.dirname(__file__), os.pardir,
                                                     'images/blood4.png')))
    blood_list.append(pygame.image.load(os.path.join(os.path.dirname(__file__), os.pardir,
                                                     'images/blood5.png')))
    blood_list.append(pygame.image.load(os.path.join(os.path.dirname(__file__), os.pardir,
                                                     'images/blood6.png')))
    blood_list.append(pygame.image.load(os.path.join(os.path.dirname(__file__), os.pardir,
                                                     'images/blood7.png')))
    blood_list.append(pygame.image.load(os.path.join(os.path.dirname(__file__), os.pardir,
                                                     'images/blood8.png')))


    # Create the player
    player = Player()
    enemy_player = MovingEnemy()


    level_list = []
    level_list.append(Level_01(player, enemy_player))

    # Set the current level
    current_level_no = 0
    current_level = level_list[current_level_no]

    #create a sprite group for active sprites
    active_sprite_list = pygame.sprite.Group()
    player.level = current_level
    enemy_player.level = current_level


    player.rect.x = 200
    player.rect.y = SCREEN_HEIGHT - player.rect.height
    active_sprite_list.add(player)

    enemy_player.rect.x = 400
    enemy_player.rect.y = 428
    active_sprite_list.add(enemy_player)

    # Loop until the user clicks the close button
    done = False
    walking_right = False
    walking_left = False
    bullet_status = False
    player_facing = False
    enemy_player_facing = False
    enemy_bullet_delay_counter = 0
    tank_bullet_delay_counter = 0
    blood_current = []
    blood_counter = 0
    blood_status = False
    player_life = 90
    game_over_status = False
    enemy_display = False
    enemy_lift = 50

    #enemy life bar
    player_life_status = Player_life()

    #a group for a bullet
    bullet_active_list = pygame.sprite.Group()
    my_bullet_active_list = pygame.sprite.Group()
    blood_active_list = pygame.sprite.Group()
    #####################################################################################
    # -------- Main Program Loop -----------
    while not done:
        if game_over_status == False:
        #  print("in if")
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                ###############################################################################
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        walking_left = True
                        player_facing = True
                    if event.key == pygame.K_RIGHT:
                        walking_right = True
                        player_facing = False
                    if event.key == pygame.K_UP:
                        player.jump()
                    if event.key == pygame.K_s:
                        bullet_status = True

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT and player.change_x < 0:
                        walking_left = False
                        player.image = player_image_left[0]
                        player.stop()
                    if event.key == pygame.K_RIGHT and player.change_x > 0:
                        walking_right = False
                        player.image = player_image_right[0]
                        player.stop()
                    if event.key == pygame.K_s:
                        bullet_status = False

           ###############################################################################
           #this if and elif loop take care of the moving enemy to move slower and animation
            if enemy_display == False:
                if enemy_counter == 2:
                    #moving to the right
                    if count_right < 32:
                        enemy_player_current_right = count_right % 4
                        enemy_player.image = enemy_player_right[enemy_player_current_right]
                        enemy_player.enemy_go_right()
                        count_right += 1
                        enemy_player_facing = False

                        #moving to the left
                    elif 31 < count_right < 64:
                        enemy_player_current_left = count_right % 4
                        enemy_player.image = enemy_player_left[enemy_player_current_left]
                        enemy_player.enemy_go_left()
                        count_right += 1
                        enemy_player_facing = True
                    else:
                        count_right = 0
               #set the counter to 0
                elif enemy_counter > 3:
                    enemy_counter = 0
                enemy_counter += 1

               # enemy_player bullets
                if enemy_bullet_delay_counter == 30:
                    enemy_bullet = Enemy_Bullet(enemy_player_facing, enemy_player.rect.x, enemy_player.rect.y - 6)
                    enemy_bullet2 = Enemy_Bullet(enemy_player_facing, enemy_player.rect.x, enemy_player.rect.y + 5)

                    bullet_active_list.add(enemy_bullet)
                    active_sprite_list.add(enemy_bullet)
                    bullet_active_list.add(enemy_bullet2)
                    active_sprite_list.add(enemy_bullet2)

                elif enemy_bullet_delay_counter > 30:
                    enemy_bullet_delay_counter = 0
                enemy_bullet_delay_counter += 1

            if tank_bullet_delay_counter == 60:
                tank_bullet = Tank_Bullet(1230, 325)
                bullet_active_list.add(tank_bullet)
                active_sprite_list.add(tank_bullet)
            elif tank_bullet_delay_counter > 60:
                tank_bullet_delay_counter = 0
            tank_bullet_delay_counter += 1

           ###############################################################################
           # going right changing images
            if walking_right and player.change_y == 0:
                player_current_right = (player_current_right + 1) % 4
                player.image = player_image_right[player_current_right]
                player.go_right()
           #going to right but the player is in air, so no need to change the images
            elif walking_right and player.change_y != 0:
                player.image = player_image_right[0]
                player.go_right()

           # going left changing images
            if walking_left and player.change_y == 0:
                player_current_left = (player_current_left + 1) % 4
                player.image = player_image_left[player_current_left]
                player.go_left()
            elif walking_left and player.change_y != 0:
                #going to left but the player is in air, so no need to change the images
                player.image = player_image_left[0]
                player.go_left()

            #when the warrior dies
            if player.dead_status:
                player.dead_jump()
                player.image = pygame.image.load(os.path.join(os.path.dirname(__file__), os.pardir, 'robot/dead.png'))

            if player.jumping_status:
                player.jump_spring()
                player.jumping_status = False
            ###############################################################################

            if bullet_status:
                bullet = Bullet(player_facing, player.rect.x, player.rect.y + 30)
                my_bullet_active_list.add(bullet)
                active_sprite_list.add(bullet)
                bullet_status = False

            #checking if the bullet is touching the enemy
            player_bullet_check = pygame.sprite.spritecollide(enemy_player, my_bullet_active_list, True,
                                                              pygame.sprite.collide_mask)
            if not not player_bullet_check:
                enemy_lift -= 10
                player_life_status.hit_enemy()
                player_life_status.draw_enemy_life(screen)

                if enemy_lift == 0:
                    enemy_display = True
                    active_sprite_list.remove(enemy_player)

           #removing the bullets from the list
            for each_bullet in my_bullet_active_list:
                if each_bullet.rect.x > 1300 or each_bullet.rect.x < 5:
                    my_bullet_active_list.remove(each_bullet)
                    active_sprite_list.remove(each_bullet)

           #checking for the enamy's bullets limit
            for each_bullet in bullet_active_list:
                if each_bullet.rect.x > 1300 or each_bullet.rect.x < 5:
                    bullet_active_list.remove(each_bullet)
                    active_sprite_list.remove(each_bullet)
           ###############################################################################

            bullet_collide = pygame.sprite.spritecollide(player, bullet_active_list, False, pygame.sprite.collide_mask)
            if not not bullet_collide:
                blood_status = True
            if blood_status:
                player_life -= 10
                print(player_life, 'player life')
                player_life_status.hit_player()
                player_life_status.draw(screen)
                blood_current = Blood(player.rect.x, player.rect.y)
                #this is to display blood
                if blood_counter != 7:
                    blood_current.image = blood_list[blood_counter]
                    blood_active_list.add(blood_current)
                    active_sprite_list.add(blood_current)
                    blood_counter += 1
                    blood_status = False
                #setting the blood number back to 0
            if blood_counter == 7:
                blood_counter = 0
            if player_life <= 0:
                if blood_counter != 7:
                    blood_current = Blood(player.rect.x, player.rect.y)
                    blood_current.image = blood_list[blood_counter]
                    blood_active_list.add(blood_current)
                    active_sprite_list.add(blood_current)
                    blood_counter += 1
                if blood_counter == 7:
                    player.image = pygame.image.load(os.path.join(os.path.dirname(__file__),
                                                                  os.pardir, 'images/dead.png'))
                    #bg_music.stop()
                    game_over_status = True
                    #game_over = Final_image(50, 10)


           ###############################################################################
           # Update the player.
            active_sprite_list.update()

            # Update items in the level
            current_level.update()

            # If the player gets near the right side, shift the world left (-x)
            if player.rect.right > SCREEN_WIDTH:
                player.rect.right = SCREEN_WIDTH

            # If the player gets near the left side, shift the world right (+x)
            if player.rect.left < 0:
                player.rect.left = 0

            # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
            current_level.draw(screen)

            active_sprite_list.draw(screen)

            blood_active_list.remove(blood_current)
            active_sprite_list.remove(blood_current)

        # Go ahead and update the screen with what we've drawn.

            screen.blit(player_name, (0, 0))
            screen.blit(enemy_name, (135, 0))
            player_life_status.draw(screen)
            player_life_status.draw_enemy_life(screen)
            pygame.display.flip()
            screen.blit(backgroud, (0, 0))
            fps_clock.tick(FPS)

        else:
            time.sleep(1)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
            pygame.display.flip()
            screen.blit(backgroud, (0, 0))
            screen.blit(game_over, (400, 150))
            fps_clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()