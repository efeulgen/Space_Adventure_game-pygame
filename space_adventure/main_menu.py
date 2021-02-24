import pygame
import sys
from assets import screen

pygame.init()
clock = pygame.time.Clock()

space_adventure_opening_img = pygame.image.load("assets/space_adventure_opening.png")
space_adventure_opening_rect = space_adventure_opening_img.get_rect(center=(640, 320))

play_img = pygame.image.load("assets/play.png")
play_rect = play_img.get_rect(center=(640, 550))


def play_main_menu():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_rect.collidepoint(event.pos):
                    running = False

        screen.fill((0, 0, 0))
        screen.blit(space_adventure_opening_img, space_adventure_opening_rect)
        screen.blit(play_img, play_rect)

        # display&update
        pygame.display.update()
        clock.tick(120)
