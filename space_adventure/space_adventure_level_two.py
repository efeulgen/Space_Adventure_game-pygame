import pygame
import sys
import assets
import random
import assets_level_two
import game_text
from pygame import mixer

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

mixer.music.load("sounds/scifi_game_music.wav")
mixer.music.play(-1)

background = assets_level_two.BackgroundLevelTwo()
player = assets.Player()
hunter = assets_level_two.SpaceHunter()
laser = assets.Laser()
life = assets.Life()
game_over_sign = assets.GameOverSign()
level_over_sign = assets.LevelOverSign()
ammo = assets.Ammo()
next_level_sign = assets.NextLevel()

HUNTER_FIRE = pygame.USEREVENT
pygame.time.set_timer(HUNTER_FIRE, 350)


def play_level_two():
    player.player_rect = player.player_img.get_rect(center=(player.player_pos_x, player.player_pos_y))
    game_over = False
    level_over = False
    play_again = False
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

                if event.key == pygame.K_SPACE:
                    laser_x = player.player_rect.x
                    laser_y = player.player_rect.y
                    laser_rect = laser.laser_img.get_rect(center=(laser_x + 70, laser_y + 30))
                    if len(laser.laser_rect_list) < 3:
                        laser.laser_rect_list.append(laser_rect)

                if event.key == pygame.K_p and game_over:
                    play_again = True

            if event.type == pygame.MOUSEBUTTONDOWN and level_over:
                if next_level_sign.arrow_rect.collidepoint(event.pos):
                    hunter.reset_hunter()
                    laser.laser_rect_list.clear()

                    game_over = False
                    level_over = False
                    running = False

            if event.type == HUNTER_FIRE:
                if hunter.hunter_rects != []:
                    hunter_laser_y = random.choice(hunter.hunter_rects).y
                    hunter_laser_rect = laser.laser_img.get_rect(center=(1180, hunter_laser_y + 65))
                    laser.hunter_laser_rect_list.append(hunter_laser_rect)
                else:
                    pass

        # end of key binding
        background.show_bg_level_two()

        if not game_over:
            keys_pressed = pygame.key.get_pressed()
            if keys_pressed[pygame.K_DOWN]:
                player.player_rect.y += player.player_speed
            if keys_pressed[pygame.K_UP]:
                player.player_rect.y -= player.player_speed

            player.show_player()
            hunter.show_hunter()
            laser.fire()
            laser.fire_hunter()
            life.show_life()

            # collision
            for index, hunter_rect in enumerate(hunter.hunter_rects):
                for laser_obj in laser.laser_rect_list:
                    if laser_obj.colliderect(hunter_rect):
                        explosion_sound = pygame.mixer.Sound("sounds/explosion_1.wav")
                        explosion_sound.play()
                        laser.laser_rect_list.remove(laser_obj)
                        hunter.hunter_lifes[index] -= 1
                        if hunter.hunter_lifes[index] == 0:
                            hunter.hunter_rects.remove(hunter_rect)
                            hunter.hunter_speeds.remove(hunter.hunter_speeds[index])
                            hunter.hunter_lifes.remove(hunter.hunter_lifes[index])

            # player damage
            for laser_rect in laser.hunter_laser_rect_list:
                if player.player_rect.colliderect(laser_rect):
                    explosion_sound = pygame.mixer.Sound("sounds/explosion_1.wav")
                    explosion_sound.play()
                    life.player_life_rect_list.remove(life.player_life_rect_list[-1])
                    laser.hunter_laser_rect_list.remove(laser_rect)

            # game over
            if life.player_life_rect_list == []:
                game_over = True
                laser.hunter_laser_rect_list.clear()
                laser.laser_rect_list.clear()

            if hunter.hunter_rects == []:
                game_over = True
                level_over = True
                laser.hunter_laser_rect_list.clear()
                laser.laser_rect_list.clear()

            # ammo
            if len(laser.laser_rect_list) == 0:
                ammo.show_ammo(3)

            if len(laser.laser_rect_list) == 1:
                ammo.show_ammo(2)

            if len(laser.laser_rect_list) == 2:
                ammo.show_ammo(1)

        elif level_over:
            player.show_player()
            player.player_rect.x += 10
            assets.screen.blit(level_over_sign.levelOver_img, level_over_sign.levelOver_rect)
            next_level_sign.show_next_level_text()

        elif play_again:
            player.player_rect = player.player_img.get_rect(center=(player.player_pos_x, player.player_pos_y))
            hunter.reset_hunter()
            life.reset_life()

            game_over = False
            play_again = False

        else:
            life.player_life_x = 20
            laser.hunter_laser_rect_list.clear()
            hunter.hunter_rects.clear()
            hunter.hunter_speeds.clear()
            assets.screen.blit(game_over_sign.gameOver_img, game_over_sign.gameOver_rect)
            game_text.play_again_message()

        # update&clock
        pygame.display.update()
        clock.tick(120)

#pygame.quit()
