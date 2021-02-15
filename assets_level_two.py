import pygame
import random
from assets import screen

class BackgroundLevelTwo:
    background_img = pygame.image.load("assets/deep_space_bg_1280x720.png")
    background_1_x = 0
    background_2_x = 1280
    background_increment = -1
    background_respwan = 1280

class SpaceHunter:
    hunter_img = pygame.image.load("assets/space_hunter.png")
    hunter_x = 1300
    hunter_y = random.choice([100, 650])
    hunter_increment_y = 4

