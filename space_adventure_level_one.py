import pygame
import sys
import assets
import game_text
import random

pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("Space Adventure")
pygame.mouse.set_visible(False)

assets.play_music()
bg = assets.Background()
player = assets.Player()
enemy = assets.Enemy()
laser = assets.Laser()
life = assets.Life()
game_over_sign = assets.GameOverSign()
level_over_sign = assets.LevelOverSign()
ground_missile = assets.GroundMissile()

# sun damage
sun_damage_red = 0
sun_damage_red_val = 0
sun_damage_val = 0
sun_damage_surface = pygame.Surface((1280, 720))
sun_damage_surface.set_alpha(75)

# console
console = pygame.Rect(900, 620, 500, 100)
console_boundaries = pygame.Rect(890, 610, 500, 110)

missile_counter = 0
in_missile_range = False
taking_sun_damage = False
level_over = False
game_over = False
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False

            if event.key == pygame.K_SPACE:
                laser_x = player.player_rect.x
                laser_y = player.player_rect.y
                laser_rect = laser.laser_img.get_rect(center=(laser_x, laser_y))
                laser.laser_rect_list.append(laser_rect)

        if event.type == pygame.MOUSEMOTION:
            player.player_rect.y = event.pos[1]

    bg.show_background()

    if not game_over:
        player.show_player()
        enemy.move_bugs_to_arena()
        enemy.show_bugs()
        life.show_life()
        laser.fire()
        pygame.draw.rect(assets.screen, (46, 62, 87), console_boundaries)
        pygame.draw.rect(assets.screen, (157, 178, 212), console)

        # collision
        for laser_rect in laser.laser_rect_list:
            for index, bug in enumerate(enemy.bug_rect_list):
                if laser_rect.colliderect(bug):
                    explosion_sound = pygame.mixer.Sound("sounds/explosion_1.wav")
                    explosion_sound.play()
                    enemy.bug_rect_list.remove(bug)
                    enemy.bug_speeds.remove(enemy.bug_speeds[index])
                    laser.laser_rect_list.remove(laser_rect)

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

        # console
        if taking_sun_damage:
            game_text.sun_damage_message()
        elif in_missile_range:
            game_text.missile_range_message()
        else:
            game_text.mission_message()

        # game over
        if life.player_life_rect_list == []:
            game_over = True

        if enemy.bug_rect_list == []:
            game_over = True
            level_over = True

    elif level_over:
        player.show_player()
        player.player_rect.x += 10
        assets.screen.blit(level_over_sign.levelOver_img, level_over_sign.levelOver_rect)
    else:
        assets.screen.blit(game_over_sign.gameOver_img, game_over_sign.gameOver_rect)
    # update and clock
    pygame.display.update()
    clock.tick(120)

pygame.quit()

# todo play again
# todo next level
# todo redesign alien spawns
