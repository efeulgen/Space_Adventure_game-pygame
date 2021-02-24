import pygame
import sys
import assets
import random
import game_text

pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("Space Adventure")

assets.play_music()
bg = assets.Background()
player = assets.Player()
enemy = assets.Enemy()
laser = assets.Laser()
life = assets.Life()
game_over_sign = assets.GameOverSign()
level_over_sign = assets.LevelOverSign()
ground_missile = assets.GroundMissile()
ammo = assets.Ammo()
next_level_sign = assets.NextLevel()

# sun damage


sun_damage_surface = pygame.Surface((1280, 720))
sun_damage_surface.set_alpha(75)


def play_level_one():
    player.player_rect = player.player_img.get_rect(center=(player.player_pos_x, player.player_pos_y))
    sun_damage_red_val = 0
    sun_damage_val = 0
    missile_counter = 0
    sun_damage_red = 0
    in_missile_range = False
    taking_sun_damage = False
    level_over = False
    play_again = False
    game_over = False
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
                    if len(laser.laser_rect_list) < 4:
                        laser.laser_rect_list.append(laser_rect)

                if event.key == pygame.K_p and game_over:
                    play_again = True

            if event.type == pygame.MOUSEBUTTONDOWN and level_over:
                if next_level_sign.arrow_rect.collidepoint(event.pos):
                    enemy.reset_bugs()
                    laser.laser_rect_list.clear()
                    ground_missile.missile_rect_list.clear()

                    game_over = False
                    level_over = False
                    running = False

        # end of key binding
        bg.show_background()

        if not game_over:
            keys_pressed = pygame.key.get_pressed()
            if keys_pressed[pygame.K_DOWN]:
                player.player_rect.y += player.player_speed

            if keys_pressed[pygame.K_UP]:
                player.player_rect.y -= player.player_speed

            player.show_player()
            enemy.move_bugs_to_arena()
            enemy.show_bugs()
            life.show_life()
            laser.fire()

            # collision
            for index, bug in enumerate(enemy.bug_rect_list):
                for laser_obj in laser.laser_rect_list:
                    if laser_obj.colliderect(bug):
                        explosion_sound = pygame.mixer.Sound("sounds/explosion_1.wav")
                        explosion_sound.play()
                        enemy.bug_rect_list.remove(bug)
                        enemy.bug_speeds.remove(enemy.bug_speeds[index])
                        laser.laser_rect_list.remove(laser_obj)

            # player damage
            for bug in enemy.bug_rect_list:
                if player.player_rect.colliderect(bug):
                    explosion_sound = pygame.mixer.Sound("sounds/explosion_1.wav")
                    explosion_sound.play()
                    life.player_life_rect_list.remove(life.player_life_rect_list[-1])
                    enemy.bug_rect_list.remove(bug)

            for missile_rect in ground_missile.missile_rect_list:
                if player.player_rect.colliderect(missile_rect):
                    big_explosion = pygame.mixer.Sound("sounds/big_explosion_1.mp3")
                    big_explosion.play()
                    life.player_life_rect_list.clear()

            # sun damage
            if player.player_rect.top <= 100:
                taking_sun_damage = True
                assets.screen.blit(sun_damage_surface, (0, 0))
                sun_damage_surface.fill((sun_damage_red, 0, 0))

                if sun_damage_red >= 150:
                    sun_damage_red_val = -20
                elif sun_damage_red <= 0:
                    sun_damage_red_val = 20
                sun_damage_red += sun_damage_red_val
                sun_damage_val += 1
                if sun_damage_val >= 20:
                    life.player_life_rect_list.remove(life.player_life_rect_list[-1])
                    sun_damage_val = 0
            else:
                taking_sun_damage = False

            # ground missiles
            ground_missile.shoot_missile()
            if player.player_rect.bottom >= 650:
                missile_counter += 1
                in_missile_range = True
                if missile_counter >= 10:
                    ground_missile.missile_rect_list.append(ground_missile.missile_img.get_rect(center=(random.choice([300, 400, 500, 600, 700]), 750)))
                    missile_counter = 0

            else:
                in_missile_range = False

            # game over
            if life.player_life_rect_list == []:
                game_over = True
                laser.laser_rect_list.clear()

            # level over
            if enemy.bug_rect_list == []:
                game_over = True
                level_over = True
                laser.laser_rect_list.clear()

            # ammo
            if len(laser.laser_rect_list) == 0:
                ammo.show_ammo(4)

            if len(laser.laser_rect_list) == 1:
                ammo.show_ammo(3)

            if len(laser.laser_rect_list) == 2:
                ammo.show_ammo(2)

            if len(laser.laser_rect_list) == 3:
                ammo.show_ammo(1)

        elif level_over:
            player.show_player()
            player.player_rect.x += 10
            assets.screen.blit(level_over_sign.levelOver_img, level_over_sign.levelOver_rect)
            next_level_sign.show_next_level_text()

        elif play_again:
            player.player_rect = player.player_img.get_rect(center=(player.player_pos_x, player.player_pos_y))
            enemy.reset_bugs()
            life.reset_life()

            game_over = False
            play_again = False

        else:  # elif game over
            ground_missile.missile_rect_list.clear()
            enemy.bug_speeds.clear()
            enemy.bug_rect_list.clear()
            assets.screen.blit(game_over_sign.gameOver_img, game_over_sign.gameOver_rect)
            game_text.play_again_message()

        # update and clock
        pygame.display.update()
        clock.tick(120)

#pygame.quit()
