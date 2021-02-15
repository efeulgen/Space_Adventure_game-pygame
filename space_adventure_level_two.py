import pygame
import sys
import random
import assets
from pygame import mixer

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)

# music
mixer.music.load("sounds/scifi_game_music.wav")
mixer.music.play(-1)

# bg


player = assets.Player()


# game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False

        if event.type == pygame.MOUSEMOTION:
            player_y = event.pos[1]

    # background blit and animation
    screen.blit(background_img, (background_1_x, 0))
    screen.blit(background_img, (background_2_x, 0))
    background_1_x += background_increment
    background_2_x += background_increment

    if background_1_x <= -1280:
        background_1_x = background_respwan

    if background_2_x <= -1280:
        background_2_x = background_respwan

    # player blit/ animation
    player_rect = player_img.get_rect(center=(player_x, player_y))
    screen.blit(player_img, player_rect)

    # hunter blit/ animation
    hunter_rect = hunter_img.get_rect(center=(hunter_x, hunter_y))
    screen.blit(hunter_img, hunter_rect)
    if not hunter_x <= 1150:
        hunter_x += -2

    else:
        hunter_y += hunter_increment_y
        if not 32 <= hunter_y <= 688:
            hunter_increment_y *= -1

    # update&clock
    pygame.display.update()
    clock.tick(120)

pygame.quit()