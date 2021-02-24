import pygame
import sys
import assets
import assets_level_two
import game_text

pygame.init()
clock = pygame.time.Clock()

assets.play_music()
background = assets_level_two.BackgroundLevelTwo()
player = assets.Player()
laser = assets.Laser()
life = assets.Life()
game_over_sign = assets.GameOverSign()
ammo = assets.Ammo()

boss_img = pygame.transform.scale2x(pygame.image.load("assets/space_adventure_final_boss.png"))


boss_life_bar = pygame.Rect(800, 20, 400, 20)

BOSS_FIRE = pygame.USEREVENT
pygame.time.set_timer(BOSS_FIRE, 640)


def play_final_boss_fight():
    player.player_rect = player.player_img.get_rect(center=(player.player_pos_x, player.player_pos_y))
    boss_rect = boss_img.get_rect(center=(1350, 360))
    boss_speed = 4
    boss_life_minus_x = 0
    play_again = False
    game_over = False
    game_complete = False
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q and game_complete:
                    pygame.quit()
                    sys.exit()

                if event.key == pygame.K_p and game_complete:
                    life.reset_life()
                    laser.laser_rect_list.clear()
                    running = False

                if event.key == pygame.K_SPACE:
                    laser_x = player.player_rect.x
                    laser_y = player.player_rect.y
                    laser_rect = laser.laser_img.get_rect(center=(laser_x + 70, laser_y + 30))
                    if len(laser.laser_rect_list) < 3:
                        laser.laser_rect_list.append(laser_rect)

                if event.key == pygame.K_p and game_over:
                    play_again = True

            if event.type == BOSS_FIRE:
                boss_laser_x_1 = boss_rect.x + 110
                boss_laser_y_1 = boss_rect.y + 68
                boss_laser_rect_1 = laser.boss_laser_img.get_rect(center=(boss_laser_x_1, boss_laser_y_1))

                boss_laser_x_2 = boss_rect.x + 106
                boss_laser_y_2 = boss_rect.y + 78
                boss_laser_rect_2 = laser.boss_laser_img.get_rect(center=(boss_laser_x_2, boss_laser_y_2))

                boss_laser_x_3 = boss_rect.x + 106
                boss_laser_y_3 = boss_rect.y + 182
                boss_laser_rect_3 = laser.boss_laser_img.get_rect(center=(boss_laser_x_3, boss_laser_y_3))

                boss_laser_x_4 = boss_rect.x + 110
                boss_laser_y_4 = boss_rect.y + 192
                boss_laser_rect_4 = laser.boss_laser_img.get_rect(center=(boss_laser_x_4, boss_laser_y_4))

                laser.boss_laser_rect_list.append(boss_laser_rect_1)
                laser.boss_laser_rect_list.append(boss_laser_rect_2)
                laser.boss_laser_rect_list.append(boss_laser_rect_3)
                laser.boss_laser_rect_list.append(boss_laser_rect_4)

        # end of key binding
        background.show_bg_level_two()
        if not game_over:
            keys_pressed = pygame.key.get_pressed()
            if keys_pressed[pygame.K_DOWN]:
                player.player_rect.y += player.player_speed
            if keys_pressed[pygame.K_UP]:
                player.player_rect.y -= player.player_speed

            assets.screen.blit(boss_img, boss_rect)
            player.show_player()
            life.show_life()
            laser.fire()
            laser.fire_boss()

            # boss movement
            if not boss_rect.right < 1250:
                boss_rect.x -= 5

            else:
                boss_rect.y += boss_speed

            if boss_rect.top <= 0 or boss_rect.bottom >= 720:
                boss_speed *= -1

            # boss life
            boss_life_minus = pygame.Rect(800, 20, boss_life_minus_x, 20)
            pygame.draw.rect(assets.screen, (255, 255, 0), boss_life_bar)
            pygame.draw.rect(assets.screen, (255, 0, 0), boss_life_minus)

            # collision
            for laser_obj in laser.laser_rect_list:
                if boss_rect.colliderect(laser_obj):
                    explosion_sound = pygame.mixer.Sound("sounds/explosion_1.wav")
                    explosion_sound.play()
                    laser.laser_rect_list.remove(laser_obj)
                    boss_life_minus_x += 20

            # player damage
            for boss_laser_obj in laser.boss_laser_rect_list:
                if player.player_rect.colliderect(boss_laser_obj):
                    explosion_sound = pygame.mixer.Sound("sounds/explosion_1.wav")
                    explosion_sound.play()
                    laser.boss_laser_rect_list.remove(boss_laser_obj)
                    life.player_life_rect_list.remove(life.player_life_rect_list[-1])

            # game over
            if life.player_life_rect_list == []:
                game_over = True
                laser.laser_rect_list.clear()

            # game complete
            if boss_life_minus_x >= 400:
                game_complete = True
                game_over = True

            # ammo
            if len(laser.laser_rect_list) == 0:
                ammo.show_ammo(3)

            if len(laser.laser_rect_list) == 1:
                ammo.show_ammo(2)

            if len(laser.laser_rect_list) == 2:
                ammo.show_ammo(1)

        elif game_complete:
            laser.boss_laser_rect_list.clear()
            player.show_player()
            game_text.you_win_message()
            player.player_rect.x += 8
            game_text.play_again_message()

        elif play_again:
            for i in range(3):
                life.player_life_rect_list.append(life.player_life_img.get_rect(center=(life.player_life_x, 20)))
                life.player_life_x += 30

            boss_rect = boss_img.get_rect(center=(1350, 360))

            player.player_rect = player.player_img.get_rect(center=(player.player_pos_x, player.player_pos_y))
            game_over = False
            play_again = False

        else:
            life.player_life_x = 20
            boss_life_minus_x = 0
            laser.boss_laser_rect_list.clear()
            assets.screen.blit(game_over_sign.gameOver_img, game_over_sign.gameOver_rect)
            game_text.play_again_message()

        # clock&update
        pygame.display.update()
        clock.tick(120)

#pygame.quit()